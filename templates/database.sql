CREATE TABLE "tasks" (
	"id" SERIAL PRIMARY KEY,
	"task" VARCHAR(256),
	"status" BOOLEAN DEFAULT FALSE
	);
	
INSERT INTO "tasks" ("task") VALUES ('Complete weekend challenge');
INSERT INTO "tasks" ("task") VALUES ('Make Costco run');
INSERT INTO "tasks" ("task") VALUES ('Make Target run');
INSERT INTO "tasks" ("task") VALUES ('Grocery shop');
INSERT INTO "tasks" ("task") VALUES ('Clean kitchen');
INSERT INTO "tasks" ("task") VALUES ('Laundry');