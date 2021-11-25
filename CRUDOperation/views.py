from django import forms
from django.shortcuts import render
from django.db import connection
from CRUDOperation.models import CusModel, EmpModel        #employee model as created in models.py
from django.contrib import messages
from CRUDOperation.forms import cusForms, empForms

def showhome(request):
    return render(request,'home.html')



def showcus(request):        #this fuction return all the record from the customer table 
    showall = CusModel.objects.all()
    return render(request,'Index_cus.html',{"data":showall})

def showemp(request):        #this fuction return all the record from the emplyee table 
    showall = EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})


def Insertcus(request):
    if request.method=="POST":
        if request.POST.get('customer_id') and request.POST.get('subscription_status') and request.POST.get('customer_name') and request.POST.get('contact_number') and request.POST.get('verification_id') and request.POST.get('user_id') and request.POST.get('pass_key') and request.POST.get('user_email') and request.POST.get('city_name'):
            saverecord=CusModel()
            saverecord.customer_id=request.POST.get('customer_id')
            saverecord.subscription_status=request.POST.get('subscription_status')
            saverecord.customer_name=request.POST.get('customer_name')
            saverecord.contact_number=request.POST.get('contact_number')
            saverecord.verification_id=request.POST.get('verification_id')
            saverecord.user_id=request.POST.get('user_id')
            saverecord.pass_key=request.POST.get('pass_key')
            saverecord.user_email=request.POST.get('user_email')
            saverecord.city_name=request.POST.get('city_name')
            allval = CusModel.objects.all()
            for i in allval:
                #print(i.customer_id)
                #print(i.customer_id==request.POST.get('customer_id'))
                if int(i.customer_id)==int(request.POST.get('customer_id')):
                    messages.warning(request,'Customer alredy exists....!');
                    return render(request,'insert_cus.html')

            saverecord.save()
            messages.success(request,'Customer ID '+saverecord.customer_id+' added successfully...! ')
            return render(request,'insert_cus.html')
    else:
        return render(request,'insert_cus.html')


def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('employee_id') and request.POST.get('employee_name') and request.POST.get('contact_number') and request.POST.get('verification_id') and request.POST.get('branch_id') and request.POST.get('city_name'):
            saverecord=EmpModel()
            saverecord.employee_id=request.POST.get('employee_id')
            saverecord.employee_name=request.POST.get('employee_name')
            saverecord.contact_number=request.POST.get('contact_number')
            saverecord.verification_id=request.POST.get('verification_id')
            saverecord.branch_id=request.POST.get('branch_id')
            saverecord.city_name=request.POST.get('city_name')
            allval = EmpModel.objects.all()
            for i in allval:
                #print(i.debitcard_id)
                #print(i.debitcard_id==request.POST.get('debitcard_id'))
                if int(i.employee_id)==int(request.POST.get('employee_id')):
                    messages.warning(request,'employee alredy exists....!');
                    return render(request,'insert.html')

            saverecord.save()
            messages.success(request,'Employee ID '+saverecord.employee_id+' added successfully...! ')
            return render(request,'insert.html')
    else:
        return render(request,'insert.html')

def editemp(request,employee_id):
    editempobj=EmpModel.objects.get(employee_id=employee_id)
    return render(request,'edit.html',{"EmpModel":editempobj})

def editcus(request,customer_id):
    editcusobj=CusModel.objects.get(customer_id=customer_id)
    return render(request,'edit_cus.html',{"CusModel":editcusobj})

def updateemp(request,employee_id):
    # print(employee_id)
    Updateemp=EmpModel.objects.get(employee_id=employee_id)
    #print(Updateemployee.balance)
    form=empForms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully...')
        return render(request,'edit.html',{"EmpModel":Updateemp})


def updatecus(request,customer_id):
    # print(employee_id)
    Updatecus=CusModel.objects.get(customer_id=customer_id)
    #print(Updateemployee.balance)
    form=cusForms(request.POST,instance=Updatecus)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully...')
        return render(request,'edit_cus.html',{"CusModel":Updatecus})

def delemp(request,employee_id):
    delemployee=EmpModel.objects.get(employee_id=employee_id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,"index.html",{"data":showdata})

def delcus(request,customer_id):
    delcustomer=CusModel.objects.get(customer_id=customer_id)
    delcustomer.delete()
    showdata=CusModel.objects.all()
    return render(request,"index_cus.html",{"data":showdata})


def runQuery(request):
    raw_query = " select * from employee where city_name = 'Mumbai'; "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    #print(alldata)
    return render(request,'runQuery.html',{'data':alldata})

def runQuery2(request):  ## 
    raw_query = " select * from customer where subscription_status = 'false' and city_name = 'Mumbai'; "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    #print(alldata)
    return render(request,'runQuery2.html',{'data':alldata})