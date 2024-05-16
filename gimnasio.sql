CREATE TABLE IF NOT EXISTS `Cliente` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`apellidos` INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `Pago` (
	`id` integer primary key NOT NULL UNIQUE,
	`fecha` REAL NOT NULL,
	`monto` REAL NOT NULL,
	`cliente_id` INTEGER NOT NULL,
FOREIGN KEY(`cliente_id`) REFERENCES `Cliente`(`id`)
);
CREATE TABLE IF NOT EXISTS `Suscripción` (
	`id` integer primary key NOT NULL UNIQUE,
	`tipo` TEXT NOT NULL,
	`precio` REAL NOT NULL,
	`inicio` REAL NOT NULL,
	`fin` REAL NOT NULL,
	`cliente_id` INTEGER NOT NULL,
FOREIGN KEY(`cliente_id`) REFERENCES `Cliente`(`id`)
);

FOREIGN KEY(`cliente_id`) REFERENCES `Cliente`(`id`)
FOREIGN KEY(`cliente_id`) REFERENCES `Cliente`(`id`)