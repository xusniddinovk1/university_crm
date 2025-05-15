from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_telegram_notification
from .models import Payment


@receiver(post_save, sender=Payment)
def notify_admin(sender, instance, created, **kwargs):
    if created:  # Check if a new record is created
        send_telegram_notification.delay(
            payment_id=instance.id,
            quantity=instance.amount,
            student_username=instance.student.user.username,
            phone_number=instance.student.user.phone_number
        )