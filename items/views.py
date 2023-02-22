from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import NewItemForm, UpdateItemForm
from .models import Item, Category



def items(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()

    if query:
        items = Item.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))

    if category_id:
        items = Item.objects.filter(category_id=category_id)

    context = {'query':query, 'items': items, 'categories': categories, 'category_id': int(category_id)}
    return render(request, 'items/items.html', context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    context = {'item': item, 'related_items': related_items}
    return render(request, 'items/detail.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid: 
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:  form = NewItemForm()
    context = {'form': form, 'title': 'New Item'}
    return render(request, 'items/form.html', context)

@login_required
def update(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = UpdateItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid: 
            form.save()

            return redirect('items:detail', pk=item.id)
    else:  form = UpdateItemForm(instance=item)
    context = {'form': form, 'title': 'Update Item'}
    return render(request, 'items/form.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')