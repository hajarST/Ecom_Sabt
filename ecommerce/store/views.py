from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from store.models import Product_Scrap

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

# def scrape_products(request):
#     url = 'https://www.jumia.ma/jeux-videos-consoles/'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_items = soup.find_all('a', class_='core')

#     products_scrap = []
#     for item in product_items:
#         name_element = item.find('h3', class_='name')
        
#         name = name_element.text.strip() if name_element else 'N/A'

#         price_element = item.find('div', class_='prc')
#         price = price_element.text.strip() if price_element else 'N/A'

#         image_url_element = item.find('img')
#         image_url = image_url_element['data-src'] if image_url_element and 'data-src' in image_url_element.attrs else ''

#         product_s = Product_Scrap(name=name, price=price, image_url=image_url)
#         products_scrap.append(product_s)

#     Product_Scrap.objects.bulk_create(products_scrap)

#     context = {
#         'products': products_scrap
#     }
#     return render(request, 'store/scrapping.html', context)
def scrape_products(request):
    url = 'https://www.jumia.ma/jeux-videos-consoles/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_items = soup.find_all('a', class_='core')

    products_scrap = []
    for item in product_items:
        name_element = item.find('h3', class_='name')
        name = name_element.text.strip() if name_element else 'N/A'
        price_element = item.find('div', class_='prc')
        price = price_element.text.strip() if price_element else 'N/A'
        
        image_url_element = item.find('img')
        image_url = image_url_element['data-src'] if image_url_element and 'data-src' in image_url_element.attrs else ''

        product_s = Product_Scrap(name=name, price=price, image_url=image_url)
        products_scrap.append(product_s)

    Product_Scrap.objects.bulk_create(products_scrap)

    context = {
        'products': products_scrap
    }
    return render(request, 'store/scrapping.html', context)





