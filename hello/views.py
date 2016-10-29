from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from hello.tara import tara

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    context = tara()
    return render(request, 'index.html', context=context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

