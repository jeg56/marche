
CREATE SEQUENCE marketPlace.type_retrait_id_seq;

CREATE TABLE marketPlace.type_retrait (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.type_retrait_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT type_retrait_pk PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.type_retrait.label IS 'Sur le marché ou chez le producteur';


ALTER SEQUENCE marketPlace.type_retrait_id_seq OWNED BY marketPlace.type_retrait.id;

CREATE SEQUENCE marketPlace.type_client_id_seq;

CREATE TABLE marketPlace.type_client (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.type_client_id_seq'),
                label VARCHAR(25) NOT NULL,
                CONSTRAINT type_client_pk PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.type_client.label IS 'type privé ou pros';


ALTER SEQUENCE marketPlace.type_client_id_seq OWNED BY marketPlace.type_client.id;

CREATE SEQUENCE marketPlace.adresse_id_seq;

CREATE TABLE marketPlace.adresse (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.adresse_id_seq'),
                adresse VARCHAR(255) NOT NULL,
                cp VARCHAR(6) NOT NULL,
                ville VARCHAR(255) NOT NULL,
                latitude REAL,
                longitude REAL,
                CONSTRAINT index_adresse_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.adresse_id_seq OWNED BY marketPlace.adresse.id;

CREATE SEQUENCE marketPlace.clients_id_seq;

CREATE TABLE marketPlace.clients (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.clients_id_seq'),
                nom VARCHAR(250) NOT NULL,
                mail VARCHAR(255) NOT NULL,
                type_client_id INTEGER NOT NULL,
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

CREATE SEQUENCE marketPlace.tickets_id_seq;

CREATE TABLE marketPlace.tickets (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.tickets_id_seq'),
                commande_id INTEGER NOT NULL,
                calendrier_id INTEGER NOT NULL,
                type_retrait_id INTEGER NOT NULL,
                adresse_id INTEGER NOT NULL,
                produit_id INTEGER NOT NULL,
                prix REAL NOT NULL,
                quantite INTEGER,
                poids INTEGER,
                CONSTRAINT index_tickets_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.tickets_id_seq OWNED BY marketPlace.tickets.id;

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

CREATE SEQUENCE marketPlace.horaire_id_seq;

CREATE TABLE marketPlace.horaire (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.horaire_id_seq'),
                heure VARCHAR(5) NOT NULL,
                CONSTRAINT index_horaire_id PRIMARY KEY (id)
);
COMMENT ON COLUMN marketPlace.horaire.heure IS 'au format HH:MM sous forme de liste';


ALTER SEQUENCE marketPlace.horaire_id_seq OWNED BY marketPlace.horaire.id;

CREATE SEQUENCE marketPlace.ref_categorie_id_seq;

CREATE TABLE marketPlace.ref_categorie (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_categorie_id_seq'),
                nom VARCHAR(50) NOT NULL,
                photo VARCHAR(255),
                CONSTRAINT id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_categorie_id_seq OWNED BY marketPlace.ref_categorie.id;

CREATE SEQUENCE marketPlace.ref_produits_id_seq;

CREATE TABLE marketPlace.ref_produits (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_produits_id_seq'),
                nom VARCHAR(255) NOT NULL,
                photo VARCHAR(2555),
                categorie_id INTEGER NOT NULL,
                CONSTRAINT index_ref_produits_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_produits_id_seq OWNED BY marketPlace.ref_produits.id;

CREATE SEQUENCE marketPlace.ref_marche_id_seq;

CREATE TABLE marketPlace.ref_marche (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.ref_marche_id_seq'),
                nom VARCHAR(255) NOT NULL,
                photo VARCHAR(255),
                heure_debut_id INTEGER NOT NULL,
                heure_fin_id INTEGER NOT NULL,
                adresse_id INTEGER NOT NULL,
                CONSTRAINT index_ref_marche_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.ref_marche_id_seq OWNED BY marketPlace.ref_marche.id;

CREATE SEQUENCE marketPlace.producteurs_id_seq;

CREATE TABLE marketPlace.producteurs (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.producteurs_id_seq'),
                nom VARCHAR(50) NOT NULL,
                photo VARCHAR(255),
                adresse_id INTEGER NOT NULL,
                CONSTRAINT index_producteur_id PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.producteurs_id_seq OWNED BY marketPlace.producteurs.id;

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

CREATE SEQUENCE marketPlace.a_lieu_id_seq;

CREATE TABLE marketPlace.a_lieu (
                id INTEGER NOT NULL DEFAULT nextval('marketPlace.a_lieu_id_seq'),
                calendrier_id INTEGER NOT NULL,
                ref_marche_id INTEGER NOT NULL,
                mise_en_vente_id INTEGER NOT NULL,
                CONSTRAINT a_lieu_pk PRIMARY KEY (id)
);


ALTER SEQUENCE marketPlace.a_lieu_id_seq OWNED BY marketPlace.a_lieu.id;

ALTER TABLE marketPlace.tickets ADD CONSTRAINT type_retrait_tickets_fk
FOREIGN KEY (type_retrait_id)
REFERENCES marketPlace.type_retrait (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.clients ADD CONSTRAINT type_client_clients_fk
FOREIGN KEY (type_client_id)
REFERENCES marketPlace.type_client (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.producteurs ADD CONSTRAINT adresse_producteurs_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresse (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.ref_marche ADD CONSTRAINT adresse_ref_marche_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresse (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.clients ADD CONSTRAINT adresse_clients_fk
FOREIGN KEY (adresse_id)
REFERENCES marketPlace.adresse (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
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

ALTER TABLE marketPlace.a_lieu ADD CONSTRAINT calendrier_a_lieu_fk
FOREIGN KEY (calendrier_id)
REFERENCES marketPlace.calendrier (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.ref_marche ADD CONSTRAINT refmarche_heure_debut
FOREIGN KEY (heure_debut_id)
REFERENCES marketPlace.horaire (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.ref_marche ADD CONSTRAINT refmarche_heure_fin
FOREIGN KEY (heure_fin_id)
REFERENCES marketPlace.horaire (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.ref_produits ADD CONSTRAINT ref_categorie_ref_produits_fk
FOREIGN KEY (categorie_id)
REFERENCES marketPlace.ref_categorie (id)
ON DELETE CASCADE
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.mise_en_vente ADD CONSTRAINT ref_produits_mise_en_vente_fk
FOREIGN KEY (produit_id)
REFERENCES marketPlace.ref_produits (id)
ON DELETE NO ACTION
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.a_lieu ADD CONSTRAINT ref_marche_a_lieu_fk
FOREIGN KEY (ref_marche_id)
REFERENCES marketPlace.ref_marche (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE marketPlace.mise_en_vente ADD CONSTRAINT producteurs_mise_en_vente_fk
FOREIGN KEY (producteur_id)
REFERENCES marketPlace.producteurs (id)
ON DELETE NO ACTION
ON UPDATE CASCADE
NOT DEFERRABLE;

ALTER TABLE marketPlace.a_lieu ADD CONSTRAINT mise_en_vente_a_lieu_fk
FOREIGN KEY (mise_en_vente_id)
REFERENCES marketPlace.mise_en_vente (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
