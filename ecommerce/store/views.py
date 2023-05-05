from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def home(request):
    trending_products = Product.objects.filter(trending=1)
    context={'trending_products': trending_products}
    return render (request,"store/index.html",context)

def collections(request):
    category = Category.objects.filter(status = 0)
    context = {'category': category}
    return render (request,"store/collections.html", context)

def collectionsviews(request,slug):
    if(Category.objects.filter(slug = slug ,status = 0)):
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products , 'category': category}
        return render (request,"store/products/index.html", context)
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')
    
def productview(request, cate_slug,prod_slug):
    if(Category.objects.filter(slug = cate_slug, status=0)):
        if(Product.objects.filter(slug = prod_slug, status=0)):
            products = Product.objects.filter (slug = prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such product found")
        return redirect('collections')
    return render(request , "store/products/view.html",context)

def productListAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productList = list(products)
    return JsonResponse(productList,safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            if product:
                return redirect('collections/'+product.category.slug+'/'+ product.slug )
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Send email using Django's built-in mail function
        send_mail(
            subject,
            message,
            email,
            ['your_email@example.com'], # Replace with your own email address
            fail_silently=False,
        )

        return HttpResponse('Your message has been sent. Thank you!')

    return HttpResponse('Invalid request method')

