from django.db import models
import string, random

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortURL(models.Model):
    original_url = models.URLField(max_length=1000)
    short_code = models.CharField(max_length=15, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code
