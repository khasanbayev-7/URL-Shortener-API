# API uchun view
from rest_framework import viewsets
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404, redirect

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

def redirect_short_url(request, short_code):
    url_obj = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url_obj.original_url)
