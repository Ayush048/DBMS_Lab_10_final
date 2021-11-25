from django.db import models

class EmpModel(models.Model):
    employee_id = models.BigIntegerField(unique = True, primary_key = True)
    employee_name = models.CharField( max_length = 40) 
    verification_id = models.BigIntegerField()
    contact_number = models.BigIntegerField()
    branch_id = models.IntegerField()
    city_name = models.CharField( max_length= 30 )    

    class Meta: 
        db_table= "employee"

class CusModel(models.Model):
    customer_id = models.BigIntegerField(unique = True, primary_key = True)
    subscription_status = models.BooleanField()
    customer_name = models.CharField( max_length= 30 ) 
    contact_number = models.BigIntegerField()
    verification_id = models.BigIntegerField()
    user_id = models.BigIntegerField() 
    pass_key = models.CharField( max_length= 15 ) 
    user_email =models.CharField( max_length= 50 ) 
    city_name = models.CharField( max_length= 30 ) 
    
    class Meta: 
        db_table= "customer"