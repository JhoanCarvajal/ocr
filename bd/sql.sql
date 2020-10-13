CREATE TABLE restaurantes (
  id INT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  direccion VARCHAR(99) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `frisby`.`facturas`
-- -----------------------------------------------------
CREATE TABLE facturas (
  id INT NOT NULL,
  id_factura INT NOT NULL,
  lectura_actual INT NOT NULL,
  lectura_anterior INT NOT NULL,
  consumo INT NOT NULL,
  vertimiento INT NOT NULL,
  total_pagar INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_resta_fact_idx (id_factura ASC) VISIBLE,
  CONSTRAINT fk_resta_fact
    FOREIGN KEY (id_factura)
    REFERENCES restaurantes (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
