from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Cat
# Create your views here.

# FUNCTION BASED VIEWS
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

# CLASS BASED VIEWS
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/' 