from django.db import models
 
# Create your models here.
class register(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length= 200)
    username=models.CharField(max_length= 200)
    email=models.EmailField()
    phoneno=models.IntegerField()
    gender=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    dob=models.DateField()
    password=models.CharField(max_length=200)

class fileupload(models.Model):
    filename=models.CharField(max_length=200)
    fileimage=models.FileField(upload_to='Calculator_app\static')
    description=models.CharField(max_length=200)
class emp(models.Model):
    empname=models.CharField(max_length=200)
    email=models.EmailField()
    comname=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    phone=models.IntegerField()

class pro(models.Model):
    proname=models.CharField(max_length=200)
    proprize=models.IntegerField()
    companyname=models.CharField(max_length=200)
    quantity=models.IntegerField()
    expiry=models.DateField()
    description=models.CharField(max_length=200)

class files(models.Model):
    audioname=models.CharField(max_length=200)
    audiofile=models.FileField(upload_to='Calculator_app\static')
    videoname=models.CharField(max_length=200)
    videofile=models.FileField(upload_to='Calculator_app\static')
    pdfname=models.CharField(max_length=200)
    pdffile=models.FileField(upload_to='Calculator_app\static')

class select(models.Model):
    choice=[
        ('kerala','Kerala'), #(database,label(templates))
        ('tamil nadu','Tamil Nadu'),
        ('karnataka','Karnataka'),
    ]
    fname=models.CharField(max_length=200)
    state=models.CharField(max_length=200,choices=choice)#select
    Malayalam=models.BooleanField(default=False)
    English=models.BooleanField(default=False)
    Hindi=models.BooleanField(default=False)
   

class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name