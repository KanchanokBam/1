from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import RegisterForm
from .models import User, Product  

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")  
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')  
def member_dashboard(request):
    products = Product.objects.all()
    return render(request, 'member/dashboard.html', {'products': products})




def home(request):
    products = Product.objects.all()
    return render(request, 'public/home.html', {'products': products})

@login_required
def profile(request):
    return render(request, 'member/profile.html')


@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)

        user.save()
        messages.success(request, "บันทึกข้อมูลสำเร็จ")
        return redirect('profile')

    return render(request, 'member/edit_profile.html')


def is_store(user):
    return user.is_authenticated and user.role == 'store'

@user_passes_test(is_store, login_url='/')
def store_dashboard(request):
    products = Product.objects.filter(store=request.user)
    return render(request, 'store/dashboard.html', {'products': products})

@user_passes_test(is_store, login_url='/login/')
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES.get('image')

        Product.objects.create(
            store=request.user,
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('store_dashboard')
    return render(request, 'store/add_product.html')

@user_passes_test(is_store, login_url='/login/')
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id, store=request.user)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('store_dashboard')

    return render(request, 'store/edit_product.html', {'product': product})

@user_passes_test(is_store, login_url='/login/')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id, store=request.user)
    product.delete()
    return redirect('store_dashboard')


