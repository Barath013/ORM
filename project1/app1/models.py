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
