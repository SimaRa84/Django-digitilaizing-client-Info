from django import forms
from django.forms import modelformset_factory

from .models import Customer, AccountInfo,CustomerDetails

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["gender", "first_name", "last_name","initials","sin_number"]


class AccountInfoForm(forms.ModelForm):    
    
    class Meta:
        TYPE_INVEST = 'I'
        TYPE_REG = 'R'
        TYPE_TFSA = 'T'

        TYPE_ACCOUNT = [
            ("",'select one'),
            (TYPE_INVEST, "INVESTMENT"),
            (TYPE_REG, "REGISTERED"),
            (TYPE_TFSA, "TFSA")
        ]

        model = AccountInfo
        fields = ["type_account", "account_number"]
        widgets = {'type_account':forms.Select(choices=TYPE_ACCOUNT)}


AccountInfoFormSet = modelformset_factory(
    AccountInfo,
    form=AccountInfoForm,
    extra=1,  # Number of extra forms to display
)

class CustomerDetailsForm(forms.ModelForm):
    
    # def __init__(self,*args,**kwargs):
    #     self.customer_id = kwargs.pop('customer_id')
    #     super(CustomerDetailsForm,self).__init__(*args,**kwargs)
    #     self.fields['customer'].widget = forms.TextInput(attrs={'size':self.customer_id})

    # customer = forms.CharField()
    class Meta:
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
            (FIFTHAMOUNT, "$150,000+")
        ]
        LEVELA='L'
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
        
       
        model = CustomerDetails
        fields = '__all__'
        widgets = {
            'gross':forms.Select(choices=ACCOUNTAMOUNT),
            'liquid_assets':forms.Select(choices=ACCOUNTAMOUNT),
            'fixed_assets':forms.Select(choices=ACCOUNTAMOUNT),
            'net_worth':forms.Select(choices=ACCOUNTAMOUNT),
            'applicant_invest_knowledge':forms.Select(choices=LEVELKNOWLEDGE),
            'coApplicant_investment_knowledge':forms.Select(choices=LEVELKNOWLEDGE),
            'risk_tolerance':forms.Select(choices=LEVELKNOWLEDGE),
            'time_horizon':forms.Select(choices=TIMEHORIZON)              
            }
        labels = {
        # 'type_account': '(Check one)',
        # 'gender': 'Gender)',
        'gross': 'a) Gross annual income from all sources',
        'net_worth': 'd) Estimated net worth :(d= b+c)',
        'liquid_assets': 'b) Estimated net liquid assets: ',
        'fixed_assets': 'c) Estimated net fixed assets: ',
        'applicant_invest_knowledge':"e) Applicant/Annutant's investment knowledge: ",
        'coApplicant_investment_knowledge':"f) Co-Applicant's investment knowledge: ",
        'risk_tolerance':'h) Risk Tolerance: ',
        'time_horizon' : 'g) timeHorizon: ',
        'liquidity':'Liquidity',
        'safety':'Safety',
        'income':'Income',
        'long_term_growth':'Long term Growth',
        'short_term_growth':'Short term Growth',
        'speculation':'Speculative',
        'inflation_hedging':'Inflation Hedging'
    }
       
