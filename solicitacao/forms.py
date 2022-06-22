from django import forms
from solicitacao.models import Solicitacao

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            "kit", "matricula",
        ]