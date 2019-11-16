from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
 
# Importa form
from meusite.forms import MeuForm
 
# Exibe View
def home(request):
 
    # Cria form
    form = MeuForm(request.POST or None)   
 
    # Valida e salva
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")
 
    # Chama Template
    return render_to_response("devaberto.html",
                              locals(),
                              context_instance = RequestContext(request))