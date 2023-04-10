from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import Seller,Products,OrderRecords,User,threeDfiles,PricingTool,Review
from .forms import PasswordResetForm

from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.db.models.query_utils import Q

#import sqlite3
#from django.contrib.auth  import authenticate,  login, logout




# Create your views here.
from .forms import PasswordResetForm,SetPasswordForm

...





def home(request):
	return render(request,"shop/index.html")

	
def shoppingcart(request):
	return render(request,"shop/shoppingcart.html")



def about(request):
	return render(request,"shop/about.html") 


def rateus(request):
	url = request.META.get('HTTP_REFERER')
	if request.method == 'POST':
		Reviewer_name=request.POST.get('Reviewer_name')
		rating=request.POST.get('rating')
		comments=request.POST.get('comments')
		data= Review(Reviewer_name=Reviewer_name,rating=rating,comment=comments)
		data.save()
		return redirect(url)

	return render(request,"shop/rateus.html") 

def comments(request):
	results=Review.objects.all()
	return render(request,"shop/test.html",{"data":results})



def Beds(request):
	order_by = request.GET.get('order_by')
	if order_by == 'highest':
		# the variable is set in the url
		beds = Products.objects.filter(p_category='Beds').order_by('-p_price')
	elif order_by == 'lowest':
		# The variable is not set
		beds = Products.objects.filter(p_category='Beds').order_by('p_price')
	else:
		beds=Products.objects.filter(p_category='Beds')

	return render(request,"shop/Beds.html",{"data":beds})


def chairs(request):
	order_by = request.GET.get('order_by')
	if order_by == 'highest':
		# the variable is set in the url
		chairs=Products.objects.filter(p_category='Chairs').order_by('-p_price')
	elif order_by == 'lowest':
		# The variable is not set
		chairs=Products.objects.filter(p_category='Chairs').order_by('p_price')
	else:
		chairs=Products.objects.filter(p_category='Chairs')
	
	return render(request,"shop/chairs.html",{"data":chairs}) 




def sofas(request):
	order_by = request.GET.get('order_by')
	if order_by == 'highest':
		# the variable is set in the url
		Sofas=Products.objects.filter(p_category='Sofas').order_by('-p_price')
	elif order_by == 'lowest':
		# The variable is not set
		Sofas=Products.objects.filter(p_category='Sofas').order_by('p_price')
	else:
		Sofas=Products.objects.filter(p_category='Sofas')
   
	return render(request,"shop/sofas.html",{"data":Sofas}) 

def table(request):
	order_by = request.GET.get('order_by')
	if order_by == 'highest':
		# the variable is set in the url
		Tables=Products.objects.filter(p_category='Tables').order_by('-p_price')
	elif order_by == 'lowest':
		# The variable is not set
		Tables=Products.objects.filter(p_category='Tables').order_by('p_price')
	else:
		Tables=Products.objects.filter(p_category='Tables')
	
	return render(request,"shop/table.html",{"data": Tables}) 

#admin side

def loginadmin(request):
  
	if request.method == "POST":
		#get the parameters
	 
	   
		username=request.POST['username']
		password=request.POST['password']
   
		Admin=authenticate( username=username, password=password)
		if Admin is not None and Admin.is_superuser==True:
			login(request,Admin)
		
			# messages.success(request, "Successfully Logged In")
			return render(request,"shop/adminhome.html") 
	return render(request,"shop/loginadmin.html") 

def logoutadmin(request):
   logout(request)
   return redirect("loginadmin")
		 
	
def adminhome(request):
	if request.user.is_authenticated and request.user.is_superuser:
		return render(request,"shop/adminhome.html") 
	else:
		return redirect("loginadmin")
def sellerinfo(request):
	if request.user.is_authenticated and request.user.is_superuser:
		results=Seller.objects.all()
		return render(request,"shop/sellerinfo.html",{"data":results})
	else:
		return redirect("loginadmin") 
	
def uploadmodel(request,req_id):
	if request.user.is_authenticated and request.user.is_superuser:
		print(request.method)
		if request.method=="POST":
			#get the parameters
			#print("i am inblock",request.method)
			
			p_threedlinks=request.POST.get('threedlinks','')
			#print("i am link",p_threedlinks)

		
			obj=threeDfiles.objects.filter(req_id=req_id).values_list('p_ID',flat=True).order_by('p_ID')[0]
			#p_ID=obj.p_ID
			Products.objects.filter(p_ID=obj).update(p_threedlinks=p_threedlinks)
			threeDfiles.objects.filter(req_id=req_id).update(Status="Approved")
			return render(request,"shop/uploadmodel.html")
			
		else:
			
			return render(request,"shop/uploadmodel.html")
	else:
		return redirect("loginadmin")
	
	
def threedinfo(request):
	if request.user.is_authenticated and request.user.is_superuser:
		results=threeDfiles.objects.filter(Status="pending").select_related('s_ID')
		print({"data":results})
		return render(request,"shop/request_3d.html",{"data":results})
	else:
		return redirect("loginadmin") 
	
def declinemodel(request,req_id):
	if request.user.is_authenticated and request.user.is_superuser:
		if request.method=="GET":
			threeDfiles.objects.filter(req_id=req_id).update(Status="declined")
			return redirect(threedinfo)
	else:
		return redirect("loginadmin") 
	
#### seller side
def signup_seller(request):
	if request.method == "POST":
		#get the parameters
	 
		username=request.POST['name']
		email=request.POST['email']
		address=request.POST['address']
		staff_members=request.POST['staff_members']
		qualityofwood=request.POST['qualityofwood']
		s_category_ofProduct=request.POST['Categories']
		phone_number=request.POST['phone_number']
		#confirm_password=request.POST[' confirm_password']
		password=request.POST['password']
		#account_type
	
		data =Seller(s_name=username,s_email=email,s_address=address,
					s_staffmembers=staff_members,s_quality_ofWood=qualityofwood,s_category_ofProduct= s_category_ofProduct, 
					s_phoneNumber= phone_number, s_passwords= password)
	
	 
		my_user=User.objects.create_user(username,email,password)
		my_user.is_seller=True  
		my_user.save()   
		id=my_user.id  
		data =Seller(s_ID=id,s_name=username,s_email=email,s_address=address,
					s_staffmembers=staff_members,s_quality_ofWood=qualityofwood,s_category_ofProduct= s_category_ofProduct, 
					s_phoneNumber= phone_number, s_passwords= password)
		data.save()
	   # messages.success(request,"your account has been successfully created")
		return redirect("loginseller")
	   
	return render(request,"shop/signup_seller.html") 

def loginseller(request):
  
	if request.method == "POST":
		#get the parameters
	 
	   
		username=request.POST['username']
		password=request.POST['password']
   
		user=authenticate(username=username,password=password)
		if user is not None and user.is_seller==True:
			login(request, user)
			# messages.success(request, "Successfully Logged In")
			return render(request,"shop/homepageSeller.html")
		 
		
	return render(request,"shop/loginseller.html")
def logoutseller(request):
	logout(request)
	print("logout")
	return redirect("loginseller")

def homepageSeller(request):
	if request.user.is_authenticated and request.user.is_seller:
		return render(request,"shop/homepageSeller.html") 
	else:
		return redirect("loginseller")
   

def addProduct(request):
	if request.user.is_authenticated and request.user.is_seller:
		if request.method == "POST":
		
			Product_Name=request.POST['Product_Name']
			Color=request.POST['Color']
			Price=request.POST['Price']
			quantity=request.POST['quantity']
			Dimensions=request.POST['Dimensions']
			category=request.POST['category']
			status=request.POST['status']
			Image=request.POST['Image']
		
			request3dmodel=request.POST['request3dmodel']
			seller_object = Seller.objects.filter(s_ID=request.user.id)
			data1 =Products(s_ID=seller_object,p_name=Product_Name,p_color=Color,p_quantity=quantity,p_price=Price, p_dimensions=Dimensions, p_category=category,  p_status=status, 
					p_images=Image)
			
			results=Products.objects.all()
			data1.save()
			if request3dmodel=="request3dmodel":

				Product_object = Products.objects.filter(s_ID=request.user.id)
				print(Product_object)
				data2=threeDfiles(p_ID=Product_object,s_ID=seller_object, Status="pending",  Image1=Image,Product_name=Product_Name)
				data2.save()
				 
		   
			return render(request,"shop/seeProducts.html",{'data':results}) 



		else:
			print(request.user)
			return render(request,"shop/addProduct.html",{'s_ID':request.user.id}) 
	else:
		return redirect("loginseller")
	

def request3d(request,p_ID):
	if request.user.is_authenticated and request.user.is_seller==True:
		if request.method=="POST":
			seller_object = Seller.objects.get(s_ID=request.user.id)
			product_object = Products.objects.get(p_ID=p_ID)
			Product_Name=request.POST.get('Product_Name')
			p_images=request.POST.get('Image')
			print("Product_Name:", Product_Name)
			print("p_images:", p_images)


			data2=threeDfiles(p_ID=product_object,s_ID=seller_object, Status="pending",Image1=p_images,Product_name=Product_Name)
			data2.save()
			print("data saved")
			results=Products.objects.filter(s_ID=request.user.id)
		 
			#messages.success(request, "Your request has been sent to the admin")
		
			return render(request,"shop/seeProducts.html",{"data":results})
		else:
			products = Products.objects.get(p_ID=p_ID)
			return render(request,"shop/request3d.html",{"products":products})
	else:
		return redirect("loginseller")


def editProduct(request,p_ID):

	if request.user.is_authenticated and request.user.is_seller==True:
		if request.method=="POST":
			print(request.POST)
			product = Products.objects.get(pk=p_ID)
			product.p_name = request.POST.get("Product_Name")
			product.p_color = request.POST.get("Color")
			product.p_price = request.POST.get("Price")
			product.p_dimensions= request.POST.get("Dimensions")
			product.p_category = request.POST.get("category")
			product.p_status = request.POST.get("status")

			if request.POST.get("Image"):
				product.p_images = request.POST.get("Image")

			product.save()

			results = Products.objects.all()
	
			return render(request,"shop/seeProducts.html", {'data': results})
		else: 
			products = Products.objects.get(p_ID=p_ID)
			
			return render(request,'shop/editproduct.html', {'products': products})
	else:
		 return redirect("loginseller") 



def destroy(request, p_ID):  
	products = Products.objects.get(p_ID=p_ID)  
	products.delete()  
	return redirect("seeProducts")   

   
def orderRecords(request):
	if request.user.is_authenticated and request.user.is_seller==True:
		results=OrderRecords.objects.filter(s_ID=request.user.id)
		print(results)
		return render(request,"shop/orderRecords.html",{"data":results}) 
	else:
		return redirect("loginseller")
	
	
def shipped(request,o_id):
	if request.user.is_authenticated and request.user.is_seller==True:
		OrderRecords.objects.filter(o_id=o_id).update(Status="Shipped")
		return redirect("orderRecords")

	else:
		return redirect("loginseller")

def delivered(request,o_id):
	if request.user.is_authenticated and request.user.is_seller==True:
		OrderRecords.objects.filter(o_id=o_id).update(Status="Delivered")
		return redirect("orderRecords")

	else:
		return redirect("loginseller")

def pricingTool(request):
	if request.user.is_authenticated and request.user.is_seller==True:
		results=PricingTool.objects.all()
		return render(request,"shop/pricingTool.html",{"data":results}) 
	else:
		return redirect("loginseller")
	

def seeProducts(request):
	if request.user.is_authenticated and request.user.is_seller==True:
		results=Products.objects.filter(s_ID=request.user.id)
		return render(request,"shop/seeProducts.html",{"data":results}) 
	else:
		return redirect("loginseller")
	

def requestinfo(request):
	if request.user.is_authenticated and request.user.is_seller==True:
		results=threeDfiles.objects.filter(s_ID=request.user.id)
		return render(request,"shop/requestinfo.html",{"data":results}) 
	else:
		return redirect("loginseller")
	

def password_reset_request(request):
	form = PasswordResetForm()
	return render( request=request, template_name="password_reset.html", context={"form": form})

def passwordResetConfirm(request, uidb64, token):
	
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except:
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		if request.method == 'POST':
			form = SetPasswordForm(user, request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
				return redirect('loginseller')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)

		form = SetPasswordForm(user)
		return render(request, 'shop/password_reset_confirm.html', {'form': form})
	else:
		messages.error(request, "Link is expired")

	messages.error(request, 'Something went wrong, redirecting back to Homepage')
	return redirect("loginseller")



def password_change(request):
	
	if request.user.is_authenticated and request.user.is_seller:
		user = request.user
		if request.method == 'POST':
			form = SetPasswordForm(user, request.POST)
			
			if form.is_valid():
				#password = form.clean['password1']
				
				form.save()
				Seller.objects.filter(s_ID=request.user.id).update(s_passwords=request.user.password)
				print("password changed")
				#messages.success(request, "Your password has been changed")
				return redirect('loginseller')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)

		form = SetPasswordForm(user)
		return render(request, 'shop/password_reset_confirm.html', {'form': form})
	else:
		return redirect('loginseller')
	

def password_reset_request(request):
	if request.method == 'POST':
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			associated_user = User.objects.filter(Q(email=user_email)).first()
			if associated_user:
				subject = "Password Reset request"
				message = render_to_string("shop/template_reset_password.html", {
					'user': associated_user,
					'domain': get_current_site(request).domain,
					'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
					'token': account_activation_token.make_token(associated_user),
					"protocol": 'https' if request.is_secure() else 'http'
				})
				email = EmailMessage(subject, message, from_email='arfurnitureweb@gmail.com', to=[user_email])
				if email.send():
					messages.success(request, """
						<h2>Password reset sent</h2><hr>
						<p>
							We've emailed you instructions for setting your password, if an account exists with the email you entered. 
							You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
							you registered with, and check your spam folder.
						</p>
					""")
					return redirect('loginseller')
				else:
					messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")
			else:
				messages.error(request, "Email address not found, please try again.")
	else:
		form = PasswordResetForm()
	return render(request, "shop/password_reset_form.html", context={"form": form})


def checkout(request):
    thank = False
    id = None
    if request.method=="POST":
        p_ID = request.POST.get('p_ID')
        s_ID = request.POST.get('s_ID')
        Product_name = request.POST.get('Product_name').strip('"')
        Product_price = request.POST.get('Product_price')
        quantity = request.POST.get('quantity')
        Buyers_name = request.POST.get('Buyers_name')
        BuyersAddress = request.POST.get('BuyersAddress')
    
        BuyersContactNumber = request.POST.get('BuyersContactNumber')
        ShippingStatus = request.POST.get('ShippingStatus')
        City_name = request.POST.get('City_name')
        Country_name =request.POST.get('Country_name')
        
        # Retrieve the p_ID and s_ID values from the Productss and SellerRecords models respectively
        try:
            product = Products.objects.get(p_name=Product_name)
            p_ID = product
            s_ID = product.s_ID
        except Products.DoesNotExist:
            raise ValueError(f"Product '{Product_name}' not found")
        
        if product.p_quantity >= int(quantity):
            order = OrderRecords(p_ID=p_ID,s_ID=s_ID,Product_name=Product_name, Product_price=Product_price, quantity=quantity,Buyers_name=Buyers_name,BuyersAddress=BuyersAddress,BuyersContactNumber=BuyersContactNumber,Status=ShippingStatus,City_name=City_name,Country_name=Country_name)
            order.save()
            
            # Subtract the quantity from the Products table
            product.p_quantity -= int(quantity)
            product.save()
            
            thank=True
            id=order.o_id
            return render(request, 'shop/checkoutform.html', {'thank':thank, 'id':id})
        else:
            thank = False
            error_msg = f"Transaction not successful. Product is not available.We will get you notified when it is available."
            messages.error(request, error_msg)
            return render(request, 'shop/checkoutform.html', {'error_msg': error_msg})
        #return render(request, 'shop/checkoutform', {'thank':thank, 'id':id})
    return render(request, 'shop/checkoutform.html', {'thank':thank, 'id':id})






