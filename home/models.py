from django.db import models


# Create your models here.

class InventoryManagement(models.Model):
    name = models.CharField(max_length=122)
    composition = models.CharField(max_length=122)
    quantity = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    date =models.DateField()
    exp_date = models.DateField()
    mfg_date = models.DateField()

    def __str__(self):
	    return self.name
    
class ReOrder(models.Model):
    name = models.CharField(max_length=122)
    composition = models.CharField(max_length=122)
    quantity = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    order_date =models.DateField()

    def __str__(self):
        return self.name 
      
