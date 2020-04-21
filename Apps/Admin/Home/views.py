from django.shortcuts import render
from django.db.models import Count, F, Sum, Q
from datetime import timedelta, date
from django.http import JsonResponse
import collections

from Apps.Web.models import *




def header(request):

    response = {
        'new_orders'     : 0,
        'delivered_products' : 0,
        'pending_orders' : 0,
        'new_products'   : 0,
    }

    orders = Order.objects.filter(collection_center = 1, date_at=date.today()).values_list('id', flat=True)    
    
    response['new_orders']         = orders.count()
    response['pending_orders']     = orders.filter(status = 1).count()
    response['delivered_products'] = OrderDetail.objects.filter(order__in=orders.filter(status = 2)).count()
    response['new_products']       = Product.objects.filter(created_at=date.today()).count()
    #response['q'] = connection.queries

    return JsonResponse(response)

def mostRequestedProducts(request):
    response = {
        'num_details' : []
    }

    today          = date.today() + timedelta()
    sevenDaysAgo  = date.today() + timedelta(days=-7)    
    orders         = Order.objects.filter(collection_center = 1, date_at__range=(sevenDaysAgo, today), status = 2).values_list('id', flat=True)  
    order_details  = OrderDetail.objects.values('product', 'name').annotate(dcount = Count('product')).filter(order__in=orders)[0:4]    
    
    response['num_details'] = list(order_details)
    
    return JsonResponse(response)

def productsWithoutStock(request):
    products_without_stock = Product.objects.filter(stock = 0, collection_center = 1)[0:3]

    return JsonResponse( { 'products_without_stock' : products_without_stock  })

def timesVisited(request):
    collection =  CollectionCenter.objects.values('times_visited').filter(id = 1).first()

    return JsonResponse({'times_visited' : collection['times_visited']})

def ordersOkToday(r):
    num_orders = Order.objects.filter(status = 2, date_at = date.today()).count()

    return JsonResponse({'num_orders' : num_orders})

def getDonatedVsSold(r):
    response = {
        'num_details' : []
    }

    orders         = Order.objects.filter(collection_center = 1, status = 1).values_list('id', flat=True)  
    order_details  = OrderDetail.objects.values('donated', ).annotate(dcount = Count('donated'), qty = Sum('qty') ).filter(order__in=orders)    

    response['num_details'] = list(order_details)
    
    return JsonResponse(response)

def mostRequestedProductHistoric(r):
    response = {
        'num_details' : []
    }

    super_dict = []

    orders         = Order.objects.filter(collection_center = 1, status = 1).values_list('id', flat=True)      
    
    
    grouped_by = list(OrderDetail.objects.values('product',).annotate(  Sum('qty'), Sum('price')).order_by('-qty__sum').filter(order__in=orders)[0:3])
    products   = list(Product.objects.filter(id__in=map(lambda order: order['product'], grouped_by)).values('name', 'image', 'id'))


    for group in grouped_by:
        for  index, product in enumerate(products):
            if product['id'] == group['product']:
                group['name'] = product['name']                
                group['image'] = product['image']
                super_dict.append(group)
    
    response['grouped_by'] = super_dict

    return JsonResponse(response)

def getTodayOrdersNotDispatched(r):
    
    orders = list(OrderDetail.objects.filter(order__collection_center = 1, order__date_at=date.today(), order__status = 1).values('order__id', 'order__user_id', 'order__user__username', ).annotate(Sum('price')))

    return JsonResponse({'orders' : orders})