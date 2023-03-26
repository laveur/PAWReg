import datetime

from .event import Event
from .membership import Membership
from .product_type_attibute import ProductTypeAttribute
from .product_type import ProductType
from .product import Product
from .profile import Profile
from .user import User
from .registration import Registration
from .registration_products import RegistrationProduct


def get_current_event():
    return Event.objects.filter(event_end_date__gte=datetime.date.today()).order_by('event_end_date').first()
