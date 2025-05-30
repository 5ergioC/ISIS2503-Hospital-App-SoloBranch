from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from pymongo import MongoClient
from django.conf import settings

@csrf_exempt
@login_required
def mri_command(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # validar campos mínimos
        required = ['cliente_id', 'fecha', 'hora', 'descripcion']
        for field in required:
            if field not in data:
                return JsonResponse({'error': f'Missing {field}'}, status=400)

        client = MongoClient(settings.MONGO_CLI)
        db = client.mri_db
        col = db.mri
        col.insert_one(data)
        client.close()
        return JsonResponse({'message': 'MRI created'}, status=201)
    else:
        return HttpResponse(status=405)
