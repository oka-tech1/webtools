from django.urls import path
from . import views
from .views import signup, contacts, mywallet, wallet_suc, history, buy, insuf, pc_stores, success


urlpatterns =[
    path('', views.home, name='home'),
    path('signup/', signup.as_view(), name='signup'),
    path('pc_stores', pc_stores.as_view(), name='pc_stores'),
    path('pc_details/<int:id>', views.pc_details, name='details'),
    path('contacts', views.contacts, name='contacts'),
    path('success', success.as_view(), name='success'),
    path('wallet_suc', views.wallet_suc, name='wallet_suc'),
    path('mywallet', mywallet.as_view(), name='mywallet'),
    path('history', history.as_view(), name='history'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('created', views.created, name='created'),
    path('insuf', views.insuf, name='insuf'),
    path('forum', views.forum, name='forum'),
    path('hardware', views.hardware, name='hardware'),
        
]

 

