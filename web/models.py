from django.db import models

from django.utils import timezone

# Create your models here.

class Universite(models.Model):
    name = models.CharField('Nom', unique=True, max_length=200)
    code = models.CharField('Code', unique=True, max_length=20)
    email = models.EmailField('Email', unique=True)
    contact = models.CharField('Contact', unique=True, max_length=100)
    

    class Meta: 
     verbose_name_plural = "Universités"

    def __str__(self):
        return self.name
    


class Sexe(models.Model):
    libelle = models.CharField('Libellé', max_length=20)


    class Meta: 
     verbose_name_plural = "Sexe"

    def __str__(self):
        return self.libelle
    
    

class Ufr(models.Model):
    libelle = models.CharField('Libellé',unique=True, max_length=150)
    code = models.CharField('Code', unique=True, max_length=20)
    email = models.EmailField('Email', unique=True)
    contact = models.CharField('Contact', unique=True, max_length=100)
    universite = models.ForeignKey(Universite, verbose_name ='Université', on_delete = models.CASCADE)


    class Meta: 
     verbose_name_plural = "UFR"

    def __str__(self):
        return self.libelle


class Filiere(models.Model):
    libelle = models.CharField('Libellé',unique=True, max_length=150)
    code = models.CharField('Code', unique=True, max_length=20)
    ufr = models.ForeignKey(Ufr, verbose_name ='ufr', on_delete = models.CASCADE)


    class Meta: 
     verbose_name_plural = "Filière"

    def __str__(self):
        return self.libelle


class Specialite(models.Model):
    libelle = models.CharField('Libellé',unique=True, max_length=150)
    filiere = models.ForeignKey(Filiere, verbose_name ='Filière', on_delete = models.CASCADE)


    class Meta: 
     verbose_name_plural = "Specialité"

    def __str__(self):
        return self.libelle


class Niveau(models.Model):
    libelle = models.CharField('Libellé',unique=True, max_length=150)

    class Meta: 
     verbose_name_plural = "Niveau"

    def __str__(self):
        return self.libelle
    
class NiveauSpecialite(models.Model):
    niveau = models.ForeignKey(Niveau, verbose_name ='Niveau', on_delete = models.CASCADE)
    specialite = models.ForeignKey(Specialite, verbose_name ='Specialité', on_delete = models.CASCADE)
    class Meta: 
     verbose_name_plural = "Niveau et Specialité"

    #def __str__(self):
    #    return self.libelle
    

class Ville(models.Model):
    libelle = models.CharField('Nom',unique=True, max_length=150)

    class Meta: 
     verbose_name_plural = "Ville"

    def __str__(self):
        return self.libelle


class Commune(models.Model):
    libelle = models.CharField('Nom',unique=True, max_length=150)
    ville = models.ForeignKey(Ville, verbose_name ='Ville', on_delete = models.CASCADE)

    class Meta: 
     verbose_name_plural = "Commune"

    def __str__(self):
        return self.libelle


class Etudiant(models.Model):
    nom = models.CharField('Nom', max_length=80)
    prenom = models.CharField('Prénoms',  max_length=100)
    lieu_nais = models.CharField('Lieu de naissance',  max_length=100)
    date_nais = models.DateField('Date de naissance')
    sexe = models.ForeignKey(Sexe, verbose_name ='Sexe', on_delete = models.CASCADE)
    email = models.EmailField('Email', unique=True)
    contact = models.CharField('Téléphone', unique=True, max_length=100)
    matricule = models.CharField('N° de carte d\'étudiant', unique=True, max_length=15)
    cni = models.CharField('N° CNI', unique=True, max_length=15)
    carte_etudiant = models.FileField('Carte d\'etudiant', upload_to = 'carte_etudiant')
    carte_cni = models.FileField('Carte CNI', upload_to = 'cni')
    universite = models.ForeignKey(Universite, verbose_name ='Université', on_delete = models.CASCADE)
    niveau = models.ForeignKey(Niveau, verbose_name ='Niveau', on_delete = models.CASCADE)
    ufr = models.ForeignKey(Ufr, verbose_name ='UFR', on_delete = models.CASCADE)
    filiere = models.ForeignKey(Filiere, verbose_name ='Filière', on_delete = models.CASCADE)
    specialite = models.ForeignKey(Specialite, verbose_name ='Specialité', on_delete = models.CASCADE)
    ville = models.ForeignKey(Ville, verbose_name ='Ville', on_delete = models.CASCADE)
    commune = models.ForeignKey(Commune, verbose_name ='Commune', on_delete = models.CASCADE)
    date = models.DateTimeField(verbose_name='Date d\'identification', default= timezone.now)


    class Meta: 
     verbose_name_plural = "Etudiant"

    def __str__(self):
        return self.nom