from django.views.generic.list import ListView
from django.utils import timezone
from .models import Customer

class CustomerListView(ListView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
