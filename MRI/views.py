from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId

@csrf_exempt
@login_required
def mri_list(request):
    if request.method == 'GET':
        cliente_id = request.GET.get('cliente_id')
        if not cliente_id:
            return JsonResponse({'error': 'cliente_id is required'}, status=400)
        
        client = MongoClient(settings.MONGO_CLI)
        db = client.mri_db
        collection = db.mri

        mris = collection.find({'cliente_id': cliente_id})
        result = []
        for mri in mris:
            result.append({
                'id': str(mri['_id']),
                'cliente_id': mri.get('cliente_id'),
                'fecha': mri.get('fecha'),
                'hora': mri.get('hora'),
                'descripcion': mri.get('descripcion'),
                'imagen_url': mri.get('imagen_url'),
            })
        client.close()
        return JsonResponse(result, safe=False)

    else:
        return HttpResponse(status=405)

@csrf_exempt
@login_required
def mri_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        required_fields = ['cliente_id', 'fecha', 'hora', 'descripcion']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'Missing field: {field}'}, status=400)

        client = MongoClient(settings.MONGO_CLI)
        db = client.mri_db
        collection = db.mri

        insert_result = collection.insert_one(data)
        client.close()

        return JsonResponse({'id': str(insert_result.inserted_id), 'message': 'MRI created'}, status=201)
    else:
        return HttpResponse(status=405)
