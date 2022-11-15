from django.shortcuts import render
from .models import Swag

# Create your views here.
def home(request):
    # don't forget to add the .html since this is django it is needed
    return render(request, 'home.html')
    # we need to return from the function
def about(request):
    # render the about template
    return render(request, 'about.html')

def swag_index(request):
    swags = Swag.objects.all()
    return render(request, 'swag/index.html', {
        'swags': swags,
    })

def swag_detail(request, swag_id):
  swag = Swag.objects.get(id=swag_id)
  return render(request, 'swag/detail.html', {'swag': swag})