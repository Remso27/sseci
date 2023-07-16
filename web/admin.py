from django.contrib import admin
from .models import *


# Register your models here.
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ['name','code', 'email', 'contact']
    search_fields = ['name']
    

class SexeAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class UfrAdmin(admin.ModelAdmin):
    list_display = ['libelle','code', 'email', 'contact', 'universite']
    search_fields = ['libelle']
    
class FiliereAdmin(admin.ModelAdmin):
    list_display = ['libelle','code','ufr']
    search_fields = ['libelle']

class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'filiere']
    search_fields = ['libelle']
    

class NiveauAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class NiveauSpecialiteAdmin(admin.ModelAdmin):
    list_display = ['niveau', 'specialite']
    search_fields = ['niveau']


class VilleAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class CommuneAdmin(admin.ModelAdmin):
    list_display = ['libelle','ville']
    search_fields = ['libelle']


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['nom','prenom', 'lieu_nais','date_nais','sexe','email', 'contact', 
                    'matricule','cni','carte_etudiant', 'carte_cni', 'universite','niveau',
                    'ufr','filiere', 'specialite', 'ville', 'commune', 'date']
    list_filter = ['universite']
    search_fields = ['nom']



admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(NiveauSpecialite, NiveauSpecialiteAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Ufr, UfrAdmin)
admin.site.register(Sexe, SexeAdmin)
admin.site.register(Universite, UniversiteAdmin)
