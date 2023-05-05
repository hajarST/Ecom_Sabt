# import requests
# from bs4 import BeautifulSoup
# from django.core.files import File
# from django.utils.text import slugify
# from store.models import Product, Category
# from django.shortcuts import render

# # Make a request to the eBay page
# url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw=canon+m50&_sacat=0'
# response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the product items
# product_items = soup.select('.s-item')

# # Loop through each product item and extract the data
# for item in product_items:
#     # Extract the product details
#     name = item.select('.s-item__title')[0].get_text().strip()
#     small_description = item.select('.s-item__subtitle')[0].get_text().strip()
#     if item.select('.s-item__image-img'):
#         image_url = item.select('.s-item__image-img')[0]['src']
#         print(image_url)
#     else:
#         print("No image found for this item.")
#     quantity = int(item.select('.s-item__quantity span')[0].get_text().strip().split()[0])
#     original_price = float(item.select('.s-item__price span')[0].get_text().strip().replace(',', '').replace('£', ''))
#     selling_price = float(item.select('.s-item__price span')[1].get_text().strip().replace(',', '').replace('£', ''))

#     # Extract the category from the product name (assuming format like "Category: Product Name")
#     category_name = name.split(':')[0]
#     category, _ = Category.objects.get_or_create(name=category_name)

#     # Generate a slug for the product
#     slug = slugify(name)

#     # Download the product image and save it to Django media storage
#     response = requests.get(image_url)
#     image_file = File(response.raw)
#     image_file.name = f'{slug}.jpg'

#     # Create a new Product instance and save it to the database
#     product = Product(
#         category=category,
#         slug=slug,
#         name=name,
#         product_image=image_file,
#         small_description=small_description,
#         description='',
#         quantity=quantity,
#         original_price=original_price,
#         selling_price=selling_price,
#         status=False,
#         trending=False,
#         tag='',
#         meta_title=name,
#         meta_keywords='',
#         meta_description='',
#     )
#     product.save()
# def scrapping(request):
#     products = Product.objects.all()
#     return render(request, 'scrapping.html', {'products': products})