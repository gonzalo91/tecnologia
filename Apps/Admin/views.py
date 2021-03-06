from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from Apps.Web.forms import ProductForm
from Apps.Web.models import *
from django.views.generic import ListView, DetailView
from datetime import date
from django.db import connection

from .Services.Home import Home
from Apps.Web.models import Order


def home(request):
    return render(request, 'admin/home/index.html')





class IndexView(ListView):
    template_name='admin/products/index.html'
    context_object_name = 'product_list'
    paginate_by = 10
    def get_queryset(self):
        return Product.objects.all().order_by('name')


def home_api(request):
    home = Home()
    response = home.all()

    return JsonResponse(response)


def action_order(request):
    if request.method == 'POST':        
        statusTo = 2 if request.POST['action'] == 'confirm' else 0
        order_id = request.POST['order_id']
        order = get_object_or_404(Order, pk=order_id)
        order.status = statusTo
        
        if order.save():
            return JsonResponse({'status' : 'ok'})   

    return JsonResponse({'status' : 'none'})





    

def productview(request):

    if request.method == 'POST':

        cpPost = request.POST.copy()        
        cpPost['collection_center_id'] = 1
        
        form = ProductForm(cpPost)     
                
        if form.is_valid():
            form.save()                                                  
            return redirect('product_index')        
        
    form = ProductForm()    
    return render(request,'admin/products/new.html',{'form': form})    

def edit(request, pk, template_name='admin/products/detail.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()        
    
    return render(request, template_name, {'form':form, 'product' : product})

def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('product_index')
    return redirect('product_index')







