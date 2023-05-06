from django.contrib import admin

# Register your models here.
from events.models import Event
from events.models import Annonce
from events.models import Livree
from events.models import doc
from events.models import formation
from events.models import VMR

admin.site.site_header = 'French Flying Club administration'

admin.site.register(Event)
admin.site.register(Annonce)
admin.site.register(Livree)
admin.site.register(doc)
admin.site.register(formation)
admin.site.register(VMR)