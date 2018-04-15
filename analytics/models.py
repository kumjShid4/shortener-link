from django.db import models
from shortener.models import URL

# Create your models here.

class ClickManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, URL):
            obj, created = self.get_or_create(url=instance)
            if created:
                obj.count = 0
            else:
                obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickCount(models.Model): 
    url = models.OneToOneField(URL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickManager()

    def __str__(self):
        return "{i}".format(i=self.count)