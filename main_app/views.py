from django.shortcuts import render

swag = [
    {'item': 'Mandalorian Helmet', 'type': 'Wearable', 'description': 'Helmet from a Mandalorian'},
    {'item': 'Uruk-Hai Rubber Duck', 'type': 'Display', 'description': 'A Rubber Duck wearing Isengard armour'},
]

# Create your views here.
def home(request):
    # don't forget to add the .html since this is django it is needed
    return render(request, 'home.html')
    # we need to return from the function
def about(request):
    # render the about template
    return render(request, 'about.html')

def swag_index(request):
    # pass in the temp data for the index page to render in the third arg
    return render(request, 'swag/index.html', {
        'swag': swag,
    })