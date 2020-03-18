ALTER TABLE communes ADD selected_text TEXT;
ALTER TABLE Adresses ADD commune integer;
CREATE INDEX index_communes_cp ON communes (cp);
CREATE INDEX index_ville_cp ON communes (ville);