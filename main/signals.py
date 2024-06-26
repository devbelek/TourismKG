from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserRegistration, GuideRegistration


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'regular':
            UserRegistration.objects.create(user=instance)
        elif instance.role == 'guide':
            GuideRegistration.objects.create(user=instance)