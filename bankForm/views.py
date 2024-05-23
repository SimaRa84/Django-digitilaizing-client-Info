from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  AccountInfo
from .forms import CustomerForm, AccountInfoFormSet,AccountInfoForm,CustomerDetailsForm
from django.db import transaction
from django.forms import modelformset_factory


def create_bank_form(request):
    AccountInfoFormSet = modelformset_factory(AccountInfo, form=AccountInfoForm, extra=1, can_delete=True)
    print(request.POST)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, prefix='customer')
        account_info_formset = AccountInfoFormSet(request.POST, request.FILES, prefix='accounts')

        if customer_form.is_valid() and account_info_formset.is_valid():
            print(account_info_formset.cleaned_data)
            customer = customer_form.save()
            accounts = account_info_formset.save(commit=False)
            for account in accounts:
                account.customer = customer
                account.save()
            account_info_formset.save_m2m()
            updated_request = request.POST.copy()
            updated_request.update({'details-customer': customer})             
           
            customer_details_form = CustomerDetailsForm(updated_request, prefix='details')
            if customer_details_form.is_valid():  
                cd= customer_details_form.cleaned_data
                customer_details_form.save()               
            else:
                print(customer_details_form.errors)
            return HttpResponse('success_url')
        else:
            print(customer_form.errors)
            print(customer_details_form.errors)
            print(account_info_formset.errors)
            return HttpResponse('Failed') 
    else:
        customer_form = CustomerForm(prefix='customer')
        account_info_formset = AccountInfoFormSet(queryset=AccountInfo.objects.none(), prefix='accounts')
        customer_details_form = CustomerDetailsForm(prefix='details')



    return render(request, 'create.html', {
        'customer': customer_form,
        'financialInfo':customer_details_form,
        'account_info_formset': account_info_formset
    })