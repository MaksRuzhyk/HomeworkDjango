from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'massage': 'Hello from Notes app'}
    a = ['Hello', 'World']
    context['some_list'] = a
    return render(request, 'notes/index.html', context)

def home_page(request):
    return render(request, 'notes/home_page.html')