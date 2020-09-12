from django.urls import path, include
from reports import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companys', views.CompanysViewSet, basename='companys')
router.register('banks', views.BanksViewSet, basename='banks')
router.register('accounts', views.AccountsViewSet, basename='accounts')
router.register('currencys', views.CurrencyViewSet, basename='currencys')

urlpatterns = [
    path('', include(router.urls)),
    # path('companys/', views.CompanysListView.as_view())
    path('api/', include('rest_framework.urls'))
]
