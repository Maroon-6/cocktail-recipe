USE cocktails;

DROP TABLE IF EXISTS recipes;
CREATE TABLE `cocktails`.`recipes` (
  `recipe_name` VARCHAR(45) NOT NULL,
  `description` TINYTEXT NULL,
  `contributor` VARCHAR(45) NULL,
  PRIMARY KEY (`recipe_name`),
  UNIQUE INDEX `recipe_name_UNIQUE` (`recipe_name` ASC) VISIBLE);

-- INSERT INTO recipes VALUES ("Negroni", "Terry's favorite cocktail", "Terry");
-- INSERT INTO recipes VALUES ("Mojito", "I love mint", "Terry");

DROP TABLE IF EXISTS ingredients;
CREATE TABLE `ingredients` (
  `ingredient_name` varchar(45) NOT NULL,
  PRIMARY KEY (`ingredient_name`),
  UNIQUE KEY `ingredients_ingredient_name_uindex` (`ingredient_name`)
);

-- INSERT INTO ingredients VALUES ("gin");
-- INSERT INTO ingredients VALUES ("campari");
-- INSERT INTO ingredients VALUES ("sweet vermouth");
-- INSERT INTO ingredients VALUES ("rum");
-- INSERT INTO ingredients VALUES ("mint leaves");
-- INSERT INTO ingredients VALUES ("mint sprig");
-- INSERT INTO ingredients VALUES ("simple syrup");
-- INSERT INTO ingredients VALUES ("lime juice");
-- INSERT INTO ingredients VALUES ("lime wheel");
-- INSERT INTO ingredients VALUES ("orange peel");
-- INSERT INTO ingredients VALUES ("soda");

DROP TABLE IF EXISTS units;
CREATE TABLE `units` (
  `unit_name` varchar(20) NOT NULL,
  PRIMARY KEY (`unit_name`),
  UNIQUE KEY `units_unit_name_uindex` (`unit_name`)
);

-- INSERT INTO units VALUES ("ounce");
-- INSERT INTO units VALUES ("fluid ounce");
-- INSERT INTO units VALUES ("L");
-- INSERT INTO units VALUES("ml");

DROP TABLE IF EXISTS recipe_ingredients;
CREATE TABLE `cocktails`.`recipe_ingredients` (
  `recipe` VARCHAR(45) NOT NULL,
  `ingredient` VARCHAR(45) NOT NULL,
  `quantity` VARCHAR(20) NULL,
  `unit` VARCHAR(20) NULL,
  `garnish` TINYINT NOT NULL,
  INDEX `ri_ingredient_idx` (`ingredient` ASC) VISIBLE,
  INDEX `ri_unit_idx` (`unit` ASC) VISIBLE,
  CONSTRAINT `ri_recipe`
    FOREIGN KEY (`recipe`)
    REFERENCES `cocktails`.`recipes` (`recipe_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `ri_ingredient`
    FOREIGN KEY (`ingredient`)
    REFERENCES `cocktails`.`ingredients` (`ingredient_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `ri_unit`
    FOREIGN KEY (`unit`)
    REFERENCES `cocktails`.`units` (`unit_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- INSERT INTO recipe_ingredients VALUES ("Negroni", "gin", "1", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Negroni", "campari", "1", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Negroni", "sweet vermouth", "1", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Negroni", "orange peel", null, null, 1);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "rum", "2", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "simple syrup", "1/2", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "lime juice", "3/4", "ounce", 0);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "mint leaves", "3", null, 0);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "soda", null, null, 0);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "mint sprig", null, null, 1);
-- INSERT INTO recipe_ingredients VALUES ("Mojito", "lime wheel", null, null, 1);

DROP TABLE IF EXISTS inventories;
CREATE TABLE `cocktails`.`inventories` (
  `inventory_id` INT NOT NULL,
  `inventory_name` VARCHAR(45) NULL,
  `ingredient_name` VARCHAR(45) NULL,
  `brand` VARCHAR(45) NULL,
  `measurement_qty` FLOAT NULL,
  `unit` VARCHAR(20) NULL,
  `abv` VARCHAR(8) NULL,
  `in_stock` INT NULL,
  `price` FLOAT NULL,
  PRIMARY KEY (`inventory_id`),
  INDEX `inventory_ingredient_idx` (`ingredient_name` ASC) VISIBLE,
  INDEX `inventory_unit_idx` (`unit` ASC) VISIBLE,
  CONSTRAINT `inventory_ingredient`
    FOREIGN KEY (`ingredient_name`)
    REFERENCES `cocktails`.`ingredients` (`ingredient_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `inventory_unit`
    FOREIGN KEY (`unit`)
    REFERENCES `cocktails`.`units` (`unit_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
-- INSERT INTO inventories
-- VALUES (1, "Absolut Vodka", "vodka", "Absolut", 1.75, "L", "40%", 1000, "29.99");
-- INSERT INTO inventories
-- VALUES (2, "Grey Goose Vodka", "vodka", "Grey Goose", 750, "ml", "40%", 800, "24.99");

