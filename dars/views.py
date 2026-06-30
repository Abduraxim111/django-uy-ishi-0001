from django.shortcuts import render

# Create your views here.
def dars_list(request):
    return render(request,'dars.html')