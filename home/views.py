from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from datetime import datetime
from home.models import InventoryManagement
from django.contrib import messages
import re
from django.urls import reverse
from django.template import loader
from home.models import ReOrder





# Create your views here.


def index(request):
    return render(request, 'index.html')

def salesDash(request):
    return render(request, 'salesDash.html')

def pos(request):
    return render(request, 'pos.html')

def customerManage(request):
    return render(request, 'customerManage.html')

def supplierManage(request):
    return render(request, 'supplierManage.html')

def prescripProcess(request):
    return render(request, 'prescripProcess.html')

def reportAnalytics(request):
    return render(request, 'reportAnalytics.html')


def setConfig(request):
    return render(request, 'setConfig.html')

def inventoryManagement(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        composition = request.POST.get('composition')
        mfg_date = request.POST.get('mfg_date')
        exp_date = request.POST.get('exp_date')
        try:
            if((name and name.strip()) and (quantity and quantity.strip()) and (price and price.strip())):
                name = re.sub(' +', ' ', name)
                quantity = re.sub(' +', ' ', quantity)
                price = re.sub(' +', ' ', price)
                inventoryManage = InventoryManagement(name=name, quantity=quantity, price=price, date = datetime.today(), composition=composition, exp_date=exp_date, mfg_date=mfg_date)
                inventoryManage.save()
                messages.success(request, f'Medicine name is {name} with the composition {composition} is save successfully')
                name, composition = ''
            else:
                messages.warning(request, "please fill all the entries")
        except:
            # this is use the to short out the  problem of page reload auto submission
            return HttpResponseRedirect('inventoryManagement')
    data = InventoryManagement.objects.all()
    
    return render(request, 'inventoryManagement.html', 
    {
        'data' :data,
    })
    

def delete(request, id):
  medicine = InventoryManagement.objects.get(id=id)
  medicine.delete()
  return HttpResponseRedirect(reverse('inventoryManagement'))

def update(request, id):
  medicine = InventoryManagement.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'medicine': medicine,
  }
  return HttpResponse(template.render(context, request))

def updateId(request):
  if request.method == 'POST':
    id = request.POST.get('med_name')
  medicine = InventoryManagement.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'medicine': medicine,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  price = request.POST['price']
  quantity = request.POST['quantity']
  medicine = InventoryManagement.objects.get(id=id)
  medicine.price = price
  medicine.quantity = quantity
  medicine.save()
  return HttpResponseRedirect(reverse('inventoryManagement'))

def reOrder(request):
   if request.method == 'GET':
      id = request.GET['reOrderName']
      medicine = InventoryManagement.objects.get(id=id)
      name = medicine.name
      composition = medicine.composition
      quantity = request.GET['quantity_re']
      price = request.GET['price_re']
      print(name,composition,quantity,price)
      reOrder = ReOrder(name=name, composition=composition, quantity=quantity, price=price, order_date = datetime.today())
      reOrder.save()
      messages.success(request, f'{name} order successfully')
      
      return HttpResponseRedirect('inventoryManagement')













