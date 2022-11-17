from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Swag, Set
from .forms import CleaningForm

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
  # create a list of the sets that the swag is a part of
  id_list = swag.sets.all().values_list('id')
  # now we can query for sets whos ids are not in the list using exclude
  sets_not_apart_of = Set.objects.exclude(id__in=id_list)
  # instantiate the cleaning form to be rendered in detail.html
  cleaning_form = CleaningForm()
  return render(request, 'swag/detail.html', {
    'swag': swag,
    'cleaning_form': cleaning_form,
    'sets': sets_not_apart_of,
  })

class SwagCreate(CreateView):
  model = Swag
  fields = ['item', 'type', 'description']

class SwagUpdate(UpdateView):
  model = Swag
  fields = ['type', 'description']

class SwagDelete(DeleteView):
  model = Swag
  success_url = '/swag'
  
def add_cleaning(request, swag_id):
  # create a ModelForm instance using the data in the request.POST
  form = CleaningForm(request.POST)
  # validate the form 
  if form.is_valid():
    # do not save to the db until the swag_id FK has been assigned
    new_cleaning = form.save(commit=False) # commit=False prevents the form from saving to the db
    # we get the id from the route params
    new_cleaning.swag_id = swag_id
    # now that it has the id we can save it
    new_cleaning.save()
  #  redirect since we are performing crud
  return redirect('detail', swag_id=swag_id)

class SetList(ListView):
  model = Set

class SetDetail(DetailView):
  model = Set

class SetCreate(CreateView):
  model = Set
  fields = '__all__'

class SetUpdate(UpdateView):
  model = Set
  fields = ['name', 'genre']

class SetDelete(DeleteView):
  model = Set
  success_url = '/sets'

def assoc_set(request, swag_id, set_id):
  # get will return the object that matches the query
  # we pass the ids into our function
  Swag.objects.get(id=swag_id).sets.add(set_id)
  # redirect since we are performing crud
  return redirect('detail', swag_id=swag_id)

def rm_assoc_set(request, set_id, swag_id):
  Set.objects.get(id=set_id).swag_set.remove(Swag.objects.get(id=swag_id))
  # redirect since we are performing crud
  return redirect('detail', swag_id=swag_id)