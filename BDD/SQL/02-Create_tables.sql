CREATE SEQUENCE marketPlace.communes_id_seq;

CREATE TABLE marketPlace.communes (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.communes_id_seq'),
                cp VARCHAR(5) NOT NULL,
                ville VARCHAR(255) NOT NULL,
                latitude REAL,
                longitude REAL,
                CONSTRAINT index_communes_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.communes_id_seq OWNED BY marketPlace.communes.id;


CREATE SEQUENCE marketPlace.connexions_id_seq;

CREATE TABLE marketPlace.connexions (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.connexions_id_seq'),
                identifiant VARCHAR(25) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                opt_in INTEGER DEFAULT 1 NOT NULL,
                num_random VARCHAR(20) NOT NULL,
                etat_connexion BOOLEAN DEFAULT false NOT NULL,
                CONSTRAINT index_connexions_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.connexions_id_seq OWNED BY marketPlace.connexions.id;

CREATE SEQUENCE marketPlace.ref_metier_id_seq;

CREATE TABLE marketPlace.ref_metier (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_metier_id_seq'),
                label VARCHAR(50) NOT NULL,
                CONSTRAINT ref_metier_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_metier_id_seq OWNED BY marketPlace.ref_metier.id;

CREATE SEQUENCE marketPlace.avis_id_seq;

CREATE TABLE marketPlace.avis (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.avis_id_seq'),
                avis VARCHAR(255),
                note INTEGER NOT NULL,
                CONSTRAINT index_avis_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.avis_id_seq OWNED BY marketPlace.avis.id;

CREATE SEQUENCE marketPlace.ref_famille_id_seq;

CREATE TABLE marketPlace.ref_famille (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_famille_id_seq'),
                label VARCHAR(255) NOT NULL,
                CONSTRAINT ref_famille_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_famille_id_seq OWNED BY marketPlace.ref_famille.id;

CREATE SEQUENCE marketPlace.ref_frequence_id_seq;

CREATE TABLE marketPlace.ref_frequence (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_frequence_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT ref_frequence_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_frequence_id_seq OWNED BY marketPlace.ref_frequence.id;

CREATE SEQUENCE marketPlace.ref_manifestation_id_seq;

CREATE TABLE marketPlace.ref_manifestation (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_manifestation_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT ref_manifestation_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_manifestation_id_seq OWNED BY marketPlace.ref_manifestation.id;

CREATE SEQUENCE marketPlace.ref_jours_semaine_id_seq;

CREATE TABLE marketPlace.ref_jours_semaine (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_jours_semaine_id_seq'),
                jours VARCHAR(15) NOT NULL,
                CONSTRAINT ref_jours_semaine_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_jours_semaine_id_seq OWNED BY marketPlace.ref_jours_semaine.id;

CREATE SEQUENCE marketPlace.ref_type_retrait_id_seq;

CREATE TABLE marketPlace.ref_type_retrait (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_type_retrait_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT ref_type_retrait_pk PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.ref_type_retrait.label IS 'Sur le marché ou chez le producteur';


ALTER SEQUENCE marketPlace.ref_type_retrait_id_seq OWNED BY marketPlace.ref_type_retrait.id;

CREATE SEQUENCE marketPlace.ref_type_client_id_seq;

CREATE TABLE marketPlace.ref_type_client (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_type_client_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT ref_type_client_pk PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.ref_type_client.label IS 'type privé ou pros';


ALTER SEQUENCE marketPlace.ref_type_client_id_seq OWNED BY marketPlace.ref_type_client.id;

CREATE SEQUENCE marketPlace.adresses_id_seq;

CREATE TABLE marketPlace.adresses (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.adresses_id_seq'),
                adresse VARCHAR(255) NOT NULL,
                cp VARCHAR(6) NOT NULL,
                ville VARCHAR(255) NOT NULL,
                latitude REAL,
                longitude REAL,
                CONSTRAINT index_adresse_id PRIMARY KEY (id)
);

CREATE INDEX index_adresses_adresse ON marketPlace.adresses (adresse);
CREATE INDEX index_adresses_cp ON marketPlace.adresses (cp);
CREATE INDEX index_adresses_ville ON marketPlace.adresses (ville);

ALTER SEQUENCE marketPlace.adresses_id_seq OWNED BY marketPlace.adresses.id;

CREATE SEQUENCE marketPlace.clients_id_seq;

CREATE TABLE marketPlace.clients (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.clients_id_seq'),
                nom VARCHAR(255) NOT NULL,
                prenom VARCHAR(255) NOT NULL,
                connexion_id INTEGER,
                type_client_id INTEGER NOT NULL,
                num_telephone_portable VARCHAR(10),
                photo VARCHAR(255),
                adresse_id INTEGER NOT NULL,
                CONSTRAINT index_clients_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.clients_id_seq OWNED BY marketPlace.clients.id;

CREATE SEQUENCE marketPlace.commande_id_seq;

CREATE TABLE marketPlace.commande (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.commande_id_seq'),
                client_id INTEGER NOT NULL,
                montant REAL NOT NULL,
                CONSTRAINT index_commande_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.commande_id_seq OWNED BY marketPlace.commande.id;

CREATE TABLE marketPlace.tickets (
                id INTEGER NOT NULL,
                commande_id INTEGER NOT NULL,
                calendrier_id INTEGER NOT NULL,
                type_retrait_id INTEGER NOT NULL,
                adresse_id INTEGER NOT NULL,
                produit_id INTEGER NOT NULL,
                prix REAL NOT NULL,
                quantite INTEGER,
                poids INTEGER,
                avis_id INTEGER DEFAULT 1 NOT NULL,
                CONSTRAINT index_tickets_id PRIMARY KEY (id)
);


CREATE SEQUENCE marketPlace.calendrier_id_seq;

CREATE TABLE marketPlace.calendrier (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.calendrier_id_seq'),
                date_du_jour DATE NOT NULL,
                date_f1 VARCHAR(10) NOT NULL,
                date_f2 VARCHAR(10) NOT NULL,
                date_YYYYMM VARCHAR(6) NOT NULL,
                date_YYYYMMDD VARCHAR(8) NOT NULL,
                date_YYYY VARCHAR(4) NOT NULL,
                num_mois INTEGER NOT NULL,
                nom_mois VARCHAR(20) NOT NULL,
                nom_jour VARCHAR(20) NOT NULL,
                num_jour_semaine INTEGER NOT NULL,
                num_jour_mois INTEGER NOT NULL,
                num_jour_annee INTEGER NOT NULL,
                num_semaine INTEGER NOT NULL,
                dernier_jour_mois DATE NOT NULL,
                weekend BOOLEAN NOT NULL,
                CONSTRAINT index_calendrier_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.calendrier_id_seq OWNED BY marketPlace.calendrier.id;

CREATE SEQUENCE marketPlace.ref_horaire_id_seq;

CREATE TABLE marketPlace.ref_horaire (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_horaire_id_seq'),
                heure VARCHAR(5) NOT NULL,
                CONSTRAINT index_horaire_id PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.ref_horaire.heure IS 'au format HH:MM sous forme de liste';


ALTER SEQUENCE marketPlace.ref_horaire_id_seq OWNED BY marketPlace.ref_horaire.id;

CREATE SEQUENCE marketPlace.ref_categorie_id_seq;

CREATE TABLE marketPlace.ref_categorie (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_categorie_id_seq'),
                label VARCHAR(50) NOT NULL,
                photo VARCHAR(255),
                famille_id INTEGER NOT NULL,
                CONSTRAINT index_ref_categorieiid PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_categorie_id_seq OWNED BY marketPlace.ref_categorie.id;

CREATE SEQUENCE marketPlace.produits_id_seq;

CREATE TABLE marketPlace.produits (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.produits_id_seq'),
                nom VARCHAR(255) NOT NULL,
                photo VARCHAR(255),
                categorie_id INTEGER NOT NULL,
                CONSTRAINT index_ref_produits_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.produits_id_seq OWNED BY marketPlace.produits.id;

CREATE SEQUENCE marketPlace.marches_id_seq;

CREATE TABLE marketPlace.marches (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.marches_id_seq'),
                nom VARCHAR(255) NOT NULL,
                photo VARCHAR(255),
                manifestation_id INTEGER NOT NULL,
                frequence_id INTEGER NOT NULL,
                heure_debut_id INTEGER NOT NULL,
                heure_fin_id INTEGER NOT NULL,
                adresse_id INTEGER NOT NULL,
                nb_exposant INTEGER,
                date_debut_id INTEGER NOT NULL,
                date_fin_id INTEGER,
                CONSTRAINT index_marche_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.marches_id_seq OWNED BY marketPlace.marches.id;

CREATE TABLE marketPlace.jour_marche (
                id INTEGER NOT NULL,
                ref_marche_id INTEGER NOT NULL,
                jours_semaine_id INTEGER NOT NULL,
                CONSTRAINT index_jour_marche_id PRIMARY KEY (id)
);


CREATE SEQUENCE marketPlace.producteurs_id_seq;

CREATE TABLE marketPlace.producteurs (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.producteurs_id_seq'),
                nom VARCHAR(50) NOT NULL,
                photo VARCHAR(255),
                raison_social VARCHAR(9),
                num_siren VARCHAR(15),
                connexions_id INTEGER,
                description VARCHAR(255),
                num_telephone_fix VARCHAR(10),
                num_telephone_portable VARCHAR(10),
                metier_id INTEGER DEFAULT 1 NOT NULL,
                adresse_id INTEGER NOT NULL,
                date_debut_id INTEGER NOT NULL,
                date_fin_id INTEGER,
                CONSTRAINT index_producteur_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.producteurs_id_seq OWNED BY marketPlace.producteurs.id;

CREATE TABLE marketPlace.sederouler (
                id INTEGER NOT NULL,
                ref_marche_id INTEGER NOT NULL,
                date_marche_id INTEGER NOT NULL,
                producteur_id INTEGER NOT NULL,
                CONSTRAINT sederouler_pk PRIMARY KEY (id)
);


CREATE SEQUENCE marketPlace.mise_en_vente_id_seq;

CREATE TABLE marketPlace.mise_en_vente (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.mise_en_vente_id_seq'),
                produit_id INTEGER NOT NULL,
                producteur_id INTEGER NOT NULL,
                prix NUMERIC(2) NOT NULL,
                quantite_stock INTEGER,
                poids_stock INTEGER,
                quantite_vendu INTEGER,
                poids_vendu INTEGER,
                etat_stock BOOLEAN DEFAULT True NOT NULL,
                CONSTRAINT index_mise_en_vente_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.mise_en_vente_id_seq OWNED BY marketPlace.mise_en_vente.id;

ALTER TABLE marketPlace.producteurs ADD CONSTRAINT connexions_producteurs_fk
FOREIGN KEY (connexions_id)
REFERENCES marketPlace.connexions (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.clients ADD CONSTRAINT connexions_clients_fk
FOREIGN KEY (connexion_id)
REFERENCES marketPlace.connexions (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.producteurs ADD CONSTRAINT ref_metier_producteurs_fk
FOREIGN KEY (metier_id)
REFERENCES marketPlace.ref_metier (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.tickets ADD CONSTRAINT avis_tickets_fk
FOREIGN KEY (avis_id)
REFERENCES marketPlace.avis (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.ref_categorie ADD CONSTRAINT famille_ref_categorie_fk
FOREIGN KEY (famille_id)
REFERENCES marketPlace.ref_famille (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.marches ADD CONSTRAINT frequence_ref_marche_fk
FOREIGN KEY (frequence_id)
REFERENCES marketPlace.ref_frequence (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.marches ADD CONSTRAINT manifestation_ref_marche_fk
FOREIGN KEY (manifestation_id)
REFERENCES marketPlace.ref_manifestation (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.jour_marche ADD CONSTRAINT ref_jours_semaine_jour_marche_fk
FOREIGN KEY (jours_semaine_id)
REFERENCES marketPlace.ref_jours_semaine (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.tickets ADD CONSTRAINT type_retrait_tickets_fk
FOREIGN KEY (type_retrait_id)
REFERENCES marketPlace.ref_type_retrait (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.clients ADD CONSTRAINT type_client_clients_fk
FOREIGN KEY (type_client_id)
REFERENCES marketPlace.ref_type_client (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.clients ADD CONSTRAINT adresse_clients_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresses (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.producteurs ADD CONSTRAINT adresse_producteurs_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresses (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.marches ADD CONSTRAINT adresse_ref_marche_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresses (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.commande ADD CONSTRAINT clients_commande_fk
FOREIGN KEY (client_id)
REFERENCES marketPlace.clients (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.tickets ADD CONSTRAINT commande_tickets_fk
FOREIGN KEY (commande_id)
REFERENCES marketPlace.commande (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.marches ADD CONSTRAINT refmarche_heure_debut
FOREIGN KEY (heure_debut_id)
REFERENCES marketPlace.ref_horaire (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.marches ADD CONSTRAINT refmarche_heure_fin
FOREIGN KEY (heure_fin_id)
REFERENCES marketPlace.ref_horaire (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.produits ADD CONSTRAINT ref_categorie_ref_produits_fk
FOREIGN KEY (categorie_id)
REFERENCES marketPlace.ref_categorie (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.mise_en_vente ADD CONSTRAINT ref_produits_mise_en_vente_fk
FOREIGN KEY (produit_id)
REFERENCES marketPlace.produits (id)
ON DELETE NO ACTION
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.sederouler ADD CONSTRAINT ref_marche_a_lieu_fk
FOREIGN KEY (ref_marche_id)
REFERENCES marketPlace.marches (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.jour_marche ADD CONSTRAINT frequence_marche_ref_marche_fk
FOREIGN KEY (ref_marche_id)
REFERENCES marketPlace.marches (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.mise_en_vente ADD CONSTRAINT producteurs_mise_en_vente_fk
FOREIGN KEY (producteur_id)
REFERENCES marketPlace.producteurs (id)
ON DELETE NO ACTION
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.sederouler ADD CONSTRAINT producteurs_sederouler_fk
FOREIGN KEY (producteur_id)
REFERENCES marketPlace.producteurs (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
