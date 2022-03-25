# from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Product

# Create your views here.

def home(request):
  return render(request,'capproject/home.html')



def search(request):
  if 'query' in request.GET:
    query=request.GET['query']
    products=Product.objects.filter(name__icontains=query)

  else:
        products=Product.objects.all().order_by('-price')
  
  # products= Product(request.GET,request.FILES)
  return render(request,'capproject/search.html',{'products':products})
  # else:  
    # return redirect(request,'capproject/search.html')
  
      
     
    
  # else:
  #   print("no info on product")
  #   return redirect(request,'search.html')

  # 

def display(request,):
  # if request.method =='GET':
  #   query=request.GET.get('query')
  #   if query:
  #     products = Product.objects.filter(name__icontains = query)
  # else:
  #    return request(request,'display.html')
  
  return render(request, 'capproject/display.html')    