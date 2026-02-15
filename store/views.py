from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import productdata 
from django.shortcuts import redirect

def landing_page(request):
    return render(request, "landingpage.html", {"is_home": True})


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
    print('product id:',proid)
    print('Qtt:',qty)
    data =req.COOKIES.get('pid')
    if data:
        data=data+","+proid+":"+qty
    else:
        data=proid+":"+qty
    response=render(req,'cart.html',{'pid':data})
    response.set_cookie('pid',data)
    return response



def shopping_cart(req):
    page = loader.get_template('cart.html')
    cookie_data = req.COOKIES.get('pid')

    cart_items = []
    grand_total = 0

    if cookie_data:
        items = cookie_data.split(',')
        for i in items:
            if ':' in i: 
                proid, qty = i.split(':')
                qty = int(qty)
                try:
                    product = productdata.objects.get(id=proid)
                    cart_items.append({'product': product, 'qty': qty})
                    grand_total += product.price * qty 
                except productdata.DoesNotExist:
                    pass 
    response = page.render({'cart_items': cart_items, 'grand_total': grand_total}, req)
    return HttpResponse(response)




def delete_cart_item(req, key):
    cookie_data = req.COOKIES.get('pid')

    if cookie_data:
        items = cookie_data.split(',')
        new_items = []

        for i in items:
            if ':' in i:
                proid, qty = i.split(':')
                if proid != key:
                    new_items.append(i)

        new_cookie_data = ','.join(new_items)

        response = redirect('shopping_cart')
        response.set_cookie('pid', new_cookie_data)
        return response

    return redirect('shopping_cart')
