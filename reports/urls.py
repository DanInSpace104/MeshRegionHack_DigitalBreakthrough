from django.urls import path, include
from reports import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companys', views.CompanysViewSet, basename='companys')
router.register('banks', views.BanksViewSet, basename='banks')
router.register('accounts', views.AccountsViewSet, basename='accounts')
router.register('superaccounts', views.AccountsViewSet, basename='accounts')
router.register('currencys', views.CurrencyViewSet, basename='currencys')
router.register('bankbiks', views.BankBiksViewSet, basename='bankbiks')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls')),
    path('change_accs/', views.change_accounts),
    path('accs_by_company/<company_id>', views.AccountsByCompList.as_view(), name='accs_by_comp'),
    path('reports/', views.ReportsListView.as_view(), name='reports'),
    path('accts/', views.accts),
    path('createacct/', views.createacct),
    path('selectorg/', views.selectorg),
    path('adminpanel/', views.adminpanel),
]
