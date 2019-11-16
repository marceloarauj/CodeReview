from  django import forms
from django.core.validators import RegexValidator
 
#Importa modulo Regex
import re 
 
# cria objeto Regex
caracteres = RegexValidator(
    regex= re.compile(r"[a-zA-Z]+"),
    message="Permitido somente caracteres Alpha numericos",
    code="invalid")
 
# Importa modelo
from models import Funcionario
 
# Cria classe do form para o modelo
class MeuForm(forms.ModelForm):
    nome = forms.CharField(required= True, validators=[caracteres])
    sobrenome = forms.CharField(required= True, validators= [caracteres])
    cargo = forms.CharField(required= True, validators= [caracteres])
    salario = forms.DecimalField()
 
    # Associa formulario ao modelo
    class Meta:
        model = Funcionario
 
    # Django Validations  - customizado campo sobrenome
    def clean_sobrenome(self):
        snome = self.cleaned_data['sobrenome']
        if len(snome) <= 3:
            raise forms.ValidationError("Sobrenome precisa conter mais de 3 caracteres.")
        return snome