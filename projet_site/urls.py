from django.contrib import admin
from projet_site import settings
from django.conf.urls.static import static

from django.urls import path
from events.views import events
from events.views import index
from events.views import docs
from events.views import contact
from events.views import livrees_MSFS
from events.views import livrees
from events.views import livrees_XP
from events.views import voltige
from events.views import formation_list
from events.views import privacy_policy
from events.views import vmr_list
from events.views import sondage
from events.views import vote
from events.views import AIRBUS
from events.views import BOEING
from events.views import LEGER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('acceuil/', index, name="index"),
    path('events/', events, name="events"),
    path('documentation/', docs, name="doc"),
    path('documentation/formation/', formation_list, name="formation_list"),
    path('contact/', contact, name="contact"),
    path('livrees/livrees_MSFS/', livrees_MSFS, name="livrees_MSFS"),
    path('livrees/livrees_MSFS/airbus/', AIRBUS, name="AIRBUS"),
    path('livrees/livrees_MSFS/boeing/', BOEING, name="BOEING"),
    path('livrees/livrees_MSFS/leger/', LEGER, name="LEGER"),
    path('livrees/', livrees, name="livrees"),
    path('voltige/', voltige, name="voltige"),
    path('livrees_xp/', livrees_XP, name="livrees_XP"),
    path('contact/privacy_policy/', privacy_policy, name="privacy_policy"),
    path('livrees/vmr/', vmr_list, name="vmr_list" ),
    path('sondage/', sondage, name='sondage'),
    path('sondage/answered', vote, name='vote')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
