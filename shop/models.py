from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	is_seller=models.BooleanField(default=False)
   
   

class Seller(models.Model):
	s_ID = models.AutoField(primary_key=True )
	s_name = models.CharField(max_length=40)
	s_email = models.CharField(max_length=255, default="")
	s_address = models.CharField(max_length=255, default="")
	s_staffmembers= models.IntegerField()
	s_quality_ofWood = models.CharField(max_length=255, default="")
	s_category_ofProduct = models.CharField(max_length=255, default="")
	s_phoneNumber = models.BigIntegerField()
	s_passwords= models.CharField(max_length=10, default="")
	class Meta:
		db_table="SellerRecords"

class Products(models.Model):
   
	p_ID = models.AutoField(primary_key=True)
	s_ID = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product")
	p_name = models.CharField(max_length=40)
	p_color = models.CharField(max_length=40, default="")
	p_price = models.IntegerField()
	p_quantity = models.IntegerField()
	p_dimensions= models.CharField(max_length=255, default="")
	p_category = models.CharField(max_length=255, default="")
	p_status = models.CharField(max_length=255, default="")
   
	p_images = models.CharField(max_length=255, default="")
	p_threedlinks = models.CharField(max_length=2000, default="")
	class Meta:
		db_table="ProductRecords"

class OrderRecords(models.Model):
	o_id = models.AutoField(primary_key=True)
	p_ID  = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="orders")
	s_ID = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="orders")
	Product_name = models.CharField(max_length=255, default="")
	Product_price = models.IntegerField()
	quantity = models.IntegerField()
	Buyers_name = models.CharField(max_length=255, default="")
	BuyersAddress = models.CharField(max_length=255, default="")
   
	BuyersContactNumber = models.BigIntegerField()
	Status = models.CharField(max_length=255, default="")
	City_name = models.CharField(max_length=255, default="")
	Country_name = models.CharField(max_length=255, default="")
   
	class Meta:
		db_table="OrderRecords"
   


class threeDfiles(models.Model):
	req_id = models.AutoField(primary_key=True)
	p_ID = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="three_d_file")
	s_ID= models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="three_d_file")
	Product_name = models.CharField(max_length=255, default="")
	Status = models.CharField(max_length=255, default="")
	Image1 = models.CharField(max_length=255, default="")


	class Meta:
		db_table="threeDfiles"



class PricingTool(models.Model):
	p_ID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=500, default="")
	price = models.CharField(max_length=500, default="")
	rating = models.CharField(max_length=500, default="")
	review_count = models.CharField(max_length=500, default="")
	availability= models.CharField(max_length=500, default="")
   
	class Meta:
		db_table="PricingTool"

class Review(models.Model):
	r_id = models.AutoField(primary_key=True)
	Reviewer_name = models.CharField(max_length=255, default="")
	rating = models.FloatField()
	comment = models.CharField(max_length=1000, default="")
	created_at = models.DateTimeField(auto_now_add=True)

   
	class Meta:
		db_table="Review"

