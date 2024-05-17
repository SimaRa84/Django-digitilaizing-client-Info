from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Customer,AccountInfo,CustomerDetails

def create_bank_form(request):
    if request.method == 'POST':

        customer = Customer(request.POST,prefix='some_prefix')
        accountInfo = AccountInfo(request.POST,prefix='some_prefix')
        customer_details = CustomerDetails(request.POST,prefix='some_prefix')

        if customer.is_valid():

            cd= customer.cleaned_data   
            return HttpResponse('Validate')
            # return redirect('success_page')

        else:
            return HttpResponse('Failed')
            
    else:
        customer = Customer(prefix='some_prefix')
        accountInfo = AccountInfo(prefix='some_prefix')
        customer_details = CustomerDetails(prefix='some_prefix')
        
        context=( customer, accountInfo ,customer_details  )
        return render (request, 'create.html',{'context':context})