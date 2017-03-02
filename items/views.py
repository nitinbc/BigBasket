from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Item, Category, Price
# Create your views here.

@login_required
def home(request):
	items_list = Item.objects.all()
	
	page = request.GET.get('page', 1)

	paginator = Paginator(items_list, 10)
	try:
		items = paginator.page(page)		
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	return render(request, 'items/items_list.html', {'items':items})
