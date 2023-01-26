from django.contrib import admin
from .models import User
from .models import Accounts
from .models import InsuranceProducts
from .models import Recives

# Register your models here.
admin.site.register(User)
admin.site.register(Accounts)
admin.site.register(InsuranceProducts)
admin.site.register(Recives)
