from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from app.models import Product
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

class ProductsManager:
    def DeleteProducts():
        Product.objects.all().delete()

    def GetProducts():
        products = Product.objects.all()
        for product in products:
            product.product_stars_range = range(product.Product_stars)
        return products
    
    def DeleteProduct(name):
        Product.objects.filter(Product_name = name).delete()
    
    def AddProduct(name, description, image_url, image, stars, available_quantity, old_price, single_price):
            new_product = Product(
            Product_name=name,
            Product_description=description,
            Product_image_url=image_url, # link image
            Product_image=image, # file from directory app/Product_images/{file}.{format}
            Product_stars=stars,
            Product_available_quantity=available_quantity,
            Product_old_price=old_price,
            Product_single_price=single_price
            )
            new_product.save()
            
class ProductsManagerHTML():
    def DeleteProductHTML(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.GET.get('product_name', None)
            
            ProductsManager.DeleteProduct(name)
    
    def AddProductHTML(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.GET.get('product_name', None)
            description = request.GET.get('product_description', None)
            image_url = request.GET.get('product_image_url', None)
            image = request.GET.get('product_image', None) # Directory must be in app/Product_images/file.jpg
            stars = request.GET.get('product_stars', None)
            available_quantity = request.GET.get('product_available_quantity', None)
            old_price = request.GET.get('product_old_price', None)
            single_price = request.GET.get('product_single_price', None)
            
            ProductsManager.AddProduct(name, description, image_url, image, stars, available_quantity, old_price, single_price)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #ProductsManager.DeleteProducts()
    #ProductsManager.AddProduct("Pineapple", "Pineapple description", None, "app/Product_images/Pineapple.jpg", 4, 142, 15.99, 9.99)
    #ProductsManager.AddProduct("Cactus", "Cactus description", "https://st.depositphotos.com/1004370/2187/i/450/depositphotos_21876019-stock-illustration-cactus.jpg", None, 2, 0, None, 20.3)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'available_products': ProductsManager.GetProducts(),
        }
    )

class GetNumberView(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            number = request.GET.get('number', None)
            return HttpResponse(f"number is {number}")
        # if number is not None and number.isdigit() and int(number) == 10:
        #     return JsonResponse({"status": "success", "message": "Number is 10"})
        # else:
        #     return JsonResponse({"status": "error", "message": "Number is not 10"})
        
class PostNameView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', None)
        if name is not None:
            return JsonResponse({"status": "success", "message": f"Hello, {name}"})
        else:
            return JsonResponse({"status": "error", "message": "Name is not provided"})
        


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
