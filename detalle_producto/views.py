from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def detalle_producto(request, *args, **kwargs):
	return render(request, "detalle_producto.html", {})
