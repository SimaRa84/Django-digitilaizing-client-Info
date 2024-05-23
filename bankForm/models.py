from django.db import models

class Customer(models.Model):
 
    GENDER = (
        ("",'select one'),
        ("1","Mr"),
        ("2","Miss"),
        ("3","Mrs"),
        ("4","Miss"),
        ("5","Dr"),
        ("6","Prof"),
    )    
    gender= models.CharField( choices=GENDER, max_length=50)  
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    sin_number = models.CharField(max_length=255)  
    initials = models.CharField(max_length=255, null=True)  


def __str__(self):
        return f"{self.name} {self.last_name}"

class AccountInfo(models.Model):
   
    customer = models.ForeignKey(Customer, related_name='accounts', on_delete=models.CASCADE)
    type_account= models.CharField( max_length=50)  
    account_number = models.CharField(max_length=255)

def __str__(self):
        return self.account_number

class CustomerDetails(models.Model):

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)   
    gross= models.CharField(max_length=255)    
    liquid_assets= models.CharField(max_length=255 )    
    fixed_assets= models.CharField( max_length=255)   
    net_worth= models.CharField(max_length=255)
    applicant_invest_knowledge= models.CharField( max_length=50 )    
    coApplicant_investment_knowledge= models.CharField(max_length=50 )   
    risk_tolerance= models.CharField(max_length=50)  
    time_horizon= models.CharField(max_length=255)  
    liquidity = models.CharField(max_length=10)
    safety = models.CharField( max_length=10)
    income = models.CharField(max_length=10)
    long_term_growth = models.CharField(max_length=10 )
    short_term_growth = models.CharField(max_length=10 )
    speculation = models.CharField(max_length=10)
    inflation_hedging = models.CharField( max_length=10)
     

    