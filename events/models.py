from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField(max_length=128)
	email = models.TextField(max_length=100)

	def __str__(self):
		return self.nome

class Evento(models.Model):
	nome = models.CharField(max_length=128)
	eventoPrincipal = models.CharField(max_length=128)
	sigla = models.CharField(max_length=10)
	dataEHoradeInicio = models.DateField(blank=True, null=True)
	palavrasChave = models.CharField(max_length=30)
	logotipo = models.CharField(max_length=30)
	realizador = models.ForeignKey(Pessoa, null=True, blank=True)
	cidade = models.CharField(max_length=50)
	uf = models.CharField(max_length=2)
	endereco = models.CharField(max_length=150,blank=False, null=False)
	cep = models.CharField(max_length=10)

class EventoCientifico(Evento):
	issn = models.TextField()
	def __str__(self):
		return self.issn


class PessoaFisica(Pessoa):
	cpf = models.CharField(max_length=100)
	def __str__(self):
		return self.cpf

class PessoaJuridica(Pessoa):
	cnpj = models.CharField(max_length=100)
	razaoSocial = models.CharField(max_length=100)
	def __str__(self):
		return self.cnpj

class Autor(Pessoa):
	curriculo = models.TextField()
	
	def __str__(self):
		return self.curriculo


class ArtigoCientifico(models.Model):
	titulo = models.CharField(max_length=128,blank=False, null=False)
	evento = models.ForeignKey(EventoCientifico, null=True, blank=False)
	#autor = ArrayField(models.CharField(max_length=200), blank=True)

	def __str__(self):
		return self.titulo