from events.models import ALERT
from events.models import VMR
from events.models import formation
from events.models import doc
from events.models import Livree
from events.models import Annonce
from events.models import Event
from django.contrib import admin

admin.site.site_header = 'French Flying Club administration'

# Register your models here.

admin.site.register(Event)
admin.site.register(Annonce)
admin.site.register(doc)
admin.site.register(formation)
admin.site.register(VMR)
admin.site.register(ALERT)
admin.site.register(Livree)
