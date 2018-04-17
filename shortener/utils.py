import random
import string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    URLclass = instance.__class__
    qs_exist = URLclass.objects.filter(short_code=new_code).exists()
    if qs_exist:
        return create_shortcode(instance=instance)
    return new_code


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if "http" in reg_val or "https" in reg_val:
        new_value = reg_val
    else:
        new_value = 'https://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")
    return new_value
