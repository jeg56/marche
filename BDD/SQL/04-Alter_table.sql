ALTER TABLE communes ADD selected_text TEXT;
ALTER TABLE Adresses ADD commune integer;
CREATE INDEX index_communes_cp ON communes (cp);
CREATE INDEX index_ville_cp ON communes (ville);

ALTER TABLE mise_en_vente ADD ordre_affichage integer;
ALTER TABLE mise_en_vente  alter column ordre_affichage set not null;
