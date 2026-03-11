from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def transfer(request):
    data_options = ["50MB", "100MB", "150MB", "200MB", "500MB", "1GB"]
    context = {
        'data_options': data_options
    }
    return render(request,'core/transfer.html', context)

def signup(request):
    return render(request,'core/signup.html')

def login(request):
    return render(request,'core/login.html')

def forget_password(request):
    return render(request,'core/forget_password.html')

def verify_code(request):
    return render(request,'core/verify_code.html')

def reset_password(request):
    return render(request,'core/reset_password.html')

def support(request):
    return render(request,'core/support.html')