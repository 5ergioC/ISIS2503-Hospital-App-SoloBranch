from celery import shared_task
from django.core.mail import send_mail
from monitoring import settings
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

    if corruptos > 0:
        send_mail(
            subject='Alerta de Integridad: Datos corruptos detectados',
            message=f'Se detectaron {corruptos} clientes con datos corruptos:\n' + "\n".join(corruptos),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['admin@tusistema.com'],  # Puedes poner aquí múltiples correos si deseas
            fail_silently=False,
        )

    return {"total": total, "corruptos": corruptos}
