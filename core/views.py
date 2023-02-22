from django.shortcuts import render, redirect

from items.models import Category, Item
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(deleted_at=None)
    categories = Category.objects.filter(deleted_at=None)

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid(): 
            form.save()
            return redirect('core:login')

    else: form = SignUpForm()
    context = {'form': form}
    return render(request, 'core/signup.html', context)


