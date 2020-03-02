
--- Insert ref_famille
INSERT INTO marketPlace.ref_famille(label) VALUES ('Fruits');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Légumes');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Poissons');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Fruits de mer');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Chacuteries');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Viandes');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Fromages');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Epicerie salée');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Epicerie sucrée');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Boissons');
INSERT INTO marketPlace.ref_famille(label) VALUES ('Plats traiteurs');

--- Insert ref_categorie
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Salade',2);
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Pommes de terre',2);
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Carotte',2);



--- Insert produits
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('Laitue',1);
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('Batavia',1);
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('Feuille de chêne',1);
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('Ambo',2);
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('BalmoraCarrl',2);
INSERT INTO marketPlace.produits(nom,categorie_id) VALUES ('Carrote Touchon',3);

--- Insert mise en vente
--- via la console admin

--- Insert ref_type_retrait 
INSERT INTO marketPlace.ref_type_retrait(label) VALUES('Sur le marché');
INSERT INTO marketPlace.ref_type_retrait(label) VALUES('Chez le producteur');

--- Insert ref_type_client
INSERT INTO marketPlace.ref_type_client(label) VALUES('Particulier');
INSERT INTO marketPlace.ref_type_client(label) VALUES('Professionnel');

--- Insert tickets
--- via la console admin

INSERT INTO marketPlace.avis(avis,note) VALUES('',0);

--- Insert adresse
INSERT INTO marketPlace.adresses(adresse,cp,ville) VALUES('A renseigner','-','-');
INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('place de la mairie','35410','Ossé',48.0463,-1.5044);
INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35410','Châteaugiron',48.0423764,-1.500912);

INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('place de la mairie','35113','Domagné',48.0706593,-1.3918429);
INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35150','Janzé',47.9556915,-1.495366);
INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35410','Domloup',48.0630976,-1.523711);

INSERT INTO marketPlace.adresses(adresse,cp,ville,latitude,longitude) VALUES('7 allé konrad','35410','Ossé',48.0630974,-1.523711);




--- Insert clients
INSERT INTO marketplace.clients(prenom,nom,type_client_id, num_telephone_portable, photo,adresse_id) 
    VALUES ('Arnaud','Jégoux', 1,null , null,6);





--- Insert ref_horaire
INSERT INTO marketPlace.ref_horaire(heure) VALUES('07:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('07:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('08:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('08:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('09:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('09:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('10:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('10:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('11:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('11:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('12:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('12:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('13:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('13:30');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('14:00');
INSERT INTO marketPlace.ref_horaire(heure) VALUES('14:30');


--- Insert manifestation
INSERT INTO marketPlace.ref_manifestation(label)VALUES ('Marché');
INSERT INTO marketPlace.ref_manifestation(label) VALUES ('Foire');
INSERT INTO marketPlace.ref_manifestation(label) VALUES ('Braderie');

--- Insert fréquence
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Quotidien');
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Hebdomadaire');
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Bi-mensuelle');
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Mensuelle');
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Trimestrielle');
INSERT INTO marketPlace.ref_frequence(label) VALUES ('Annuelle');


--- Insert ref_marche
INSERT INTO marketplace.marches( nom, photo, manifestation_id, frequence_id,heure_debut_id,heure_fin_id, adresse_id, nb_exposant, date_debut_id, date_fin_id)
    VALUES ('Ossé', null, 1, 1, 1, 13, 1, null, 1, null);
INSERT INTO marketplace.marches( nom, photo, manifestation_id, frequence_id,heure_debut_id,heure_fin_id, adresse_id, nb_exposant, date_debut_id, date_fin_id)
    VALUES ('Chateaugiron', null, 1, 1, 4, 15, 2, null, 1, null);


--- Insert ref_metier
INSERT INTO marketPlace.ref_metier(label) VALUES ('NR');
INSERT INTO marketPlace.ref_metier(label) VALUES ('Maraicher');
INSERT INTO marketPlace.ref_metier(label) VALUES ('Ostréculteur');
INSERT INTO marketPlace.ref_metier(label) VALUES ('Fromager');

--- Insert producteurs
INSERT INTO marketplace.producteurs(nom, photo, raison_social, num_siren, description, num_telephone_fix, num_telephone_portable, metier_id, adresse_id, date_debut_id, date_fin_id)
    VALUES ('Jean-Marc', null, null, null,  null,null, null, 1, 3, 1, null);
INSERT INTO marketplace.producteurs(nom, photo, raison_social, num_siren, description, num_telephone_fix, num_telephone_portable, metier_id, adresse_id, date_debut_id, date_fin_id)
    VALUES ('Gérard', null, null, null, 'Maraicher depuis 20 ans',null, null, 2, 4, 1, null);
INSERT INTO marketplace.producteurs(nom, photo, raison_social, num_siren,description, num_telephone_fix, num_telephone_portable, metier_id, adresse_id, date_debut_id, date_fin_id)
    VALUES ('Martine', null, null, null,  'Femme de philippe',null, null, 4, 5, 1, null);
INSERT INTO marketplace.producteurs(nom, photo, raison_social, num_siren,  description, num_telephone_fix, num_telephone_portable, metier_id, adresse_id, date_debut_id, date_fin_id)
    VALUES ('Philippe', null, null, null,  'Mari de philippe',null, null, 4, 5, 1, null);

--- Insert jour de la semaine
INSERT INTO marketPlace.ref_jours_semaine(jours)VALUES ('Lundi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Mardi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Mercredi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Jeudi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Vendredi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Samedi');
INSERT INTO marketPlace.ref_jours_semaine(jours) VALUES ('Dimanche');




--- Insert du calendrier
INSERT INTO marketPlace.calendrier (date_du_jour,date_f1,date_f2,date_YYYYMMDD,date_YYYYMM,date_YYYY,num_mois,nom_mois,nom_jour,
num_jour_semaine, num_jour_mois,num_jour_annee,num_semaine,dernier_jour_mois,weekend)
SELECT 
    datum AS date_du_jour,
    TO_CHAR(datum,'dd/mm/yyyy') AS date_f1,
    TO_CHAR(datum,'dd-mm-yyyy') AS date_f2,
    TO_CHAR(datum,'yyyymmdd')::INT AS date_YYYYMMDD,
    TO_CHAR(datum,'yyyymm') AS date_YYYYMM,
    TO_CHAR(datum,'yyyy')::INT AS date_YYYY,
    EXTRACT(MONTH FROM datum) AS num_mois,
    TO_CHAR(datum,'TMMonth') AS nom_mois,
    TO_CHAR(datum,'TMDay') AS nom_jour,
    EXTRACT(isodow FROM datum) AS num_jour_semaine,
    EXTRACT(DAY FROM datum) AS num_jour_mois,
    EXTRACT(doy FROM datum) AS num_jour_annee,
    EXTRACT(week FROM datum) AS num_semaine,
    (DATE_TRUNC('MONTH',datum) +INTERVAL '1 MONTH - 1 day')::DATE AS dernier_jour_mois,
    CASE
        WHEN EXTRACT(isodow FROM datum) IN (6,7) THEN TRUE
        ELSE FALSE
    END AS weekend
    FROM (SELECT '2020-01-01'::DATE+ SEQUENCE.DAY AS datum
      FROM GENERATE_SERIES (0,3650) AS SEQUENCE (DAY)
      GROUP BY SEQUENCE.DAY) DQ
ORDER BY 1;

