from django.shortcuts import render

# Create your views here.
def komputer_list(request):
    return render(request,'komputer.html')