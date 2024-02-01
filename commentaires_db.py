# CREATE DATABASE store;

# USE store;

# CREATE TABLE category(
# id INT PRIMARY KEY AUTO_INCREMENT,
# name VARCHAR(255)
# );

# CREATE TABLE product(
# id INT PRIMARY KEY AUTO_INCREMENT,
# name VARCHAR(255),
# description TEXT,
# price INT,
# quantity INT,
# id_category INT
# );

# INSERT INTO category (id, name) VALUES (1, 'Clubs');

# INSERT INTO category (id, name) VALUES (2, 'Accessoires');

# INSERT INTO category (id, name) VALUES (3, 'Vêtements');


# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (1, 'Driver AIR X Driver', 'Grâce aux dernières innovations de la marque, les drivers AIR X de chez Cobra offrent aux joueurs une légèreté incomparable pour des swings plus rapides et plus fluides.', 199, 30, 1);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (2, 'Hybride D300 SL Hybrid', 'Bénéficiez de tolérance et d’une vitesse de swing boostée grâce au design aérodynamique de la tête de cet hybride Wilson D300 SL dont la légèreté vous permettra d’augmenter la distance de vos coups.', 72, 50, 1);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (3, 'Serie de fers King F9-S Irons', 'Les fers Cobra King F9-S Irons sont dotés de la technologie Speedback favorisant la stabilité et la tolérance. Les hosels sont optimisés selon les clubs afin de promouvoir le contrôle et générer les bonnes trajectoires. ', 430, 250, 1);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (4, 'Balles neuves ERC Soft', 'Les balles Callaway ERC Soft White Triple Track sont dotées de repères d’alignement Triple Track Dagger facilitant le putting. Elles offrent un excellent toucher et beaucoup de contrôle sans sacrifier la distance.', 50, 100, 2);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (5, 'Tees Bamboo Tees White', 'Les Masters Golf Bamboo Tees White sont des tees de golf biodégradables et résistants, fabriqués à partir de bambou durable.', 3, 90, 2);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (6, 'Releve-pitch Stealth Pitch Repairer', 'Le Stealth Pitch Repairer Silver de monsieurgolf est l''outil idéal pour restaurer impeccablement le green après chaque coup de balle.', 15, 60, 2);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (7, 'Polo Women''s Gamer Shortsleeves', 'Fabriqué dans une matière synthétique à 100 % polyester, le polo golf femme Puma Women''s Gamer Shortsleeves est un modèle sans manches qui offre une totale liberté de mouvement.', 18, 40, 3);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (8, 'Polo Icon Golf Polo', 'Le polo Puma Icon Golf est à la fois très chic et confortable pour briller facilement sur le parcours. Il évacue très bien l''humidité pour rester au sec toute la journée.', 25, 50, 3);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (9, 'Pantacourt Chie Capri', 'Fabriqué à partir de matériaux hautement respirants et extensibles, le pantacourt Chie Capri de la marque Röhnisch est incomparable de confort, offrant à vos mouvements une très grande liberté de mouvement.', 43, 20, 3);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (10, 'Pantalon Dealer TLD', 'Confectionné à partir d''un tissu extensible, respirant et qui évacue l''humidité, le pantalon de golf Puma Golf Dealer TLD White Glow garantit un maximum de confort durant des longues périodes de jeu.', 72, 30, 3);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (11, 'Chaussures avec crampons Traditions Women', 'Grâce à la membrane imperméable dont bénéficie la chaussure de golf femme Footjoy Traditions Women White, vos pieds restent au sec et sont soutenus confortablement dans une tige en cuir véritable.', 134, 20, 3);

# INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (12, 'Chaussures sans crampons Biom Hybrid 3', 'Capable de préserver vos pieds de l''humidité s''il y a de la rosée ou s''il pleut légèrement, la chaussure golf déperlante Ecco Biom Hybrid 3 rime aussi avec confort de jeu.', 129, 40, 3);