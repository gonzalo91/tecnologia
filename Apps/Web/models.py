from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CollectionCenter(models.Model):
    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    address           = models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    latitude          = models.CharField(max_length=60)
    longitude         = models.CharField(max_length=60)
    times_visited     = models.PositiveSmallIntegerField()
    status            = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    status            = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    STATUS = (
        (0, _('Inactivo')),
        (1, _('Activo') ),
    )

    CONDITIONS = (
        ('n', _('Nuevo')),
        ('u', _('Usado'))
    )

    TYPES = (
        ('p', 'Product'),
        ('s', 'Service'),
        ('m', 'Medicine'),
    )

    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    price             = models.DecimalField( max_digits=7, decimal_places=2)
    donated           = models.BooleanField(default=True)
    collection_center_id = models.ForeignKey(CollectionCenter, null=False, blank=False, on_delete=models.CASCADE)
    category_id       = models.ForeignKey(ProductCategory, null=False, blank=False, on_delete=models.CASCADE)
    type_product      = models.CharField(max_length=1, choices=TYPES)
    condition         = models.CharField(max_length=1, choices=CONDITIONS)
    stock             = models.PositiveIntegerField()
    created_at        = models.DateField( auto_now=False, auto_now_add=True)
    status            = models.PositiveSmallIntegerField(choices=STATUS)

    def Name(self):
        return '{0} $ {1}'.format(self.name, self.price)

    def statusText(self):
        return self.STATUS[self.status][1]

    def __str__(self):
        return self.Name()

class Order(models.Model):    
    user              = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    collection_center = models.ForeignKey(CollectionCenter, null=False, blank=False, on_delete=models.CASCADE)
    status            = models.PositiveSmallIntegerField()
    date_at           = models.DateField( auto_now=False, auto_now_add=False)
    created_at        = models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{0} - date: {1}'.format(self.id, self.date_at)  

class OrderDetail(models.Model):
    order   = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
    name    = models.CharField(max_length=100)
    donated = models.BooleanField(default=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    price   = models.DecimalField( max_digits=9, decimal_places=2)
    qty     = models.PositiveIntegerField()

    def __str__(self):
        return 'Order: {0} - prd: {1} - price: {2} - qty : {3} - donated : {4}'.format(self.order, self.name, self.price, self.qty, self.donated)  

class Slider(models.Model):
    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    description_detail= models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    status            = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name