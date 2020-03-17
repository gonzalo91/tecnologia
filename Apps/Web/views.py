from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *


# Create your views here.
def index_view(request, *args, **kwargs):
	products = Product.objects.all().order_by('id')[:8]
	collection_centers = CollectionCenter.objects.all().order_by('id')[:8]
	return render(request, "index.html", { 'products' : products, 'collection_centers' : collection_centers })

def about_view(request, *args, **kwargs):
	return render(request, "about.html",{})


def detalle_producto(request, product_id):
	product = get_object_or_404(Product, pk = product_id)

	return render(request, "detalle_producto.html", { 'product' : product })
