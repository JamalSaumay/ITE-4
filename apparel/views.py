from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import ApparelForm, SignUpForm
from .models import Item


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('dashboard')  
            else:
                login(request, user)
                return redirect('item_apparel')
        else:
            # Handle invalid login credentials
            return render(request, 'store/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'store/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('item_apparel')
    else:
        form = SignUpForm()

    return render(request, 'store/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('item_apparel')

def apparel_item(request):
    supplys = Item.objects.all()
    return render(request, 'store/item_apparel.html', {'supplys': supplys})

def apparel_detail(request, pk):
    supply = get_object_or_404(Item, pk=pk)
    return render(request, 'store/apparel_detail.html', {'supply': supply})


def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def dashboard(request):
    supplys = Item.objects.all()
    return render(request, 'store/dashboard.html', {'supplys': supplys})


@user_passes_test(is_admin)
def add_apparel(request):
    if request.method == 'POST':
        form = ApparelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_apparel')
    else:
        form = ApparelForm()
    return render(request, 'store/add_apparel.html', {'form': form})

@user_passes_test(is_admin)
def edit_apparel(request, pk):
    supply = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ApparelForm(request.POST, request.FILES, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ApparelForm(instance=supply)
    return render(request, 'store/edit_apparel.html', {'form': form, 'supply': supply})

@user_passes_test(is_admin)
def delete_apparel(request, pk):
    supply = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        supply.delete()
        return redirect('dashboard')


