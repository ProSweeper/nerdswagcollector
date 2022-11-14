from django.shortcuts import render

# Create your views here.
def home(request):
    # don't forget to add the .html since this is django it is needed
    return render(request, 'home.html')
    # we need to return from the function