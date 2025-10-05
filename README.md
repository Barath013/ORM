# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



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

```
models.py

from django.db import models
from django.contrib import admin
class  Car_Inventory(models.Model):
    Plate_No = models.CharField(max_length=20, primary_key=True)
    Car_Model = models.CharField(max_length=100)
    Car_Type = models.CharField(max_length=20)
    Mileage = models.IntegerField()
    Engine_Type = models.CharField(max_length=15)
    Make_Date = models.DateField()
    Car_color = models.CharField(max_length=100)
class Car_InventoryAdmin(admin.ModelAdmin):
    list_display = ('Plate_No', 'Car_Model', 'Car_Type', 'Mileage','Engine_Type','Make_Date', 'Car_color')

admin.py

from django.contrib import admin
from .models import Car_Inventory, Car_InventoryAdmin
admin.site.register(Car_Inventory, Car_InventoryAdmin)
```

## OUTPUT
![alt text](<Screenshot 2025-10-05 175743.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
