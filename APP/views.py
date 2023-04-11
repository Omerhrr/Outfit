from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def frontend(request):
	return render(request, "frontend.html")





#======================== BACKEND SECTION ====================|


@login_required(login_url='login')
def backend(request):
	return render(request, "backend.html")