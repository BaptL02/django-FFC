from django.shortcuts import render
from django.db.models import Q
from datetime import datetime

from events.models import Event
from events.models import Annonce
from events.models import Livree
from events.models import doc
from events.models import formation
from events.models import VMR
from events.models import Sondage, ChoixSondage

# Create your views here.



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
    livrees = Livree.objects.filter(simulateur = "MFS")
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

def sondage(request):
    sondage = Sondage.objects.all()
    return render(request, 'site/sondage.html', {'sondages': sondage})

def vote(request):
    sondage = Sondage.objects.all()
    choix_ids = request.POST.getlist('choix')
    for choix_id in choix_ids:
        choix = ChoixSondage.objects.get(pk=choix_id)
        choix.votes += 1
        choix.save()
    return render(request, 'site/resultats.html', {'sondage': sondage})
