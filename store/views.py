from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login


def home(request):
    if request.method == 'POST':
        # poduct id send by hidden field
        product_id = request.POST.get('product')
        # this remove is used only to check weather - button is clicked or not.
        remove = request.POST.get('remove')
        # fetching the value of cart dictionary from the session database
        cart = request.session.get('cart')
        if cart:
            # here we fetching the quantity of product which is stored corresponding to the particular product id
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1

            else:
                # means card is there but that product is not availabel.
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('/')

    else:
        cart = request.session.get('cart')
        # here we are creating a cart dictionary if the user is visiting the website first time.
        if not cart:
            request.session['cart'] = {}
        data = {}
        data['products'] = Product.objects.all()
        return render(request, 'store/home.html', data)


def cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.objects.filter(id__in=ids)
    print(products)
    return render(request, 'store/cart.html', {'products': products})


def view_product(request, id):
    context = {'product': Product.objects.get(pk=id)}
    return render(request, 'store/product_detail.html', context)


# Sigup
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Your Account has been created successfully.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in Successfully !!')
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'store/login.html', {'form': form})


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
