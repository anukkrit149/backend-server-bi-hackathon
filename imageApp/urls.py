"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from django.urls import path
from imageApp.views import upload_image, get_images, webhook_image, search

urlpatterns = [
    path('get/', get_images.as_view()),
    path('upload/', upload_image.as_view()),
    path('webhook/', webhook_image.as_view()),
    path('search/', search.as_view())
]