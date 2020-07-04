from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from myapi.serializers import CustomerSerializer
from django.http import HttpResponse
import requests




class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'head']
    
def index(request):
    customers = Customer.objects.all()
    nb = len(customers)
    
    return render(request,'myapi/templates/rest_framework/index.html',{'number':nb,'customers':customers})
    #HttpResponse({nb})
def event(request):
    
    if request.method == 'POST':
        customer_id = request.POST.get("select",None)
        customer = Customer.objects.get(id=customer_id)
        args={'customer':customer.id,'name':customer.first_name,'last':customer.last_name,'city':customer.city,'email':customer.email,'gender':customer.gender,'company':customer.company,'title':customer.title,'longitude':customer.longitude,'latitude':customer.latitude}
        
        return render(request,'myapi/templates/rest_framework/event.html',args)
    
   






