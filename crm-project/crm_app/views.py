from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

def home(request):
    current_user = request.user
    return render(request,
                  'home.html',context=dict(current_user=current_user))
