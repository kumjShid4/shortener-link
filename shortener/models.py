from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.

class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_manager = super().all(*args, **kwargs)
        return qs_manager.filter(active=True)

    def refresh_codes(self, *args, **kwargs):
        query_set = URL.objects.all()
        new_codes = 0
        for q in query_set:
            q.short_code = create_shortcode(q)
            print(q.short_code)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class URL(models.Model):
    url = models.CharField(max_length=220)
    short_code = models.CharField(
        max_length=15, unique=True, null=False, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    objects = URLManager()

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_code == "" or self.short_code is None:
            self.short_code = create_shortcode(self)
        super(URL, self).save(*args, **kwargs)
