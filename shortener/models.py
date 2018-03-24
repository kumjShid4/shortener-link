from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.

class URL(models.Model):
    url = models.CharField(max_length=220)
    short_code = models.CharField(
        max_length=15, unique=True, null=False, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_code == "" or self.short_code is None:
            self.short_code = create_shortcode() 
        super(URL, self).save(*args, **kwargs)
