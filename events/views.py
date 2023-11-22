from django.shortcuts import render

from django.db.models import Q
from datetime import datetime

from events.models import Event
from events.models import Annonce
from events.models import Livree
from events.models import doc
from events.models import formation
from events.models import VMR
from events.models import ALERT
from events.models import VOL

from events.calcul_stats import temps_totale
from events.calcul_stats import temps_vol_cid

# VIEWS FRANCAIS.

def events(request):
    current_datetime = datetime.utcnow()
    upcoming_events = Event.objects.filter(Q(date_debut__gt=current_datetime) | Q(
        date_fin__gt=current_datetime, date_debut__lte=current_datetime)).order_by('date_debut')
    past_events = Event.objects.filter(
        date_fin__lt=current_datetime).order_by('-date_debut')
    return render(request, "site/events.html", context={
        "upcoming_events": upcoming_events,
        "past_events": past_events,
    })

def index(request):
    annonce = Annonce.objects.order_by('-id')
    alerts = ALERT.objects.all()
    return render(request, "site/index.html",
                  context={
                      "annonces": annonce,
                      "alerts": alerts,
                  })

def docs(request):
    docs = doc.objects.all()
    return render(request, "site/doc.html", context={"docs": docs})


def contact(request):
    return render(request, "site/contact.html")


def vmr_list(request):
    vmr = VMR.objects.all()
    return render(request, "site/vmr.html", context={"vmr": vmr})


def privacy_policy(request):
    return render(request, "site/privacy_policy.html")


def voltige(request):
    livree = Livree.objects.filter(simulateur="PAF")
    return render(request, "site/voltige.html", context={"livrees": livree})


def stats(request):
    return render(request, "site/stats.html")


def livrees_XP(request):
    livree = Livree.objects.filter(simulateur="XP")
    return render(request, "site/livrees_xp.html", context={"livrees": livree})


def formation_list(request):
    formations = formation.objects.all()
    q = request.GET.get('q')
    if q:
        formations = formations.filter(
            Q(titre__icontains=q)
        )
    return render(request, 'site/formation.html', {'formations': formations})


def livrees_MSFS(request):
    livrees = Livree.objects.filter(simulateur="MFS")
    q = request.GET.get('q')
    if q:
        livrees = livrees.filter(
            Q(avion__icontains=q) |
            Q(immat__icontains=q) |
            Q(editeur__icontains=q)
        )
    column1 = request.GET.getlist('Filtre_constructeur')
    column2 = request.GET.getlist('Filtre_livree')
    column3 = request.GET.getlist('Filtre_type')

    query = Q()
    filters_applied = False

    if column1:
        query &= Q(Filtre_constructeur__in=column1)
        filters_applied = True
    if column2:
        query &= Q(Filtre_livree__in=column2)
        filters_applied = True
    if column3:
        query &= Q(Filtre_type__in=column3)
        filters_applied = True

    if filters_applied:
        livrees = livrees.filter(query)

    context = {
        'livrees': livrees
    }
    return render(request, 'site/livrees_MSFS.html', context)

def carnetdevol(request):
    vols = VOL.objects.all().order_by('-date_co')

    temps = temps_totale()

    q = request.GET.get('q')
    if q:
        temps = temps_vol_cid(q)
        vols = vols.filter(
            Q(cid__icontains=q)
        )

    return render(request, "site/carnetdevol.html", context= {"vols" : vols, "temps" : temps})

def WF(request):
    return render(request, "site/wf-2023.html")

# views ANGLAIS


def en_index(request):
    annonce = Annonce.objects.order_by('-id')
    return render(request, "en/index.html", context={"annonces": annonce})


def en_docs(request):
    docs = doc.objects.all()
    return render(request, "en/doc.html", context={"docs": docs})


def en_contact(request):
    return render(request, "en/contact.html")


def en_vmr_list(request):
    vmr = VMR.objects.all()
    return render(request, "en/vmr.html", context={"vmr": vmr})


def en_voltige(request):
    livree = Livree.objects.filter(simulateur="PAF")
    return render(request, "en/voltige.html", context={"livrees": livree})


def en_livrees_XP(request):
    livree = Livree.objects.filter(simulateur="XP")
    return render(request, "en/livrees_xp.html", context={"livrees": livree})


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
    livrees = Livree.objects.filter(simulateur="MFS")
    q = request.GET.get('q')
    if q:
        livrees = livrees.filter(
            Q(avion__icontains=q) |
            Q(immat__icontains=q) |
            Q(editeur__icontains=q)
        )
    column1 = request.GET.getlist('Filtre_constructeur')
    column2 = request.GET.getlist('Filtre_livree')
    column3 = request.GET.getlist('Filtre_type')

    query = Q()
    filters_applied = False

    if column1:
        query &= Q(Filtre_constructeur__in=column1)
        filters_applied = True
    if column2:
        query &= Q(Filtre_livree__in=column2)
        filters_applied = True
    if column3:
        query &= Q(Filtre_type__in=column3)
        filters_applied = True

    if filters_applied:
        livrees = livrees.filter(query)

    context = {
        'livrees': livrees
    }
    return render(request, 'en/livrees_MSFS.html', context)


def en_WF(request):
    return render(request, "en/wf-2023-en.html")
