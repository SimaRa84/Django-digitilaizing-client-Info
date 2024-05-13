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


class AccountInfo(models.Model):

    TYPE_INVEST = 'I'
    TYPE_REG = 'R'
    TYPE_TFSA = 'T'
    TYPE_ACCOUNT = [
        ("",'select one'),
        (TYPE_INVEST, "INVESTMENT"),
        (TYPE_REG, "REGISTERED"),
        (TYPE_TFSA, "TFSA"),
    ]
    type_account= models.CharField( choices=TYPE_ACCOUNT, default=TYPE_ACCOUNT,max_length=50)  
    account_number = models.CharField(max_length=255)

class FinancialInfo(models.Model):
    FIRSTAMOUNT ="A"
    SECONDAMOUNT ="B"
    THIRDAMOUNT ="C"
    FORTHAMOUNT ="D"
    FIFTHAMOUNT ="E"

    ACCOUNTAMOUNT = [
        ("",'select one'),
        (FIRSTAMOUNT, "$0-$24,99"),
        (SECONDAMOUNT, "$25,000-$49,999"),
        (THIRDAMOUNT, "$50,000-$99,999"),
        (FORTHAMOUNT, "$100,000-$149,999"),
        (FIFTHAMOUNT, "$150,000+"),
    ]
    gross= models.CharField(max_length=255)    
    liquid_assets= models.CharField(max_length=255 )    
    fixed_assets= models.CharField( max_length=255)   
    net_worth= models.CharField(max_length=255)   


    LEVELA='L',
    LEVELB='LM'
    LEVELC='M'
    LEVELD='MH'
    LEVELE='H'

    LEVELKNOWLEDGE = [
        ("",'select one'),
        (LEVELA, "Low"),
        (LEVELB, "Low-Moderate"),
        (LEVELC, "Moderate"),
        (LEVELD, "Moderate-High"),
        (LEVELE, "High"),
    ]
    applicant_invest_knowledge= models.CharField( max_length=50 )    
    coApplicant_investment_knowledge= models.CharField(max_length=50 )   
    risk_tolerance= models.CharField(max_length=50)  


    TIMEA='A'
    TIMEB='B'
    TIMEC='C'
    TIMED='D'
    TIMEE='E'
    TIMEHORIZON = [
        ("",'select one'),
        (TIMEA, "Less than 1 year"),
        (TIMEB, "1 year to less than 3 years"),
        (TIMEC, "3 years to less than 5 years"),
        (TIMED, "5 years to less than 10 years"),
        (TIMEE, "10 years or more")
    ]
    time_horizon= models.CharField(max_length=255)  
    liquidity = models.DecimalField(max_digits=10, decimal_places=2)
    safety = models.DecimalField( max_digits=10, decimal_places=2)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    long_term_growth = models.DecimalField(max_digits=10, decimal_places=2 )
    short_term_growth = models.DecimalField(max_digits=10, decimal_places=2 )
    speculation = models.DecimalField(max_digits=10, decimal_places=2)
    inflation_hedging = models.DecimalField( max_digits=10, decimal_places=2)
     

    