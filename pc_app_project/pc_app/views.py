from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import pc_store, contact, wallet
from .forms import userform, walletform
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


	
def home(request):
    return render(request, 'home.html')


class signup(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("created")
    

@method_decorator(login_required, name='dispatch')
class pc_stores(ListView):
    model = pc_store
    template_name = 'pc_store.html'


@login_required()
def pc_details(request, id):
    details = pc_store.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'details':details,
    }   
    
    return HttpResponse(template.render(context, request))

@login_required()
def buy(request, id):
    pc_price = pc_store.objects.get(id=id)
    profile = request.user.profile
    if profile.bonus >= pc_price.Price:
       profile.bonus -= pc_price.Price
       profile.save()
       return render(request, 'success.html', {'pc_price': pc_price})
    else:
        return render(request, 'insuf.html')



def contacts(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')

    else:    
        form = userform()
        return render(request, 'contact.html', {'form':form})
         
class success(ListView):
    model = pc_store
    template_name = 'success.html'

'''
            #To send message to our preferred SMTP Provider(Gmail)
            send_mail(
                    f'New message submitted via the contact form by {contact.email}', # This will serve as the subject of the message upon recieving
                    contact.message, # The body of the message
                    contact.email, # From the email that sent the message
                    [settings.EMAIL_HOST_USER], # To the Email that will be recieving. (set at the settings.py file(Your email))
            )

def mywallet(request):
    if request.method == 'POST':
        form = walletform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')

    else:    
        form = walletform()
        return render(request, 'wallet.html', {'form':form})
    

'''            

@method_decorator(login_required, name='dispatch')
class mywallet(CreateView):
    form_class = walletform
    template_name = 'wallet.html'
    success_url = reverse_lazy('wallet_suc')

@login_required()
def wallet_suc(request):
    return render(request, 'wallet_suc.html')


@method_decorator(login_required, name='dispatch')
class history(ListView):
    model = wallet
    template_name = 'history.html'



def created(request):
    template = loader.get_template('created.html')
    return HttpResponse(template.render())

@login_required()
def insuf(request):
    return render(request, 'insuf.html')


@login_required()
def forum(request):
    return render(request, 'forum.html')


@login_required()
def hardware(request):
    return render(request, 'hardware.html')
    
    
def search(request):
    pass
