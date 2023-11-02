from django.db import models
import locale

# Create your models here.
"""
event 
- titre
-description
-date_debut
-end_time
"""


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    event_id = models.IntegerField()
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date_debut})"

    def format_date_debut(self):
        return self.date_debut.strftime("%A %d %B à %H%M")

    def format_date_fin(self):
        return self.date_fin.strftime("%A %d %B à %H%M")


"""
Annonce 
- content
- title
- author
- annonce_id
"""


class Annonce(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    annonce_id = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


"""
Livrees
- Avion
- Immat
- Editeur
- Photo1
- Photo2
- Lien
- Page d'affichage
- Catégorie de filtrage
"""


class Livree(models.Model):
    avion = models.CharField(max_length=100)
    immat = models.CharField(max_length=10)
    editeur = models.CharField(max_length=100)
    photo1 = models.ImageField(upload_to="dossier_image/")
    photo2 = models.ImageField(upload_to="dossier_image/")
    fichier = models.FileField(upload_to="lien_livrees/")
    ordre = models.IntegerField()

    Xplane = 'XP'
    MFS = 'MFS'
    PAF = 'PAF'
    SIMU = [
        (Xplane, 'X-Plane'),
        (MFS, 'Microsoft Flight Sim'),
        (PAF, 'Pains accrobatiques'),
    ]

    simulateur = models.CharField(
        max_length=3,
        choices=SIMU,
        default=MFS,
    )

    # FILTRAGE

    # filtre1

    AIRBUS = 'AIRBUS'
    BOEING = 'BOEING'
    CESSNA = 'CESSNA'

    Filtrage1 = [
        (AIRBUS, 'AIRBUS'),
        (BOEING, 'BOEING'),
        (CESSNA, 'CESSNA'),
    ]

    Filtre_constructeur = models.CharField(
        max_length=6,
        choices=Filtrage1,
        default=AIRBUS,
        blank=True
    )

    # filtre2

    CLASSIQUE = 'CLASSIQUE'
    SPECIALE = 'SPECIALE'

    Filtrage2 = [
        (CLASSIQUE, 'CLASSIQUE'),
        (SPECIALE, 'SPECIALE'),
    ]

    Filtre_livree = models.CharField(
        max_length=9,
        choices=Filtrage2,
        default=CLASSIQUE,
        blank=True
    )

    # filtre3

    LINER = 'LINER'
    AFFAIRE = 'AFFAIRE'
    GENERAL = 'GENERAL'
    HELICOPTERE = 'HELICO'

    Filtrage3 = [
        (LINER, 'LINER'),
        (AFFAIRE, 'AFFAIRE'),
        (GENERAL, 'GENERAL'),
        (HELICOPTERE, 'HELICO'),
    ]

    Filtre_type = models.CharField(
        max_length=7,
        choices=Filtrage3,
        default=LINER,
        blank=True
    )

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return f" {self.ordre} / {self.simulateur} - {self.avion} ({self.editeur})"


"""
Doc
- Titre
- Lien 
- Catégorie 
"""


class doc(models.Model):
    titre = models.CharField(max_length=500)
    lien = models.URLField()
    Fonctionnement = 'FT'
    ATO = 'AT'
    DOC_CHOICES = [
        (Fonctionnement, 'Fonctionnement du club'),
        (ATO, 'ATO'),
    ]
    categorie = models.CharField(
        max_length=2,
        choices=DOC_CHOICES,
        default=Fonctionnement,
    )

    def __str__(self):
        return f"{self.titre} ({self.categorie})"


"""
Formations
- Titre
- Lien
- Image
"""


class formation(models.Model):
    titre = models.CharField(max_length=300)
    lien = models.URLField()
    image = models.ImageField(upload_to="dossier_image/")

    def __str__(self):
        return f"{self.titre}"


"""
VMR
- Titre
- Lien 
"""


class VMR(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to="lien_VMR/")

    def __str__(self):
        return f"{self.titre}"


"""
alert
- Contenu
- Lien
"""


class ALERT(models.Model):
    contenu = models.CharField(max_length=124)
    hyperlink_msg = models.CharField(max_length=30, blank=True)
    lien = models.URLField(blank=True)

    def __str__(self):
        return f"{self.contenu}"
