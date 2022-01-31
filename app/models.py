from django.db import models

# Create your models here.
class usercourier(models.Model):
	#uidd=models.ForeignKey(product_tb,on_delete=models.CASCADE,null=True)
	firstname=models.CharField(max_length=50, default="")
	lastname=models.CharField(max_length=50, default="")
	address=models.TextField(default="")
	email=models.CharField(max_length=100, default="")
	password=models.CharField(max_length=100, default="")
	status=models.CharField(max_length=100, default="")


class product_tb(models.Model):
	uid=models.ForeignKey(usercourier, on_delete=models.CASCADE, null=True)
	productname=models.CharField(max_length=50, default="")
	price=models.CharField(max_length=50, default="")
	address=models.CharField(max_length=100, default="")
	starting=models.CharField(max_length=100,default="")
	destination=models.CharField(max_length=100, default="")
	status=models.CharField(max_length=100,default="pending")

#create models for admin here............................................................................................................................
class admin_signup(models.Model):
	firstname=models.CharField(max_length=50, default="")
	lastname=models.CharField(max_length=50, default="")
	email=models.CharField(max_length=100, default="")
	gender=models.CharField(max_length=100, default="")
	password=models.CharField(max_length=100, default="")
	confirmpassword=models.CharField(max_length=100, default="")



# class tables_tb(models.Model):
# 	uid=models.ForeignKey(usercourier, on_delete=models.CASCADE, null=True)
