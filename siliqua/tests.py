#coding:utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from models import TipoPadrao, TipoDecisao, Padrao, Decisao
from django.core.urlresolvers import resolve

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


###########################################testes de bd##############################################

#testes positivos
class TipoPadraoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")

    def test_models(self):
        tipoPadrao = TipoPadrao.objects.get(id=1)
        self.assertEqual(tipoPadrao.nome, "tipo de padrao")

class TipoDecisaoTest(TestCase):

    def setUp(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")

    def test_models(self):
        tipoDecisao = TipoDecisao.objects.get(id=1)
        self.assertEqual(tipoDecisao.nome, "tipo de decisao")

class PadraoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.padrao = Padrao.objects.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias",
                                            tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)


    def test_models(self):
        padroes = Padrao.objects.all()
        self.assertEqual(padroes.count(), 3)

class DecisaoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        self.decisao = Decisao.objects.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado', categoria="categoria")


        self.decisao.decisaoRelacionada.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado', categoria="categoria")
        self.decisao.decisaoRelacionada.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado', categoria="categoria")

        self.decisao.padraoUtilizado.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)

    def test_models(self):
        decisoes = Decisao.objects.all()
        self.assertEqual(decisoes.count(), 3)




################################################## teste views #########################################################


##class HomePageTest(TestCase):

##    def test_url(self):
  ##      c = Client()
    ##    response = c.get('/')
      ##self.assertEqual(response, 200)