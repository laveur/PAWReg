from django.urls import path

from .views import MerchantIndexPageView, TableListPageView, TableCreatePageView
from .views import TableDetailPageView

app_name = 'merchant'
urlpatterns = [
    path('', MerchantIndexPageView.as_view(), name='index'),
    path('table', TableListPageView.as_view(), name='table-list'),
    path('table/new', TableCreatePageView.as_view(), name='table-create'),
    path('table/<key>', TableDetailPageView.as_view(), name='table-detail'),
]