from django.db import models

# Create your models here.




class model_seller(models.Model):
    fullname=models.CharField(max_length=120)
    place=models.CharField(max_length=100)
    age=models.IntegerField()
    brand=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    photo=models.FileField(upload_to='ecommerce_app/static')
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class proadd(models.Model):
    name=models.CharField(max_length=200)
    
    size=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    choice=[
        ('Fashion','Fashion'),
        ('Jewellery','Jewellery'),
        ('Electronic','Electronic'),
    ]
    p_type=models.CharField(max_length=200,choices=choice)
    price=models.IntegerField()
    quality=models.IntegerField()
    photo=models.FileField(upload_to='ecommerce_app/static')
    color=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class model_byer(models.Model):
    fullname=models.CharField(max_length=100)
    age=models.IntegerField()
    phonenumber=models.IntegerField()
    photo=models.FileField()
    email=models.EmailField()
    password=models.CharField(max_length=100)



class wishmodel(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    pname=models.CharField(max_length=100)
    pbrand=models.CharField(max_length=100)
    price=models.IntegerField()
    photo=models.FileField()


class cartmodel(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    qty = models.IntegerField()
    pname=models.CharField(max_length=100)
    pbrand=models.CharField(max_length=100)
    price=models.IntegerField()
    photo=models.FileField()
    
    

class address_buyer(models.Model):
    userid=models.IntegerField()
    full_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    u_address=models.CharField(max_length=200)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    pin=models.IntegerField()

    def __str__(self):
        return self.full_name
    


class final_deliver(models.Model):
    user_id= models.IntegerField()
    address=models.CharField(max_length=100)
    order_date=models.DateField(auto_now_add=True)
    est_del_date=models.DateField(null=True)
    products=models.CharField(max_length=100)
    amount=models.IntegerField()

