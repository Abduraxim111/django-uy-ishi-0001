from django.shortcuts import render

# Create your views here.
def poyezd_list(request):
    return render(request,'poyezd.html')