from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from app.models import  *
import os

# Create your views here.
def myfun(request):
	a=("hello iam here")
	return HttpResponse(a)
def index(request):
	return render(request,'courier/index.html')	
def about(request):
	return render(request,'courier/about.html')
def blogd(request):
	return render(request,'courier/blog-details.html')
def blog(request):
	return render(request,'courier/blog.html')
def contact(request):
	return render(request,'courier/contact.html')
def index2(request):
	return render(request,'courier/index-2.html')
def index3(request):
	return render(request,'courier/index-3.html')
def index4(request):
	return render(request,'courier/index-4.html')	
def index5(request):
	return render(request,'courier/index-5.html')	
def servicesd(request):
	return render(request,'courier/services-details.html')
def services(request):
	return render(request,'courier/services.html')	
def user(request):
	    if request.method=="POST":
	    	# ii=request.session['myid']
	    	# uid=usercourier.objects.get(id=ii)
	    	fname=request.POST['firstname']
	    	lname=request.POST['lastname']
	    	caddress=request.POST['address']
	    	cemail=request.POST['email']
	    	cpassword=request.POST['password']
	    	check=usercourier.objects.filter(email=cemail)
	    	if check:
	    		return render(request,'courier/userregistration.html',{"error":"same email"})
	    	else:
	    		add=usercourier(firstname=fname,lastname=lname,address=caddress,email=cemail,password=cpassword,status='pending')
	    		add.save()
	    		return render(request,'courier/userregistration.html')
	    else:
	    	return render(request,'courier/userregistration.html')
def product(request):
	if request.method=="POST":
		ii=request.session['myid']
		uid=usercourier.objects.get(id=ii)
		pname=request.POST['product']
		cprice=request.POST['price']
		caddress=request.POST['address']
		cstarting=request.POST['starting']
		cdestination=request.POST['destination']
		query=product_tb.objects.filter(uid=ii)

		add=product_tb(uid=uid,productname=pname,price=cprice,address=caddress,starting=cstarting,destination=cdestination)
		add.save()
		return render(request,'courier/product.html',{'prd':query})
	else:
		ii=request.session['myid']
		query=product_tb.objects.filter(uid=ii)

		return render(request,'courier/product.html',{'prd':query})


def sign(request):
	if request.method=="POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		# crpassword=request.POST['rpassword']
		check=usercourier.objects.filter(email=cemail,password=cpassword,status='approved')
		if check:
			for x in check:
				request.session["myid"]=x.id
				request.session["name"]=x.firstname

				return render(request,'courier/index.html',{"sucess":" pass matches"})
		else:
			return render(request,'courier/signin.html',{"error":"  doesnot matches or does not approved"})
	else:
			return render(request,'courier/signin.html')	


def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['name']

		logout(request)
		return HttpResponseRedirect('/')	




############################################### USER DETAILS #####################################################################





def viewuser(request):
	if request.session.has_key('myid'):
		iii=request.session['myid']
		print(iii,'--------')
		# uids=usercourier.objects.get(id=iii)
		query=usercourier.objects.filter(id=iii)
		return render(request,'courier/viewuser.html',{"qry":query})
	else:
		return render(request,'courier/viewuser.html')



def edituser(request):
	id1=request.GET['id']
	query=usercourier.objects.all().filter(id=id1)
	return render(request,'courier/updateuser.html',{"db":query})

def updateuser(request):
	if request.method=="POST":
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		caddress=request.POST['address']
		cemail=request.POST['email']
		cpassword=request.POST['password']
		userid=request.GET['id']
		usercourier.objects.filter(id=userid).update(firstname=fname,lastname=lname,address=caddress,email=cemail,password=cpassword)
		return HttpResponseRedirect('/viewuser/')
	else:
		return HttpResponseRedirect('/viewuser/')


def deleteuser(request):
	ids=request.GET['id']
	query=usercourier.objects.all().filter(id=ids)
	usercourier.objects.filter(id=ids).delete()
	query1=usercourier.objects.all()
	return render(request,'courier/viewuser.html',{"qry":query1})

def changepass(request):
	if request.session.has_key('myid'):
		if request.method=="POST":
			iii=request.session['myid']
			oldpass=request.POST['oldpass']
			newpass=request.POST['newpass']
			check=usercourier.objects.filter(id=iii,password=oldpass)
			if check:
				usercourier.objects.filter(id=iii).update(password=newpass)

				print(iii,'--------')
				# return render(request,'courier/viewuser.html')
				return HttpResponseRedirect('/viewuser/')

			else:
				return render(request,'courier/changepass.html',{"msg":"creditional doesnot matches"})

		else:
			return render(request,'courier/changepass.html')
	else:
		return render(request,'courier/signin.html')




# def oldpass(request):
# 		return render(request,'courier/forgotpass.html')

def forgotpass(request):
	if request.method=="POST":
		email=request.POST['email']
		check=usercourier.objects.filter(email=email)
		if check:
			return render(request,'courier/forgetpass.html',{"usr":check})
		else:
			return render(request,'courier/forgotpassword.html',{"error":"email doesnot registered"})
	else:
		return render(request,'courier/forgotpassword.html')


def forgetpassword(request):
	if request.method=="POST":
		newpass=request.POST['password']
		confpass=request.POST['confpassword']
		uid=request.POST['uid']
		if confpass == newpass:
			usercourier.objects.filter(id=uid).update(password=newpass)
			return HttpResponseRedirect('/signin/')	

		else:
			return render(request,'courier/forgetpass.html',{"error":"creditional doesnot matches"})
	else:
		return render(request,'courier/forgetpass.html',{"error":"creditional doesnot matches"})






def search(request):
	if request.method=="POST":
		prd=request.POST['search']
		iii=request.session['myid']
		query=product_tb.objects.filter(uid=iii,productname=prd)
		return render(request,'courier/view.html',{"qry":query})
	else:
		return render(request,'courier/view.html')




########PRODUCT DETAILS#######################

def viewproduct(request):
	if request.session.has_key('myid'):
	   idds=request.session['myid']
	  # uidss=usercourier.objects.get(id=idds)
	   query=product_tb.objects.filter(uid=idds)
	   #query=product_tb.objects.all()

	   return render(request,'courier/view.html',{"qry":query})
	else:
		return render(request,'courier/view.html')

def edit(request):
	id1=request.GET['id']
	query=product_tb.objects.all().filter(id=id1)
	return render(request,'courier/update.html',{"db":query})

def update(request):
	if request.method=="POST":
		pname=request.POST['product']
		cprice=request.POST['price']
		caddress=request.POST['address']
		cstarting=request.POST['starting']
		cdestination=request.POST['destination']
		uid=request.GET['id']
		product_tb.objects.filter(id=uid).update(productname=pname,price=cprice,address=caddress,starting=cstarting,destination=cdestination)
		return HttpResponseRedirect('/viewproduct/')
	else:
		return HttpResponseRedirect('/viewproduct/')


def delete(request):
	ids=request.GET['id']
	query=product_tb.objects.all().filter(id=ids)
	product_tb.objects.filter(id=ids).delete()
	query1=product_tb.objects.all()
	return render(request,'courier/view.html',{"qry":query1})

##########CREATE FUNCTION FOR ADMIN SIDE....................................................................................................

########### ADMIN  #################
def admin_index(request):
	if request.session.has_key('myid'):
		return render(request,'admin/index.html')
	else:
		return HttpResponseRedirect('/login/')	


def tables(request):
	if request.session.has_key('myid'):
		user=usercourier.objects.all()
		#user=usercourier.objects.all().filter(status='approved')
		return render(request,'admin/tables.html',{"user":user})
	

def producttable(request):
	if request.session.has_key('myid'):
		product=product_tb.objects.all()
		return render(request,'admin/producttable.html',{"product":product})



def signup(request):
	if request.method=="POST":
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		cemail=request.POST['email']
		cgender=request.POST['Gender']
		cpassword=request.POST['password']
		crpassword=request.POST['crpassword']
		check=admin_signup.objects.filter(email=cemail)
		if check:
			return render(request,'admin/signup.html',{"error":"same email"})
		else:
			add=admin_signup(firstname=fname,lastname=lname,email=cemail,gender=cgender,password=cpassword,confirmpassword=crpassword)
			add.save()
			return render(request,'admin/login.html')
	else:
		return render(request,'admin/signup.html')	

def login(request):
	if request.method=="POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		# crpassword=request.POST['rpassword']
		check=admin_signup.objects.filter(email=cemail,password=cpassword)
		if check:
			for x in check:
				request.session["myid"]=x.id
				return render(request,'admin/index.html',{"sucess":" pass matches"})
		else:
			return render(request,'admin/login.html',{"error":"  doesnot matches"})
	else:
			return render(request,'admin/login.html')	


def adminlogout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		logout(request)
		return HttpResponseRedirect('/login/')	
	


def approve(request):
	if request.session.has_key('myid'):
		ids=request.GET['id']
		querys=usercourier.objects.all().filter(id=ids).update(status='approved')
		return HttpResponseRedirect ('/tables/')

def productapprove(request):
	if request.session.has_key('myid'):
		idss=request.GET['id']
		queryss=product_tb.objects.all().filter(id=idss).update(status='approved')
		return HttpResponseRedirect('/producttable/')

def productreject(request):
	if request.session.has_key('myid'):
		idss=request.GET['id']
		queryss=product_tb.objects.all().filter(id=idss).update(status='reject')
		return HttpResponseRedirect('/producttable/')
