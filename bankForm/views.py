from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Customer,AccountInfo,FinancialInfo

def create_bank_form(request):
    if request.method == 'POST':

        customer = Customer(request.POST,prefix='some_prefix')
        accountInfo = AccountInfo(request.POST,prefix='some_prefix')
        financialInfo = FinancialInfo(request.POST,prefix='some_prefix')

        if customer.is_valid():

            cd= customer.cleaned_data   
            return HttpResponse('Validate')
            # return redirect('success_page')

        else:
            return HttpResponse('Failed')
            
    else:
        customer = Customer(prefix='some_prefix')
        accountInfo = AccountInfo(prefix='some_prefix')
        financialInfo = FinancialInfo(prefix='some_prefix')
        
        context=( customer, accountInfo ,financialInfo  )
        return render (request, 'create.html',{'context':context})