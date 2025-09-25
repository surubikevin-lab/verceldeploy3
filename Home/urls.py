from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Django y Home app funcionando en Vercel")

urlpatterns = [
    path("", home, name="home"),
]
