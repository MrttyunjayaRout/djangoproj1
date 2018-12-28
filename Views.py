from django.shortcuts import render
from.models import Product
def input(request):
   return render(request,'input.html')
def insert(request):
   pid=int(request.GET["t1"])
   pname=request.GET["t2"]
   pcost=float(request.GET["t3"])
   pmfd=request.GET["t4"]
   pexpdt=request.GET["t5"]
   f=Product(pid=pid1,pname=pname1,pcost=pcost1,pmfd=pmfd1,pexpdt=pexpdt1)
   f.save()
   return render
def display(request):
   recs=Product.objects.all()
   return render(request,'display.html',{'records:recs'})
   


