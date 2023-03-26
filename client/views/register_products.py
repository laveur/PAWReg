from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from shared.models import get_current_event
from shared.models import Event, User, Membership, Registration, RegistrationProduct, Product, ProductTypeAttribute


@method_decorator(login_required, name='dispatch')
class SelectProductsPageView(TemplateView):
    template_name = 'register_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = get_current_event()
        registration = Registration.objects.get(user=self.request.user, event=event)
        membership = registration.membership
        included_products = membership.included_products.all()
        additional_products = Product.objects.exclude(id__in=[ip.id for ip in included_products])
        product_type_attributes = ProductTypeAttribute.objects.all()
        context['registration'] = registration
        context['membership'] = membership
        context['included_products'] = included_products
        context['additional_products'] = additional_products
        context['product_type_attributes'] = product_type_attributes

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        for included_product in context['included_products']:
            registration_product = RegistrationProduct()
            registration_product.membership = context['membership']
            registration_product.product = included_product

            attr_key = 'included_product_' + str(included_product.id) + '_attr'
            if request.POST.get(attr_key, None) != None:
                registration_product.attribute = request.POST[attr_key]

            registration_product.value = 0.00
            registration_product.save()


        for product in context['additional_products']:
            product_key = 'product_' + str(product.id)
            product_attr_key = 'product_' + str(product.id) + '_attr'
            product_value_key = 'product_' + str(product.id) + '_value'

            if request.POST.get(product_key, None) != None:
                registration_product = RegistrationProduct()
                registration_product.membership = context['membership']
                registration_product.product = product

                if request.POST.get(product_attr_key, None) != None:
                    registration_product.attribute = request.POST[product_attr_key]
                    registration_product.value = product.tier1_pricing
                
                if request.POST.get(product_value_key, None) != None:
                    registration_product.value = request.POST[product_value_key]
                
                registration_product.save()

        if context['registration'].is_parent:
            return HttpResponseRedirect(reverse('client:register-parent'))
        elif context['registration'].is_merchant:
            return HttpResponseRedirect(reverse('client:register-merchant'))
        elif context['registration'].is_party_host:
            return HttpResponseRedirect(reverse('client:register-party'))
        elif context['registration'].is_volunteer:
            return HttpResponseRedirect(reverse('client:register-volunteer'))
        else:
            return HttpResponseRedirect(reverse('client:register-payment'))
        endif
