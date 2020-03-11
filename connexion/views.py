# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ConnexionProducteurForm,ParagraphErrorList,IdentificationProducteurForm
from marketPlace.models import Connexions,Producteurs,RefMetier,Adresses
import random
import string
import crypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.db import transaction
from django.urls import reverse
from .fonctionnalites.proposition_identifiants import proposition_identifiants
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def identification(request):
    context = {
        'title': 'Identification'
        }
    context['form']=IdentificationProducteurForm()
    if request.method == 'POST':
        
        form = IdentificationProducteurForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            identifiant = form.cleaned_data['identifiant']
            password = form.cleaned_data['password']
            
            connexion = Connexions.objects.filter(identifiant=identifiant)
      
            if connexion.exists():
                if connexion.first().etat_connexion==False:
                    context['message']= 'Vous n''avez pas activé votre compte en cliquant sur le lien dans l''email'
                    return render(request, 'connexion/identification.html', context)
                else :
                    valid_password = crypt.crypt(password, connexion.first().password) == connexion.first().password
                    if(valid_password) :
                        #return HttpResponseRedirect('/producteur/{}'.format(Producteurs.objects.get(connexions_id=connexion.first().id).id))
                        request.session['identifiant'] = connexion.first().identifiant
                        request.session['id'] = connexion.first().id  

                        #Authentification Django
                        user = authenticate(username=identifiant, password=password)
     
                        if user is not None:
                            login(request, user)


                        return HttpResponseRedirect(reverse('producteur:fiche_producteur', args=(int(Producteurs.objects.get(connexions_id=connexion.first().id).id),)))
                      
                    else:
                        form.add_error('password', 'Identification invalide')
            else:
                form.add_error('identifiant', 'Identifiant inconnu ...')

                
            context['errors'] = form.errors.items()
            return render(request, 'connexion/identification.html', context)
    return render(request, 'connexion/identification.html', context)
    




def inscription_producteur(request):
    context = {
        'title': 'Formulaire d\'inscription des producteurs',
        'message': None,
        'form' : ConnexionProducteurForm()
        }
    if request.method == 'POST':

        form = ConnexionProducteurForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            
            identifiant = form.cleaned_data['identifiant']
            password = form.cleaned_data['password']
            repassword =  request.POST.get('repassword')
            email = form.cleaned_data['email']
            opt_in = form.cleaned_data['opt_in']

            # To encrypt the password. This creates a password hash with a random salt.
            password_hash = crypt.crypt(password)



            rechercheMailExistant = Connexions.objects.filter(email=email,etat_connexion=True)
            rechercheIdentifiantExistant = Connexions.objects.filter(identifiant=identifiant,etat_connexion=True)
            if not rechercheMailExistant.exists() and not rechercheIdentifiantExistant.exists() and repassword == password :
                lettersAndDigits = string.ascii_letters + string.digits
                lettersAndDigits_20=''.join(random.choice(lettersAndDigits) for i in range(20))


                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('mylittelmarkel@gmail.com', 'mylittelmarkel56')


                msg = MIMEMultipart("alternative")
                
                html = u"""\
                Bonjour,<br>
                Pour finaliser votre inscription, merci de cliquer sur ce lien ci-dessous : <br>
                <a href='http://127.0.0.1:8000/connexion/inscription/"""+lettersAndDigits_20+"""'>Finaliser l'inscription</a>,<br>,<br>
            
                L'équipe My littel Market.
                """
                msg['From'] = str('my littel Market <mylittelmarkel@gmail.com>')
                msg['To'] = email
                msg['Subject'] = "Inscription à my littel market"
                part2 = MIMEText(html, "html")
                msg.attach(part2)

                try:
          
                    server.sendmail('mylittelmarkel@gmail.com',email,msg.as_string())

                except smtplib.SMTPException as e:
                    print(e)
                server.quit()

                connexion = Connexions.objects.create(
                    identifiant=identifiant,
                    password=password_hash,
                    email=email,
                    opt_in=1 if opt_in=='on' else  0,
                    num_random=lettersAndDigits_20
                )
                connexion.save()

                #Sécurité Django
                user = User.objects.create_user(connexion.identifiant, connexion.email, password)




                context['message'] = "Merci de valider votre inscription en cliquant sur le lien que vous avez recu dans votre boite mail {} " .format(email)
                return render(request, 'connexion/identification.html', context)

            else:
                if repassword != password:
                    form.add_error('repassword', 'Mot de passe différent')
                if rechercheMailExistant.exists():
                    form.add_error('email', 'Cette adresse email est déjà utilisée.' )
                if rechercheIdentifiantExistant.exists():
                    form.add_error('identifiant', 'Cet identifiant existe déjà... Vous pouvez utilisez un de ces identifiants : {}'. format( ', '.join(proposition_identifiants(identifiant))))
                
                context['errors'] = form.errors.items()
        else:
            context['errors'] = form.errors.items()

        context['message']= 'Inscription en cours - Email envoyé'

    return render(request, 'connexion/inscription_producteur.html', context)
    




@transaction.atomic
def inscription_valider(request,id):
    context = {
        'title': 'Formulaire d\'inscription des producteurs',
        }
    
    connexion = Connexions.objects.filter(num_random=id,etat_connexion=False)

    if connexion.exists():
        producteurs = Producteurs.objects.create(nom=connexion.first().identifiant,
                                                photo='img_avatar.png',
                                                connexions_id=connexion.first().id,
                                                date_debut_id=1)
        producteurs.save()
        

        for item in connexion:
            item.etat_connexion=True
            item.save()

        context['form']= IdentificationProducteurForm()
        context['message']='Validation de votre inscription !! '

        return redirect('/connexion/')
    context['form']= IdentificationProducteurForm()

    return redirect('/connexion/')