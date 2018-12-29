from django.shortcuts import render, redirect
from .forms import DogForm


# Create your views here.
def dog(request):
    context = {
        'modelform': DogForm,
    }
    return render(request, 'dogform.html', context)


def add_dog(request):
    dog_form = DogForm(request.POST)
    if dog_form.is_valid():
        dog_form.save()
    return redirect('dog')
