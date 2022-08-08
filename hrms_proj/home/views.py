
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from calendar import monthrange
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
import os
from datetime import date, timedelta
from django.db.models import Q
# Create your views here.

# login **************************************************************

@never_cache
def user_login(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(dashboard)
        else:
            messages.success(request,"Incorrect Username or Password")
            return redirect(user_login)
    return render(request,'login.html')


# logout **************

@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect(user_login)

# end  login **************************************************************



# dashboard
@login_required(login_url='/') 
@never_cache  
def dashboard(request):
    send_mail_user(request)
    no_employee=len(Employee.objects.all())
    no_company=len(Company.objects.all())
    no_catogery=len(Category.objects.all())
    no_branch=len(Branch.objects.all())
    username = request.user.username
    dict_dash={
        'no_employee':no_employee,
        'no_company':no_company,
        'no_catogery':no_catogery,
        'no_branch':no_branch,
        "user":username
    }
    return render(request,'dashboard.html',dict_dash)

# addemployee
@login_required(login_url='/')
def addemployee(request):
    dict_emp={
        'company':Company.objects.all(),
        'catogory':Category.objects.all(),
        'branch':Branch.objects.all()
    }
    return render(request,'add_employee.html',dict_emp)


@login_required(login_url='/')
def get_addemployee(request):
    if request.method == "POST":
        emp=Employee()
        user_id = request.user.id
        if len(request.FILES)!=0:
            try:
                upload_image=request.FILES['image']
                emp.upload_image=upload_image
            except:
                pass

            try:
                insurence_copy=request.FILES['insurence_copy']
                emp.insurance_copy=insurence_copy
            except:
                pass

            try:
                passport_copy=request.FILES['passport_copy']
                emp.passport_copy=passport_copy
            except:
                pass

            try:
                visa_copy=request.FILES['visa_copy']
                emp.visa_copy=visa_copy
            except:
                pass
          
            try:
                emirates_copy=request.FILES['emirates_copy']
                emp.emirates_copy=emirates_copy
            except:
                pass

            try:
                other_document=request.FILES['other_document']
                emp.other_document=other_document
            except:
                pass

        try:
            company=request.POST['company']
            company_id = Company.objects.get(id = company)
            emp.company=company_id
        except:
            pass

        try:
            catogory=request.POST['catogory']
            catogory_id=Category.objects.get(id=catogory)
            emp.catogory=catogory_id
        except:
            pass

        try:
            branch=request.POST['branch']
            branch_id=Branch.objects.get(id=branch)
            emp.branch=branch_id
        except:
            pass
              
        if len(request.POST['passport_expiry']) !=0:
            passport_expiry=request.POST['passport_expiry']
            emp.passport_expiry=passport_expiry

        if len(request.POST['visa_expiry']) !=0:
            visa_expiry=request.POST['visa_expiry']
            emp.visa_expiry=visa_expiry

        if len(request.POST['emirates_expiry']) !=0:
            emirates_expiry=request.POST['emirates_expiry']
            emp.emirates_expiry=emirates_expiry


        if len(request.POST['insurence_expiry']) !=0:
            insurence_expiry=request.POST['insurence_expiry']
            emp.insurence_expiry=insurence_expiry
        
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        dob=request.POST['dob']
        emp_id=request.POST['emp_id']
        uid=request.POST['uid']
        gender=request.POST['gender']
        blood=request.POST['blood']
        mobail_no=request.POST['mobail_no']
        passport_number=request.POST['passport_number']
        visa=request.POST['visa']
        emirates=request.POST['emirates']
        insurence=request.POST['insurence']
        notification_email=request.POST['notification_email']
        user=User.objects.get(id=user_id)
        emp.user=user       
        emp.fname=fname
        emp.lname=lname      
        emp.email=email
        emp.dob=dob
        emp.emp_id=emp_id
        emp.uid=uid
        emp.gender=gender
        emp.blood=blood
        emp.mobail_no=mobail_no
        emp.passport_number=passport_number
        emp.visa=visa
        emp.emirates=emirates            
        emp.insurence=insurence
        emp.notification_email=notification_email
        emp.save()
        return redirect(addemployee)


# listemployee
@login_required(login_url='/')
def listemployee(request):
    if request.method == "POST":
        branch = request.POST['branch']
        company = request.POST['company']
        category = request.POST['catogary']
        if len(branch) == 0 and len(company) == 0 and len(category)==0:
            employee=Employee.objects.all()
        elif len(branch) != 0 and len(company) == 0 and len(category)==0:
            employee=Employee.objects.filter(branch=branch)
        elif len(branch) == 0 and len(company) != 0 and len(category)==0:
            employee=Employee.objects.filter(company=company)        
        elif len(branch) == 0 and len(company) == 0 and len(category)!=0:
            employee=Employee.objects.filter(catogory=category)
        elif len(branch) != 0 and len(company) != 0 and len(category)==0:
            employee=Employee.objects.filter(branch=branch,company=company)
        elif len(branch) != 0 and len(company) == 0 and len(category)!= 0:
            employee=Employee.objects.filter(branch=branch,catogory=category)
        elif len(branch) == 0 and len(company) != 0 and len(category)!=0:
            employee=Employee.objects.filter(company=company,catogory=category)
        elif len(branch) != 0 and len(company) != 0 and len(category)!=0:
            employee=Employee.objects.filter(branch=branch,company=company,catogory=category)
        dict_employee ={
            'employee':employee,
            'catogary':Category.objects.all(),
            'company':Company.objects.all(),
            'branch':Branch.objects.all()
        }
        return render(request,'emplist.html',dict_employee)
    else:
        dict_employee ={
            'employee':Employee.objects.all(),
            'catogary':Category.objects.all(),
            'company':Company.objects.all(),
            'branch':Branch.objects.all()
        }
        return render(request,'emplist.html',dict_employee)


@login_required(login_url='/')
def edit_employee(request ,id):
    dict_edit={
        'employee_intance':Employee.objects.get(id=id),
        'catogary':Category.objects.all(),
        'company':Company.objects.all(),
        'branch':Branch.objects.all()
    }
    return render(request,'emp_list_update.html',dict_edit)


@login_required(login_url='/')
def get_edit_employee(request,id):
    try:
        if request.method == 'POST':
            emp=Employee.objects.get(id=id)
            user_id = request.user.id
            if len(request.FILES)!=0:
                try:
                    upload_image=request.FILES['image']
                    image_path=emp.upload_image.path
                    emp.upload_image=upload_image
                    os.remove(image_path)
                except:
                    pass

                try:
                    insurance_copy=request.FILES['insurence_copy']             
                    insurence_path=emp.insurance_copy.path
                    emp.insurance_copy=insurance_copy
                    os.remove(insurence_path)
                except:
                    pass
            
                try:
                    passport_copy=request.FILES['passport_copy']
                    passport_path=emp.passport_copy.path
                    emp.passport_copy=passport_copy
                    os.remove(passport_path)
                except:
                    pass

                try:
                    visa_copy=request.FILES['visa_copy']
                    visa_path=emp.visa_copy.path
                    emp.visa_copy=visa_copy
                    os.remove(visa_path)
                except:
                    pass

                try:
                    emirates_copy=request.FILES['emirates_copy']
                    emirates_path=emp.emirates_copy.path
                    emp.emirates_copy=emirates_copy    
                    os.remove(emirates_path)
                except:
                    pass

                try:
                    other_document=request.FILES['other_document']
                    other_document_path=emp.other_document.path
                    emp.other_document=other_document                    
                    os.remove(other_document_path)
                except:
                    pass
    
            try:
            
                if len(request.POST['dob']) !=0:
                    dob=request.POST['dob']
                    f_dob=datetime.strptime(dob,"%Y-%m-%d").date()
                    emp.dob=f_dob

                if len(request.POST['passport_expiry']) !=0:
                    passport_expiry=request.POST['passport_expiry']
                    f_passport_expiry=datetime.strptime(passport_expiry,"%Y-%m-%d").date()
                    emp.passport_expiry=f_passport_expiry

                if len(request.POST['visa_expiry']) !=0:
                    visa_expiry=request.POST['visa_expiry']
                    f_visa_expiry=datetime.strptime(visa_expiry,"%Y-%m-%d").date()
                    emp.visa_expiry=f_visa_expiry


                if len(request.POST['emirates_expiry']) !=0:
                    emirates_expiry=request.POST['emirates_expiry']
                    f_emirates_expiry=datetime.strptime(emirates_expiry,"%Y-%m-%d").date()
                    emp.emirates_expiry=f_emirates_expiry


                if len(request.POST['insurence_expiry']) !=0:
                    insurence_expiry=request.POST['insurence_expiry']
                    f_insurence_expiry=datetime.strptime(insurence_expiry,"%Y-%m-%d").date()
                    emp.insurence_expiry=f_insurence_expiry


            except:
                return HttpResponse("<script>alert('failed');window.history.back()</script>")

            try:
                company=request.POST['company']
                company_id = Company.objects.get(id = company)
                emp.company=company_id
            except:
                pass

            try:
                catogory=request.POST['catogory']
                catogory_id=Category.objects.get(id=catogory)
                emp.catogory=catogory_id
            except :
                pass

            try:
                branch=request.POST['branch']
                branch_id=Branch.objects.get(id=branch)
                emp.branch=branch_id
            except :
                pass            
                
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            emp_id=request.POST['emp_id']
            uid=request.POST['uid']
            gender=request.POST['gender']
            blood=request.POST['blood']
            mobail_no=request.POST['mobail_no']
            passport_number=request.POST['passport_number']
            visa=request.POST['visa']
            emirates=request.POST['emirates']
            insurence=request.POST['insurence']
            notification_email=request.POST['notification_email']
            user=User.objects.get(id=user_id)
            emp.user=user   
            emp.fname=fname
            emp.lname=lname
            emp.email=email
            emp.emp_id=emp_id
            emp.uid=uid
            emp.gender=gender
            emp.blood=blood
            emp.mobail_no=mobail_no
            emp.passport_number=passport_number
            emp.visa=visa
            emp.emirates=emirates
            emp.insurence=insurence
            emp.notification_email=notification_email
            emp.save()
            return redirect(listemployee)
    except:
        return HttpResponse("<script>alert('failed');window.history.back()</script>")


@login_required(login_url='/')
def delete_employee(request,id):
    employee_instance=Employee.objects.get(id=id)
    employee_instance.delete()
    return redirect(listemployee)
    

# expairydetails
@login_required(login_url='/')
def expairydetails(request):
    if request.method == "POST":
        branch = request.POST['branch']
        company = request.POST['company']
        category = request.POST['catogary']
        expiry_category = request.POST['expiry_category']
        days_of_expiry = request.POST['days_of_expiry']
        month_expiry_date = date.today().replace(day=1) + timedelta(days=29)

        ten_day_expiry=date.today() + timedelta(days=10)

        one_week_expiry=date.today() + timedelta(weeks=1)

        this_month_last = date.today().replace(day=1) + timedelta(days=29)
        next_month_expiry=date.today().replace(day=30) + timedelta(days=this_month_last.day)

        three_month_expiry=date.today().replace(day=1) + timedelta(days=120)
        
        one_year_expiry=date.today().replace(month=12,day=30) + timedelta(days=365)

        if len(branch) == 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) == 0:
            employees=Employee.objects.all()
        elif len(branch) != 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) == 0:
            employees=Employee.objects.filter(branch=branch)
        elif len(branch) == 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) == 0:
            employees=Employee.objects.filter(company=company) 
        elif len(branch) == 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) == 0 and len(days_of_expiry) == 0:
            employees=Employee.objects.filter(catogory=category)

        elif len(branch) == 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) != 0 and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter(passport_expiry__lte=month_expiry_date)  
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter(emirates_expiry__lte=month_expiry_date)
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter(visa_expiry__lte=month_expiry_date)
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter(insurence_expiry__lte=month_expiry_date)

        elif len(branch) == 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) != 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) == 0  and len(days_of_expiry) == 0:
            employees=Employee.objects.filter( Q(branch=branch) & Q(company=company))
        elif len(branch) != 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) == 0 and len(days_of_expiry) == 0:
            employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category))

        elif len(branch) != 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) != 0 and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(passport_expiry__lte=month_expiry_date)) 
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(emirates_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(visa_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(insurence_expiry__lte=month_expiry_date))
        
        elif len(branch) != 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) == 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) == 0  and len(days_of_expiry) == 0:
            employees=Employee.objects.filter( Q(company=company) & Q(catogory=category))
        elif len(branch) == 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) != 0 and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(company=company) & Q(passport_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(company=company) & Q(emirates_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(company=company) & Q(visa_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(company=company) & Q(insurence_expiry__lte=month_expiry_date))

        elif len(branch) == 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) == 0 and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(company=company) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(company=company) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))


        elif len(branch) == 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) != 0 and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date))
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date))

        elif len(branch) == 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) == 0 and len(days_of_expiry) != 0:

            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) == 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) != 0 and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry))  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_year_expiry))        

        elif len(branch) != 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) == 0  and len(days_of_expiry) == 0:
            employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(catogory=category) )   

        elif len(branch) != 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) != 0  and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(passport_expiry__lte=month_expiry_date))           
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(emirates_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(visa_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(insurence_expiry__lte=month_expiry_date))  

        elif len(branch) != 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) == 0  and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(company=company) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(company=company) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(company=company) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) != 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date))           
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date))  


        elif len(branch) != 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) == 0  and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(catogory=category) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(catogory=category) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(catogory=category) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))


        elif len(branch) != 0 and len(company) == 0 and len(category) == 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_year_expiry))        

        elif len(branch) == 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category)  & Q(passport_expiry__lte=month_expiry_date))           
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category)  & Q(emirates_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category)  & Q(visa_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category)  & Q(insurence_expiry__lte=month_expiry_date))  

        elif len(branch) == 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) == 0  and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) == 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(company=company) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(company=company) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(company=company) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(company=company) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry) )

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(company=company) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(company=company) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(company=company) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(company=company) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(company=company) & Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(company=company) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) &  Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(company=company) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(company=company) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) &  Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(company=company) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))        

        elif len(branch) == 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(catogory=category)&  Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))        

        elif len(branch) != 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) == 0:
            if len(expiry_category) == 1:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company) & Q(catogory=category)  & Q(passport_expiry__lte=month_expiry_date))           
            elif len(expiry_category) == 2:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company) & Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 3:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company) & Q(catogory=category)  & Q(visa_expiry__lte=month_expiry_date))   
            elif len(expiry_category) == 4:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company) & Q(catogory=category)  & Q(insurence_expiry__lte=month_expiry_date))  

        elif len(branch) != 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) == 0  and len(days_of_expiry) != 0:
            if   len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=one_week_expiry) | Q(visa_expiry__lte=one_week_expiry)| Q(emirates_expiry__lte=one_week_expiry)| Q(insurence_expiry__lte=one_week_expiry))
            elif len(days_of_expiry) == 2:
                employees=Employee.objects.filter(Q(branch=branch) &  Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=next_month_expiry) | Q(visa_expiry__lte=next_month_expiry)| Q(emirates_expiry__lte=next_month_expiry)| Q(insurence_expiry__lte=next_month_expiry))
            elif len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry)| Q(emirates_expiry__lte=three_month_expiry)| Q(insurence_expiry__lte=three_month_expiry))
            elif len(days_of_expiry) == 4:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company) & Q(catogory=category) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry)| Q(emirates_expiry__lte=one_year_expiry)| Q(insurence_expiry__lte=one_year_expiry))

        elif len(branch) != 0 and len(company) != 0 and len(category) == 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry))  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company)  &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(Q(branch=branch) & Q(company=company)  &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company) &  Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) & Q(company=company)  & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))        


        elif len(branch) != 0 and len(company) == 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry) )

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category)& Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(Q(branch=branch) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(Q(branch=branch) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(branch=branch) & Q(catogory=category) &  Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(branch=branch) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))       

        elif len(branch) == 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry) )

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category)& Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=next_month_expiry) )
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(Q(company=company) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) | Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(Q(company=company) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry) | Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) & Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter( Q(company=company) & Q(catogory=category) &  Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter( Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))        


        elif len(branch) != 0 and len(company) != 0 and len(category) != 0 and len(expiry_category) != 0  and len(days_of_expiry) != 0:
            if  len(expiry_category) == 1 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(   Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_week_expiry) )  
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=next_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=three_month_expiry) )
            elif  len(expiry_category) == 1 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(passport_expiry__lte=month_expiry_date) & Q(passport_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 2 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category)& Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) &  Q(emirates_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 2 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(emirates_expiry__lte=month_expiry_date) & Q(emirates_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 3 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(visa_expiry__lte=month_expiry_date) & Q(visa_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(company=company) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 3 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) & Q(company=company) &  Q(catogory=category) &  Q(visa_expiry__lte=month_expiry_date) &  Q(visa_expiry__lte=one_year_expiry))

            elif  len(expiry_category) == 4 and len(days_of_expiry) == 1:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_week_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 2:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=next_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 3:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) & Q(catogory=category) &  Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=three_month_expiry))
            elif  len(expiry_category) == 4 and len(days_of_expiry) == 4:
                employees=Employee.objects.filter(  Q(branch=branch) &  Q(company=company) &  Q(catogory=category) & Q(insurence_expiry__lte=month_expiry_date) &  Q(insurence_expiry__lte=one_year_expiry))        

        dict_expiry ={
            'employee':employees,
            'catogary':Category.objects.all(),
            'company':Company.objects.all(),
            'branch':Branch.objects.all(),
            "red":ten_day_expiry
        }
        return render(request,'expiry.html',dict_expiry)
    else:
        month_expiry_date = date.today().replace(day=1) + timedelta(days=29)
        ten_day_expiry=date.today() + timedelta(days=10)
        employee=Employee.objects.filter( Q(passport_expiry__lte=month_expiry_date) | Q(visa_expiry__lte=month_expiry_date)| Q(emirates_expiry__lte=month_expiry_date)| Q(insurence_expiry__lte=month_expiry_date))
        # temp=Employee.objects.values_list('passport_expiry',flat=True)
        # print(temp)
        dict_expiry ={
            'employee':employee,  
            'catogary':Category.objects.all(),
            'company':Company.objects.all(),
            'branch':Branch.objects.all(),
            "red":ten_day_expiry
        }
        return render(request,'expiry.html',dict_expiry)

# catogory****************************************************************

@login_required(login_url='/')
def catogory(request):
    dict_catogory ={
        'catogary':Category.objects.all()
    }
    return render(request,'catogory.html',dict_catogory)

@login_required(login_url='/')
def get_catogory(request):
    new_catogory=request.POST['catogary']
    cat=Category()
    cat.category=new_catogory
    cat.save()
    return  redirect(catogory)

def delete_category(request,id):
    category_instance=Category.objects.get(id=id)
    category_instance.delete()
    return redirect(catogory)

# this not working 

def update_category(request):
    name=request.GET['name']
    print(name)
    return redirect(catogory)



# this not working 

# end catogory****************************************************************


# company****************************************************************

@login_required(login_url='/')
def company(request):
    dict_company ={
        'company':Company.objects.all()
    }
    return render(request,'company.html',dict_company)

@login_required(login_url='/')
def get_company(request):
    new_company=request.POST['company']
    cam=Company()
    cam.company=new_company
    cam.save()
    return  redirect(company)


# this not working 
def edit_company(request,id):
    request.session['edit_company_id']=id  
    return HttpResponse("<script>alert('hay')</script>")

def update_company(request):
    if request.method == 'POST':
        try:
            company_name=request.POST['company']
            company_id=request.session['edit_company_id']
            print(company_id)
            company_instance=Company.objects.get(id=company_id)
            company_instance.company=company_name
            company_instance.save()
            return redirect(company)
        except :
            return HttpResponse("<script>alert('Company Not Found');window.history.back()</script>")
# this not working 


def delete_company(request,id):
    company_instance=Company.objects.get(id=id)
    company_instance.delete()
    return redirect(company)



# end company****************************************************************



# branch***********************************************************************

@login_required(login_url='/')
def branch(request):
    dict_branch={
        'branch':Branch.objects.all()
    }
    return render(request,'branches.html',dict_branch)

@login_required(login_url='/')
def get_branch(request):
    new_branch=request.POST['branch']
    bra=Branch()
    bra.branch=new_branch
    bra.save()
    return  redirect(branch)

def delete_branch(request,id):
    branch_instance=Branch.objects.get(id=id)
    branch_instance.delete()
    return redirect(branch)

# end  branch***********************************************************************

def send_mail_user(request):
    try:
        days_in_month = lambda dt: monthrange(dt.year, dt.month)[1]
        today = date.today()
        next_month_expiry_date = today.replace(day=30) + timedelta(days_in_month(today))
        month_expiry_date = today.replace(day=1) + timedelta(days_in_month(today))

        employee_passport_expiry=Employee.objects.values_list('passport_expiry','notification_email').filter( (Q(passport_expiry__lte=next_month_expiry_date) & Q(passport_expiry__gte=month_expiry_date)) )

        for i in employee_passport_expiry:
            subject = 'Code Band'
            message = 'Sending Email through Gmail {}'.format(i[0])
            send_mail(subject, 
                    message, settings.EMAIL_HOST_USER, [i[1]] , fail_silently=False)
        return 
    except:
        return HttpResponse("<script>alert('mail send Failed');window.history.back()</script>")


