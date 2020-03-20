# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime
def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    dateYYYYMMJJ_HH_MM_SS=datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S.%f')
    #print(instance.nom)
    return u'{0}-{1}'.format(dateYYYYMMJJ_HH_MM_SS,filename)

class Communes(models.Model):
    cp = models.CharField(max_length=6)
    ville = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    class Meta:
        db_table = 'communes'


class Adresses(models.Model):
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=6)
    ville = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    class Meta:
        db_table = 'adresses'


image_storage_marches= FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/marches/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/marches/'.format(settings.MEDIA_URL),
)

class Marches(models.Model):
    nom = models.CharField(max_length=255)
    photo =   models.ImageField(upload_to=image_directory_path, storage=image_storage_marches,null=True)
    manifestation = models.ForeignKey('RefManifestation', models.DO_NOTHING)
    frequence = models.ForeignKey('RefFrequence', models.DO_NOTHING)
    heure_debut = models.ForeignKey('RefHoraire', models.DO_NOTHING, related_name='heure_debut')
    heure_fin = models.ForeignKey('RefHoraire', models.DO_NOTHING ,related_name='heure_fin')
    adresse = models.ForeignKey(Adresses, models.DO_NOTHING)
    nb_exposant = models.IntegerField(blank=True, null=True)
    date_debut_id = models.IntegerField()
    date_fin_id = models.IntegerField(blank=True, null=True)
    historique= models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'marches'







class Avis(models.Model):
    avis = models.CharField(max_length=255, blank=True, null=True)
    note = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'avis'


class Calendrier(models.Model):
    date_du_jour = models.DateField()
    date_f1 = models.CharField(max_length=10)
    date_f2 = models.CharField(max_length=10)
    date_yyyymm = models.CharField(max_length=6)
    date_yyyymmdd = models.CharField(max_length=8)
    date_yyyy = models.CharField(max_length=4)
    num_mois = models.IntegerField()
    nom_mois = models.CharField(max_length=20)
    nom_jour = models.CharField(max_length=20)
    num_jour_semaine = models.IntegerField()
    num_jour_mois = models.IntegerField()
    num_jour_annee = models.IntegerField()
    num_semaine = models.IntegerField()
    dernier_jour_mois = models.DateField()
    weekend = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'calendrier'

image_storage_client = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/clients/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/clients/'.format(settings.MEDIA_URL),
)
    

class Clients(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    connexion = models.ForeignKey('Connexions', models.DO_NOTHING, blank=True, null=True)
    type_client = models.ForeignKey('RefTypeClient', models.DO_NOTHING)
    num_telephone_portable = models.CharField(max_length=10, blank=True, null=True)
    photo =   models.ImageField(upload_to=image_directory_path, storage=image_storage_client)
    adresse = models.ForeignKey(Adresses, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clients'


class Commande(models.Model):
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    montant = models.FloatField()

    class Meta:
        managed = False
        db_table = 'commande'


class Connexions(models.Model):
    identifiant = models.CharField(max_length=25)
    password = models.CharField(max_length=255, verbose_name=u"Mot de passe")
    email = models.CharField(max_length=255)
    opt_in = models.BooleanField(default=False)
    num_random = models.CharField(max_length=255)
    etat_connexion = models.BooleanField(default=False)

    class Meta:
        db_table = 'connexions'


class JourMarche(models.Model):
    ref_marche = models.ForeignKey('Marches', models.DO_NOTHING)
    jours_semaine = models.ForeignKey('RefJoursSemaine', models.DO_NOTHING)
    class Meta:
        db_table = 'jour_marche'


    
class MiseEnVente(models.Model):
    produit = models.ForeignKey('Produits', models.DO_NOTHING)
    producteur = models.ForeignKey('Producteurs', models.DO_NOTHING)
    ordre_affichage= models.IntegerField(null=False)
    prix = models.DecimalField(max_digits=2, decimal_places=2)
    quantite_stock = models.IntegerField(blank=True, null=True)
    poids_stock = models.IntegerField(blank=True, null=True)
    quantite_vendu = models.IntegerField(blank=True, null=True)
    poids_vendu = models.IntegerField(blank=True, null=True)
    etat_stock = models.BooleanField()

    class Meta:
        db_table = 'mise_en_vente'

image_storage_producteur = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/producteurs/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/producteurs/'.format(settings.MEDIA_URL),
)

class Producteurs(models.Model):
    nom = models.CharField(max_length=50)
    photo =   models.ImageField(upload_to=image_directory_path, storage=image_storage_producteur)
    raison_social = models.CharField(max_length=9, blank=True, null=True)
    num_siren = models.CharField(max_length=15, blank=True, null=True)
    connexions = models.ForeignKey(Connexions, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    num_telephone_fix = models.CharField(max_length=10, blank=True, null=True)
    num_telephone_portable = models.CharField(max_length=10, blank=True, null=True)
    metier = models.ForeignKey('RefMetier', models.DO_NOTHING, null=True)
    adresse = models.ForeignKey(Adresses, models.DO_NOTHING, null=True)
    date_debut_id = models.IntegerField()
    date_fin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'producteurs'


image_storage_produit = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/produits/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/produits/'.format(settings.MEDIA_URL),
)

class Produits(models.Model):
    nom = models.CharField(max_length=255)
    photo =   models.ImageField(upload_to=image_directory_path, storage=image_storage_produit)
    categorie = models.ForeignKey('RefCategorie', models.DO_NOTHING)

    class Meta:
        db_table = 'produits'

image_storage_categorie= FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/produits_categories/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/produits_categories/'.format(settings.MEDIA_URL),
)
   
class RefCategorie(models.Model):
    label = models.CharField(max_length=50)
    photo =   models.ImageField(upload_to=image_directory_path, storage=image_storage_categorie)

    class Meta:
        db_table = 'ref_categorie'


class RefFrequence(models.Model):
    label = models.CharField(max_length=25)

    class Meta:
        db_table = 'ref_frequence'


class RefHoraire(models.Model):
    label = models.CharField(max_length=5)
    description = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'ref_horaire'


class RefJoursSemaine(models.Model):
    jours = models.CharField(max_length=15)

    class Meta:
        db_table = 'ref_jours_semaine'


class RefManifestation(models.Model):
    label = models.CharField(max_length=25)

    class Meta:
        db_table = 'ref_manifestation'


class RefMetier(models.Model):
    label = models.CharField(max_length=50)

    class Meta:
        db_table = 'ref_metier'


class RefTypeClient(models.Model):
    label = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'ref_type_client'


class RefTypeRetrait(models.Model):
    label = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'ref_type_retrait'


class Sederouler(models.Model):
    id = models.IntegerField(primary_key=True)
    ref_marche = models.ForeignKey(Marches, models.DO_NOTHING)
    date_marche_id = models.IntegerField()
    producteur = models.ForeignKey(Producteurs, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sederouler'


class Tickets(models.Model):
    id = models.IntegerField(primary_key=True)
    commande = models.ForeignKey(Commande, models.DO_NOTHING)
    calendrier_id = models.IntegerField()
    type_retrait = models.ForeignKey(RefTypeRetrait, models.DO_NOTHING)
    adresse_id = models.IntegerField()
    produit_id = models.IntegerField()
    prix = models.FloatField()
    quantite = models.IntegerField(blank=True, null=True)
    poids = models.IntegerField(blank=True, null=True)
    avis = models.ForeignKey(Avis, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tickets'
