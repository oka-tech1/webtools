from .models import contact, wallet
from django.forms import models

class userform(models.ModelForm):


    class Meta:
        model = contact
        fields = '__all__'
    
    
class walletform(models.ModelForm):

    class Meta:
        model = wallet
        fields = ['Enter_name', 'Deposit_amount', 'Enter_email', 'Upload_transaction_receipt_screenshot',]
