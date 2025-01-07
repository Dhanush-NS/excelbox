from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Totalsolutions,Item
from django.contrib.auth.models import auth, User
from django.contrib import messages


# from .forms import ItemForm

@login_required
def home(request):
 return render(request, "home.html", {})

@login_required
def edit_view(request):
    if request.method == "POST":
        new_username = request.POST.get('username')
        if User.objects.filter(username=new_username).exists():
                messages.error(request, "Username already exists, choose another")
                return redirect('edit')

        else:
            # Update the current user's username
            user = request.user 
            user.username = new_username
            user.save()
        return redirect('edit')
    return render(request, "edit.html")

def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("exapp:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

@login_required
@never_cache
def totalsolutions(request):

    # Get search query parameters
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', 'all')
    
    # Filter the products based on the search query and category
    products = Totalsolutions.objects.all()

    if search_query:
        products = products.filter(application__icontains=search_query)
    
    if category_filter != 'all':
        products = products.filter(category=category_filter)
    
    objs = Totalsolutions.objects.all()
    return render(request, 'totalsolutions.html', {'objs': products, 'category_filter': category_filter, 'search_query': search_query})

def success(request):
   return render(request,"success.html")

@login_required
@never_cache
def additem(request):
    if request.method == "POST":
        print(request.POST)
        # Extract data from POST request
        sl_no = request.POST.get("sl_no")
        application = request.POST.get("application")
        categories = request.POST.get("categories")
        product_name = request.POST.get("product_name")
        make = request.POST.get("make")
        model = request.POST.get("model")
        specification = request.POST.get("specification")
        uom = request.POST.get("uom")
        buying_price = request.POST.get("buying_price")
        vendor = request.POST.get("vendor")
        quotation_received_date = request.POST.get("quotation_received_date")
        lead_time = request.POST.get("lead_time")
        remarks = request.POST.get("remarks")
        list_price = request.POST.get("list_price")
        discount = request.POST.get("discount")
        sales_price = request.POST.get("sales_price")
        sales_margin = request.POST.get("sales_margin")

        # Create and save an Item instance
        item = Item(
            sl_no=sl_no,
            application=application,
            categories=categories,
            product_name=product_name,
            make=make,
            model=model,
            specification=specification,
            uom=uom,
            buying_price=buying_price,
            vendor=vendor,
            quotation_received_date=quotation_received_date,
            lead_time=lead_time,
            remarks=remarks,
            list_price=list_price,
            discount=discount,
            sales_price=sales_price,
            sales_margin=sales_margin
        )
        item.save()
        
        return redirect('success')  # Redirect to a success page or another view
    # else:
        # form = ItemForm()

    return render(request, "additem.html")

