from marketPlace.models import Connexions,Producteurs,RefMetier,Adresses
import random
import string


def proposition_identifiants(id_user):

 
    list_propal=[]
    digits = string.digits

    
    id_digits_1=''
    id_digits_2=''
    id_digits_date19=''
    id_digits_date20=''

    test=False
    while test==False:
        id_digits_1=id_user+'_'.join(random.choice(digits) for i in range(1))
        if not Connexions.objects.filter(identifiant=id_digits_1).exists():
            test=True

    test=False
    while test==False:
        id_digits_2=id_user+'_'+(''.join(random.choice(digits) for i in range(2)))
        if not Connexions.objects.filter(identifiant=id_digits_2).exists():
            test=True


    test=False
    while test==False:
        id_digits_date19=id_user+'_19'+(''.join(random.choice(digits) for i in range(2)))
        if not Connexions.objects.filter(identifiant=id_digits_date19).exists():
            test=True

    test=False
    while test==False:
        id_digits_date20=id_user+'_20'+(''.join(random.choice(digits) for i in range(2)))
        if not Connexions.objects.filter(identifiant=id_digits_date20).exists():
            test=True


    list_propal.append(id_digits_1)
    list_propal.append(id_digits_2)
    list_propal.append(id_digits_date19)
    list_propal.append(id_digits_date20)


    return list_propal
