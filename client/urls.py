from django.urls import path

from .views import HomePageView, DayPassPageView, ForgotPasswordPageView
from .views import SignupPageView, SigninPageView, SignoutPageView, ProfilePageView
from .views import RegisterPageView, SelectMembershipPageView, SelectProductsPageView
from .views import RegisterPaymentPageView, RegisterParentPageView, RegisterMerchantPageView
from .views import RegisterPartyPageView, RegisterVolunteerPageView

app_name = 'client'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path ('day_pass', DayPassPageView.as_view(), name='day-pass'),
    path('forgot', ForgotPasswordPageView.as_view(), name='forgot'),
    path('signup', SignupPageView.as_view(), name='signup'),
    path('signin', SigninPageView.as_view(), name='signin'),
    path('signout', SignoutPageView.as_view(), name='signout'),
    path('profile', ProfilePageView.as_view(), name='profile'),
    path('register', RegisterPageView.as_view(), name='register'),
    path('register/membership', SelectMembershipPageView.as_view(), name='register-membership'),
    path('register/products', SelectProductsPageView.as_view(), name='register-products'),
    path('register/parent', RegisterParentPageView.as_view(), name='register-parent'),
    path('register/merchant', RegisterMerchantPageView.as_view(), name='register-merchant'),
    path('register/party', RegisterPartyPageView.as_view(), name='register-party'),
    path('register/volunteer', RegisterVolunteerPageView.as_view(), name='register-volunteer'),
    path('register/payment', RegisterPaymentPageView.as_view(), name='register-payment'),
]
