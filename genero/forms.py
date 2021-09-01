from django import forms
from genero.models import Genero
class GeneroForm(forms.ModelForm):
  #  def __init__(self, *args, **kwargs):
  #      super(GeneroForm, self).__init__(*args, **kwargs)
  #      self.fields('descricao').error_messages={'required':'Campo Obrigatorio'}

  #  descricao = forms.CharField(label='Gênero', required=True)

    class Meta:
        model = Genero
        fields = '__all__'