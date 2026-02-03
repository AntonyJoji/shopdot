from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import productdata 

def landing_page(req):
    return render(req, 'landingpage.html')

def store_home(req):
    page=loader.get_template('homepage.html')
    data={}
    response =page.render(data,req)
    return HttpResponse(response)

def product_page(req):
    page=loader.get_template('product_page.html')
    db=productdata.objects.all()
    data={'product':db}
    response =page.render(data,req)
    return HttpResponse(response)

def product_details(req, key):
    page=loader.get_template('productdetails.html')
    db=productdata.objects.get(id=key)
    datas={'pro':db}
    response =page.render(datas,req)
    return HttpResponse(response)


def addtocart(req):
    proid=req.GET['proid']
    qty=req.GET['qty']
    print(proid, qty)
    response=HttpResponse("Item added to cart successfully")
    return response


def shopping_cart(req):
    page=loader.get_template('cart.html')
    db=req.COOKIES.get('pid')
    if db!=None:
        items =db.split(',')
        values={}
        print(items)
        response=page.render({},req)
    else:
        response=page.render({},req)
    return HttpResponse(response)
