from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = (
            'nom','prenom','lieu_nais','date_nais','sexe','email','contact','matricule','cni',
            'carte_etudiant','carte_cni','universite','niveau','ufr','filiere','specialite',
            'ville','commune'
        )
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'lieu_nais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance'}),
            'date_nais': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance', 'type': 'date'}),
            'sexe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sexe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro Carte Etudiant'}),
            'cni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero CNI'}),
            'carte_etudiant': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Carte Etudiant'}),
            'carte_cni': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Import'}),
            'universite': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Universite'}),
            'niveau': forms.Select(attrs={'class': 'form-control'}),
            'ufr': forms.Select(attrs={'class': 'form-control'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'specialite': forms.Select(attrs={'class': 'form-control'}),
            'ville': forms.Select(attrs={'class': 'form-control'}),
            'commune': forms.Select(attrs={'class': 'form-control'}),
        }


        
        
    