from django.shortcuts import render
from django.db.models import Q
from datetime import datetime

from events.models import Event
from events.models import Annonce
from events.models import Livree
from events.models import doc
from events.models import formation
from events.models import VMR

# VIEWS FRANCAIS.

def events(request):
    current_date = datetime.now().date()
    upcoming_events = Event.objects.filter(date_debut__gte=current_date)
    past_events = Event.objects.filter(date_fin__lt=current_date)
    return render(request, "site/events.html", context={
        "upcoming_events": upcoming_events,
        "past_events": past_events
    })

def index(request):
    annonce = Annonce.objects.order_by('-id')
    return render(request, "site/index.html", context={"annonces" : annonce})

def docs(request):
    docs = doc.objects.all()
    return render(request, "site/doc.html", context={"docs": docs})

def contact(request):
    return render(request, "site/contact.html")

def livrees(request):
    return render(request, "site/livrees.html")

def vmr_list(request):
    vmr = VMR.objects.all()
    return render(request, "site/vmr.html", context={"vmr" : vmr})

def privacy_policy(request):
    return render(request, "site/privacy_policy.html")

def voltige(request):
    livree = Livree.objects.filter(simulateur = "PAF")
    return render(request, "site/voltige.html", context={"livrees" : livree})

def livrees_XP(request):
    livree = Livree.objects.filter(simulateur = "XP")
    return render(request, "site/livrees_xp.html", context={"livrees" : livree})

def formation_list(request):
    formations = formation.objects.all()
    q = request.GET.get('q')
    if q:
        formations = formations.filter(
            Q(titre__icontains=q) 
        )
    return render(request, 'site/formation.html', {'formations': formations})

def livrees_MSFS(request):
    livrees = Livree.objects.filter(simulateur = "MFS").order_by('ordre')
    q = request.GET.get('q')
    if q:
        livrees = livrees.filter(
            Q(avion__icontains=q) |
            Q(immat__icontains=q) |
            Q(editeur__icontains=q)
        )
    return render(request, 'site/livrees_MSFS.html', {'livrees': livrees})

def AIRBUS(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "AIB")
    return render(request, 'site/livrees_MSFS.html', {'livrees': livrees})

def BOEING(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "BOE")
    return render(request, 'site/livrees_MSFS.html', {'livrees': livrees})

def LEGER(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "LEG")
    return render(request, 'site/livrees_MSFS.html', {'livrees': livrees})

def HELICO(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "HEL")
    return render(request, 'site/livrees_MSFS.html', {'livrees': livrees})

#views ANGLAIS

def en_index(request):
    annonce = Annonce.objects.order_by('-id')
    return render(request, "en/index.html", context={"annonces" : annonce})

def en_docs(request):
    docs = doc.objects.all()
    return render(request, "en/doc.html", context={"docs": docs})

def en_contact(request):
    return render(request, "en/contact.html")

def en_livrees(request):
    return render(request, "en/livrees.html")

def en_vmr_list(request):
    vmr = VMR.objects.all()
    return render(request, "en/vmr.html", context={"vmr" : vmr})

def en_voltige(request):
    livree = Livree.objects.filter(simulateur = "PAF")
    return render(request, "en/voltige.html", context={"livrees" : livree})

def en_livrees_XP(request):
    livree = Livree.objects.filter(simulateur = "XP")
    return render(request, "en/livrees_xp.html", context={"livrees" : livree})

def en_events(request):
    current_date = datetime.now().date()
    upcoming_events = Event.objects.filter(date_debut__gte=current_date)
    past_events = Event.objects.filter(date_fin__lt=current_date)
    return render(request, "en/events.html", context={
        "upcoming_events": upcoming_events,
        "past_events": past_events
    })

def en_formation_list(request):
    formations = formation.objects.all()
    q = request.GET.get('q')
    if q:
        formations = formations.filter(
            Q(titre__icontains=q) 
        )
    return render(request, 'en/formation.html', {'formations': formations})

def en_livrees_MSFS(request):
    livrees = Livree.objects.filter(simulateur = "MFS")
    q = request.GET.get('q')
    if q:
        livrees = livrees.filter(
            Q(avion__icontains=q) |
            Q(immat__icontains=q) |
            Q(editeur__icontains=q)
        )
    return render(request, 'en/livrees_MSFS.html', {'livrees': livrees})

def en_AIRBUS(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "AIB")
    return render(request, 'en/livrees_MSFS.html', {'livrees': livrees})

def en_BOEING(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "BOE")
    return render(request, 'en/livrees_MSFS.html', {'livrees': livrees})

def en_LEGER(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "LEG")
    return render(request, 'en/livrees_MSFS.html', {'livrees': livrees})

def en_HELICO(request):
    livrees = Livree.objects.filter(simulateur = "MFS" ).filter(Filtre = "HEL")
    return render(request, 'en/livrees_MSFS.html', {'livrees': livrees})

