from django.db import models


class JoursSemaine(models.Model):
    jours = models.CharField(max_length=15)

    class Meta:
        db_table = 'jours_semaine'

    def __str__(self):
        return self.jours


class Horaire(models.Model):
    heure = models.CharField(max_length=5)

    class Meta: 
        db_table = 'horaire'
    def __str__(self):
        return self.heure


class Adresse(models.Model):
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=6)
    ville = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'adresse'
    def __str__(self):
        return "{} {} {} ({},{})".format(self.adresse,self.cp,self.ville,self.latitude,self.longitude)

class Marche(models.Model):
    nom = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    jours_semaine= models.ManyToManyField(JoursSemaine, related_name='jours_Semaine', blank=True)
    heure_debut = models.ForeignKey(Horaire, models.DO_NOTHING, related_name='heure_debut')
    heure_fin = models.ForeignKey(Horaire, models.DO_NOTHING,related_name='heure_fin')
    adresse = models.ForeignKey(Adresse, models.DO_NOTHING)

    class Meta:
        db_table = 'marche'
        verbose_name = "Marché"

    def __str__(self):
        return "{}" .format(self.nom)

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
        db_table = 'calendrier'

    def __str__(self):
        return "{}" .format(self.date_f1)




class Sederouler(models.Model):
    calendrier = models.ForeignKey('Calendrier', models.DO_NOTHING)
    ref_marche = models.ForeignKey('RefMarche', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'derouler'

         
