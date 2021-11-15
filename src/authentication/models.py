from django.db import models
from django.db.models import Model 
from django.contrib.auth.models import User


class products(models.Model):
    title =        models.CharField(max_length=255)
    sku =          models.CharField(max_length=255)
    description =  models.TextField(max_length=50)
    created_at =   models.DateTimeField(auto_now_add=True)
    updated_at =   models.DateTimeField(auto_now_add=True)




class products_image(models.Model):
    product_id =         models.IntegerField()
    file_path =          models.CharField(max_length=255)
    thumbnail =          models.BooleanField()
    created_at =         models.DateTimeField(auto_now_add=True)
    updated_at =         models.DateTimeField(auto_now_add=True)


class products_variants(models.Model):
    product_id =         models.IntegerField()
    variant =            models.CharField(max_length=255)
    variant_id =         models.IntegerField()
    product_id =         models.IntegerField()
    created_at =         models.DateTimeField(auto_now_add=True)
    updated_at =         models.DateTimeField(auto_now_add=True)



class products_variants_prices(models.Model):
    product_variant_one =           models.BigIntegerField()
    product_variant_two =           models.BigIntegerField()
    product_variant_three =         models.BigIntegerField()
    price =                         models.IntegerField()
    stock =                         models.IntegerField()
    product_id =                    models.IntegerField()
    created_at =                    models.DateTimeField(auto_now_add=True)
    updated_at =                    models.DateTimeField(auto_now_add=True)


class variants(models.Model):
    title =        models.CharField(max_length=255)
    description =  models.TextField(max_length=50)
    created_at =   models.DateTimeField(auto_now_add=True)
    updated_at =   models.DateTimeField(auto_now_add=True)



