from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from store.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlistt.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id= int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlistt.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':'Product already in wishlist'})
                else:
                    Wishlistt.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'Product Added Successfully to Wishlist'})
            else:
                return JsonResponse({'status':'No Such Product Found !!'})
        else:
                return JsonResponse({'status':'Login to Continue'})
    return redirect('/')  

def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id= int(request.POST.get('product_id'))
            if(Wishlistt.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem = Wishlistt.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':'Product removed from wishlist'})
            else:
                return JsonResponse({'status':'Product Not found in  Wishlist'})
        else:
            return JsonResponse({'status':'Login to Continue'})
    return redirect("/")
        
        
            