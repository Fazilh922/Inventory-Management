from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'vendor/index.html')
def staff(request):
    return render(request,'vendor/staff.html')
def product(request):
    return render(request,'vendor/product.html')
def order(request):
    return render(request,'vendor/order.html')
def profile(request):
    return render(request,'vendor/profile.html')
def customer_index(request):
    return render(request,'vendor/customer_index.html')
def customer_details(request):
    return render(request,'vendor/customer_details.html')
def customer(request):
    return render(request,'vendor/customer')
def product_details(request):
    return render(request,'vendor/product_details')
def product_edit(request):
    return render(request,'vendor/product_edit')
def product_delete(request):
    return render(request,'vendor/product_delete')



