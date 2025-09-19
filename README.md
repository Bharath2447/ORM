# Ex02 Django ORM Web Application
## Date: 19/09/2025.

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![WhatsApp Image 2025-09-13 at 11 18 51_03b75a6c](https://github.com/user-attachments/assets/4b3d6505-77f9-4ef2-bd4f-f052b57f664b)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py
```
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

```
admin.py
```
from django.contrib import admin
from . models import car, carAdmin
admin.site.register(car, carAdmin)

```


## OUTPUT

![alt text](<Screenshot 2025-09-19 090114.png>)
![alt text](<Screenshot 2025-09-19 090124.png>)
![alt text](<Screenshot 2025-09-19 090215.png>)
![alt text](<Screenshot 2025-09-19 090225.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
