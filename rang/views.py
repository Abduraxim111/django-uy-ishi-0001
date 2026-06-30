from django.shortcuts import render

# Create your views here.
def rang_list(request):
    return render(request,'rang.html')