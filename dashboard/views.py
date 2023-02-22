from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from items.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    context = {'items': items}

    return render(request, 'dashboard/index.html', context)
