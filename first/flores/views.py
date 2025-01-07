from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # dest1 = Destination() 
    # dest1.img = 'first.png'
    # dest1.name = 'Mumbai'
    # dest1.desc = 'the city that never sleep.'
    # dest1.price = 300
    # dest1.offer = False 

    # dest2 = Destination() 
    # dest2.img = 'second.png'
    # dest2.name = 'Delhi'
    # dest2.desc = 'the city that never stop.'
    # dest2.price = 600
    # dest2.offer = True 

    # dests = [dest1, dest2]
    
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
