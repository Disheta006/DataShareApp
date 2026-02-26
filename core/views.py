from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def transfer(request):
    return render(request,'core/transfer.html')