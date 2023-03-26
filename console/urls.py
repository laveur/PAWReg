from django.urls import path

from .views import ConsoleIndexPageView, EventsListPageView, EventsCreatePageView, EventsDetailsPageView, MembershipsCreatePageView, MembershipsDetailPageView, ProductCreatePageView, ProductDetailPageView

app_name = 'console'
urlpatterns = [
    path('', ConsoleIndexPageView.as_view(), name='index'),
    path('events', EventsListPageView.as_view(), name='events-list'),
    path('events/new', EventsCreatePageView.as_view(), name='events-create'),
    path('events/<int:event_id>', EventsDetailsPageView.as_view(), name='events-detail'),
    path('events/<int:event_id>/memberships', MembershipsCreatePageView.as_view(), name='memberships-create'),
    path('events/<int:event_id>/memberships/<int:membership_id>', MembershipsDetailPageView.as_view(), name='memberships-detail'),
    path('events/<int:event_id>/products', ProductCreatePageView.as_view(), name='products-create'),
    path('events/<int:event_id>/products/<int:product_id>', ProductDetailPageView.as_view(), name='products-detail'),
]
