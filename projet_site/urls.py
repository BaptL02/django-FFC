from django.contrib import admin
from projet_site import settings
from django.conf.urls.static import static

from django.urls import path

#import FRANCAIS
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

#import ANGLAIS
from events.views import en_index
from events.views import en_contact
from events.views import en_docs
from events.views import en_livrees
from events.views import en_livrees_XP
from events.views import en_vmr_list
from events.views import en_voltige
from events.views import en_events
from events.views import en_AIRBUS
from events.views import en_BOEING
from events.views import en_livrees_MSFS
from events.views import en_LEGER
from events.views import en_formation_list

urlpatterns = [

    #Lien FRANCAIS
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
    path('sondage/answered', vote, name='vote'),

    #Lien ANGLAIS
    path('en/', en_index, name="en_index"),
    path('en/contact', en_contact, name="en_contact"),
    path('en/documentation', en_docs, name="en_doc"),
    path('en/livrees', en_livrees, name="en_livrees"),
    path('en/livrees_XP', en_livrees_XP, name="en_livrees_XP"),
    path('en/vmr_list', en_vmr_list, name="en_vmr_list"),
    path('en/voltige', en_voltige, name="en_voltige"),
    path('en/events', en_events, name="en_events"),
    path('en/documentation/formation/', en_formation_list, name="en_formation_list"),
    path('en/livrees/livrees_MSFS/', en_livrees_MSFS, name="en_livrees_MSFS"),
    path('en/livrees/livrees_MSFS/airbus/', en_AIRBUS, name="en_AIRBUS"),
    path('en/livrees/livrees_MSFS/boeing/', en_BOEING, name="en_BOEING"),
    path('en/livrees/livrees_MSFS/leger/', en_LEGER, name="en_LEGER"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
