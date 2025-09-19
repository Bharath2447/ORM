from django.db import models
from django.contrib import admin

# Create your models here.
class car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_name = models.CharField(max_length=50)
    design = models.CharField(max_length=50)
    price = models.IntegerField()
    cate= models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_id','car_name','design','price','cate')