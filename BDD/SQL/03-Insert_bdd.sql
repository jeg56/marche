--- Insert ref_categorie
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Salade',2);
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Pommes de terre',2);
INSERT INTO marketPlace.ref_categorie(label,famille_id) VALUES ('Carotte',2);

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


--- Insert ref_produits
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('Laitue',1);
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('Batavia',1);
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('Feuille de chêne',1);
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('Ambo',2);
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('BalmoraCarrl',2);
INSERT INTO marketPlace.ref_produits(nom,categorie_id) VALUES ('Carrote Touchon',3);

--- Insert type_retrait 
INSERT INTO marketPlace.type_retrait(label) VALUES('Sur le marché');
INSERT INTO marketPlace.type_retrait(label) VALUES('Chez le producteur');

--- Insert type_client
INSERT INTO marketPlace.type_client(label) VALUES('Particulier');
INSERT INTO marketPlace.type_client(label) VALUES('Professionnel');

--- Insert tikets
--- via la console admin

--- Insert adresse
INSERT INTO marketPlace.adresse(adresse,cp,ville,latitude,longitude) VALUES('place de la mairie','35410','Ossé',48.0463,-1.5044);
INSERT INTO marketPlace.adresse(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35410','Châteaugiron',48.0423764,-1.500912);

INSERT INTO marketPlace.adresse(adresse,cp,ville,latitude,longitude) VALUES('place de la mairie','35113','Domagné',48.0706593,-1.3918429);
INSERT INTO marketPlace.adresse(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35150','Janzé',47.9556915,-1.495366);
INSERT INTO marketPlace.adresse(adresse,cp,ville,latitude,longitude) VALUES('place des halles','35410','Domloup',48.0630976,-1.523711);



--- Insert horaire
INSERT INTO marketPlace.horaire(heure) VALUES('07:00');
INSERT INTO marketPlace.horaire(heure) VALUES('07:30');
INSERT INTO marketPlace.horaire(heure) VALUES('08:00');
INSERT INTO marketPlace.horaire(heure) VALUES('08:30');
INSERT INTO marketPlace.horaire(heure) VALUES('09:00');
INSERT INTO marketPlace.horaire(heure) VALUES('09:30');
INSERT INTO marketPlace.horaire(heure) VALUES('10:00');
INSERT INTO marketPlace.horaire(heure) VALUES('10:30');
INSERT INTO marketPlace.horaire(heure) VALUES('11:00');
INSERT INTO marketPlace.horaire(heure) VALUES('11:30');
INSERT INTO marketPlace.horaire(heure) VALUES('12:00');
INSERT INTO marketPlace.horaire(heure) VALUES('12:30');
INSERT INTO marketPlace.horaire(heure) VALUES('13:00');
INSERT INTO marketPlace.horaire(heure) VALUES('13:30');
INSERT INTO marketPlace.horaire(heure) VALUES('14:00');
INSERT INTO marketPlace.horaire(heure) VALUES('14:30');



--- Insert ref_marche
INSERT INTO marketPlace.ref_marche(nom,heure_debut_id,heure_fin_id,adresse_id) VALUES('Ossé',1,13,1);
INSERT INTO marketPlace.ref_marche(nom,heure_debut_id,heure_fin_id,adresse_id) VALUES('Chateaugiron',4,15,2);


--- Insert producteurs
INSERT INTO marketPlace.producteurs(nom,adresse_id) VALUES ('Jean-Marc',3);
INSERT INTO marketPlace.producteurs(nom,adresse_id) VALUES ('Gérard',4);
INSERT INTO marketPlace.producteurs(nom,adresse_id) VALUES ('Michel',5);

--- Insert jour de la semaine
INSERT INTO marketPlace.jours_semaine(jours)VALUES ('Lundi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Mardi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Mercredi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Jeudi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Vendredi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Samedi');
INSERT INTO marketPlace.jours_semaine(jours) VALUES ('Dimanche');

--- Insert fréquence
INSERT INTO marketPlace.frequence(label) VALUES ('Quotidien');
INSERT INTO marketPlace.frequence(label) VALUES ('Hebdomadaire');
INSERT INTO marketPlace.frequence(label) VALUES ('Bi-mensuelle');
INSERT INTO marketPlace.frequence(label) VALUES ('Mensuelle');
INSERT INTO marketPlace.frequence(label) VALUES ('Trimestrielle');
INSERT INTO marketPlace.frequence(label) VALUES ('Annuelle');



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

--- Insert manifestation
INSERT INTO marketPlace.manifestation(label)VALUES ('Marché');
INSERT INTO marketPlace.manifestation(label) VALUES ('Foire');
INSERT INTO marketPlace.manifestation(label) VALUES ('Braderie');