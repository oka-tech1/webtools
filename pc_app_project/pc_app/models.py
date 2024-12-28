from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus = models.FloatField(default=0.0)
    mesg = models.CharField(default="thanks for being here.", max_length=5000)

    def __str__(self):
        return f'{self.user.username}{self.bonus}{self.mesg}'
    

class pc_store(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images', null=True)
    img1 = models.ImageField(upload_to='images', null=True)
    Description = models.TextField(max_length=5000)
    Price = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.name}'    


class contact(models.Model):
    message = models.TextField(max_length=5000)
    email = models.EmailField(null=True, max_length=500)
    def __str__(self):
        return f'{self.message}{self.email}'
        
class wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Enter_name = models.CharField(max_length=500, default='you dont have history yet')
    Deposit_amount = models.CharField(max_length=500, default='No payment fund yet')
    Enter_email = models.EmailField(default='Empty')
    Upload_transaction_receipt_screenshot = models.ImageField(default='Status', upload_to='images')
    status = models.CharField(max_length=500, default='Status')
    time = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.user}{self.Enter_name}'
    
    
        
