from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.


class URLManager(models.Manager):
    def refresh_codes(self, *args, **kwargs):
        query_set = URL.objects.all()
        new_codes = 0
        for q in query_set:
            q.short_code = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class URL(models.Model):
    url = models.CharField(max_length=220)
    short_code = models.CharField(
        max_length=15, unique=True, null=False, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = URLManager()

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_code == "" or self.short_code is None:
            self.short_code = create_shortcode(self)
        super(URL, self).save(*args, **kwargs)

    def get_short_url(self):
        return "http://127.0.0.1:8000/{shortcode}".format(shortcode=self.short_code)