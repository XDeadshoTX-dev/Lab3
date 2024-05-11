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

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    new_product = Product(
            Product_name="Example Product",
            Product_description="This is an example product created without a form.",
            #Product_image="https://ih1.redbubble.net/image.5051273779.4416/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg", # link image
            Product_image = "app/Product_images/Pineapple.jpg", # file from directory app/Product_images/{file}.{format}
            Product_stars=4,
            Product_available_quantity=100,
            Product_single_price=9.99
        )
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'product': new_product,
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
