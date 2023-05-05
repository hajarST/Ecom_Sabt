from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from store.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
from django.http import HttpResponse

def index(request):
    orders = Orderr.objects.filter(user= request.user)
    context = {'orders': orders}
    return render(request,"store/orders/index.html",context)

def vieworder(request,t_no):
    order = Orderr.objects.filter(tracking_no = t_no).filter(user=request.user).first()
    orderitems = OrderrItem.objects.filter(order=order)
    context = {'order': order, 'orderitems': orderitems}
    return render(request,"store/orders/view.html",context)