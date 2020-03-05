# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your tests here.

import crypt
from django.test import RequestFactory,TestCase
from marketPlace.models import Connexions,Producteurs,RefMetier,Adresses
from django.utils import timezone
from .forms import ConnexionProducteurForm,ParagraphErrorList,IdentificationProducteurForm
from marketPlace import settings
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class connexionTest(TestCase,StaticLiveServerTestCase):
    
    @classmethod
    def setUpTestData(cls):
        Connexions.objects.create(identifiant="Jeg", password=crypt.crypt("password"),email='test@gmail.com', num_random='abcdef',opt_in=1 )
        Connexions.objects.create(identifiant="Jeg_2", password=crypt.crypt("password_2"),email='test_2@gmail.com', num_random='abcdef2' ,opt_in=1 )

        RefMetier.objects.create(label='Agriculteur')
        Adresses.objects.create(adresse='Adresse 1', cp='56500',ville='Bignan')



    def setUp(self):
        self.user_1=Connexions.objects.get(pk=1)
        self.user_2=Connexions.objects.get(pk=2)

    def test_create_producteur(self):
        self.assertEqual(self.user_1.id, 1)
        self.assertEqual(self.user_1.identifiant, 'Jeg')
        self.assertEqual(self.user_1.password, crypt.crypt("password", self.user_1.password))
        self.assertEqual(self.user_1.email, 'test@gmail.com')
        self.assertEqual(self.user_1.num_random, 'abcdef')
        self.assertEqual(self.user_1.etat_connexion, False)

        self.assertEqual(self.user_2.id, 2)
        self.assertEqual(self.user_2.identifiant, 'Jeg_2')
        self.assertEqual(self.user_2.password, crypt.crypt("password_2", self.user_2.password))
        self.assertEqual(self.user_2.email, 'test_2@gmail.com')
        self.assertEqual(self.user_2.num_random, 'abcdef2')
        self.assertEqual(self.user_2.etat_connexion, False)


    def test_inscription_valider(self):
        
        #response = self.client.get(reverse('connexion:inscription_valider', {'id':self.user_1.num_random}))
        
        response = self.client.get('/connexion/inscription/{}/'.format(self.user_1.num_random))
        user_1=Connexions.objects.get(pk=1)
        self.assertEqual(user_1.etat_connexion, True)
   

        response = self.client.get('/connexion/inscription/{}/'.format(self.user_2.num_random))
        user_2=Connexions.objects.get(pk=2)
        self.assertEqual(user_2.etat_connexion, True)



# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.headless = True
        cls.selenium = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()



    def test_bout_en_bout_connexion_producteur(self):

        #Connexion à la page d'inscription
        self.selenium.get("%s%s" % (self.live_server_url, reverse('connexion:inscription_producteur')))
        self.selenium.implicitly_wait(1)


        #Rempli le formulaire
        self.selenium.find_element_by_name("identifiant").send_keys('jeg3')
        self.selenium.find_element_by_name("password").send_keys('ABCDEFGHIJ')
        self.selenium.find_element_by_name("repassword").send_keys('ABCDEFGHIJ')
        self.selenium.find_element_by_name("email").send_keys('a@gmail.com')
        self.selenium.find_element_by_name("opt_in").send_keys('1')

        self.selenium.find_element_by_xpath('/html/body/div/div/div/form/div[6]/button').click()

        #Recupère la nvlle inscription 
        user=Connexions.objects.get(pk=3)
        self.assertEqual(user.identifiant, 'jeg3')
        self.assertEqual(user.email, 'a@gmail.com')
        self.assertEqual(user.etat_connexion, False)

        #Valide le lien 
        self.client.get('/connexion/inscription/{}/'.format(user.num_random))
        user=Connexions.objects.get(pk=3)
        self.assertEqual(user.etat_connexion, True)

        print('---------------------------------------               -----------------------------------------                               ----------------------------------')
        print('---------------------------------------               -----------------------------------------                               ----------------------------------')
        #on se connecte 
        self.selenium.get("%s%s" % (self.live_server_url, reverse('connexion:identification')))
        self.selenium.implicitly_wait(1)

        self.selenium.find_element_by_name("identifiant").send_keys(user.identifiant)
        self.selenium.find_element_by_name("password").send_keys('ABCDEFGHIJ')
        
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_xpath('//*[@id="btn-identifier"]').click()


        connexion = Connexions.objects.filter(identifiant=user.identifiant)
        self.selenium.get("%s%s" % (self.live_server_url, reverse('producteur:fiche_producteur', args=(int(Producteurs.objects.get(connexions_id=connexion.first().id).id),) )))

        self.selenium.implicitly_wait(1)
        #assert 'Vous êtes connecté' in self.selenium.page_source






