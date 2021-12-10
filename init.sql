-- create table Holiday
create table "Holiday" (
	"id" smallserial not null, 
	"name" varchar(255) not null, 
	"date" date not null, 
	"createdAt" timestamptz not null default CURRENT_TIMESTAMP, 
	"updatedAt" timestamptz not null default CURRENT_TIMESTAMP
);

-- create primary key on table Holiday
alter table "Holiday" add constraint "Holiday_pkey" primary key ("id");

-- create index on Holiday.date
create index "holiday_date_index" on "Holiday" ("date");

-- insert german national holidays
insert into "Holiday" ("name", "date") VALUES ('New Year''s Day', '2021-01-01');
insert into "Holiday" ("name", "date") VALUES ('Good Friday', '2021-04-02');
insert into "Holiday" ("name", "date") VALUES ('Easter Monday', '2021-04-05');
insert into "Holiday" ("name", "date") VALUES ('Labour Day', '2021-05-01');
insert into "Holiday" ("name", "date") VALUES ('Ascension Day', '2021-05-13');
insert into "Holiday" ("name", "date") VALUES ('Whit Monday', '2021-05-24');
insert into "Holiday" ("name", "date") VALUES ('Day of German Unity', '2021-10-03');
insert into "Holiday" ("name", "date") VALUES ('Christmas Day', '2021-12-25');
insert into "Holiday" ("name", "date") VALUES ('2nd Day of Christmas', '2021-12-26');
insert into "Holiday" ("name", "date") VALUES ('New Year''s Day', '2022-01-01');

-- read inserted data
select * from "Holiday";
