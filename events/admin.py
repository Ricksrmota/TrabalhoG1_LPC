from django.contrib import admin
from events.models import Pessoa
from events.models import PessoaFisica
from events.models import PessoaJuridica
from events.models import Autor
from events.models import Evento
from events.models import EventoCientifico
from events.models import ArtigoCientifico


admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(Autor)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)