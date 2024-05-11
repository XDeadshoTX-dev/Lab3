from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
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
