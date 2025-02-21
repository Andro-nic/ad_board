from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Response

@receiver(post_save, sender=Response)
def send_notification(sender, instance, created, **kwargs):
    if created:
        ad_author = instance.announcement.user
        send_mail(
            'Новый отклик на ваше объявление',
            f'У вас новый отклик на ваше объявление "{instance.announcement.title}".',
            'AndrSFtest@yandex.ru',
            [ad_author.email],
            fail_silently=False,
        )
