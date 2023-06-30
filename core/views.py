from django.shortcuts import render
from .models import Place, Person


# Create your views here.
def index(request):
    obj = Place.objects.all()
    obj2 = Person.objects.all()
    return render(request, "index.html", {"result": obj, "result2": obj2})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def news(request):
    return render(request, "news.html")


def services(request):
    return render(request, "services.html")
