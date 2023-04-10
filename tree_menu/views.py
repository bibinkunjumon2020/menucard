from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render
from .models import MenuItem

def index(request):
    #menu_items = MenuItem.objects.filter(name='main_menu')
    menu_items = MenuItem.objects.all()
    for item in menu_items:
        print(item.name)
    return render(request, 'index.html', {'menu_items': menu_items})
