from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def transfer(request):
    data_options = ["100MB", "250MB", "500MB", "1GB", "2GB", "5GB"]
    context = {
        'data_options': data_options
    }
    return render(request,'core/transfer.html', context)

def signup(request):
    return render(request,'core/signup.html')

def login(request):
    return render(request,'core/login.html')