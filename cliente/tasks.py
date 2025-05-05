from celery import shared_task
from .models import Cliente
import logging

logger = logging.getLogger(__name__)

@shared_task
def verificar_integridad_clientes():
    total = 0
    corruptos = 0
    for cliente in Cliente.objects.all():
        total += 1
        if not cliente.verificar_integridad():
            corruptos += 1
            logger.warning(f"Cliente corrupto detectado: ID={cliente.id}, Nombre={cliente.name}")
    logger.info(f"Integridad verificada: {total - corruptos}/{total} válidos")
    return {"total": total, "corruptos": corruptos}
