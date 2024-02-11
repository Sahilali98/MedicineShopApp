# import form class from django 
from django import forms 

# import GeeksModel from models.py 
from home.models import InventoryManagement 

# create a ModelForm 
class CreateForm(forms.ModelForm): 
	# specify the name of model to use 
	class Meta: 
		model = InventoryManagement 
		fields = "__all__"
