from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId

@login_required
def mri_list_query(request):
    cliente_id = request.GET.get('cliente_id')
    if not cliente_id:
        return JsonResponse({'error': 'cliente_id is required'}, status=400)

    client = MongoClient(settings.MONGO_CLI)
    db = client.mri_db
    col = db.mri

    docs = col.find({'cliente_id': cliente_id})
    result = []
    for d in docs:
        result.append({
            'id': str(d['_id']),
            'cliente_id': d.get('cliente_id'),
            'fecha': d.get('fecha'),
            'hora': d.get('hora'),
            'descripcion': d.get('descripcion'),
            'imagen_url': d.get('imagen_url')
        })
    client.close()
    return JsonResponse(result, safe=False)
