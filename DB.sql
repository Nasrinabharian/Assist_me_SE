--------------------- person table -----------------------
create table person(
	person_id varchar(20),
	[name] varchar(30),
	family_name varchar(50),
	primary key(person_id)
);
--------------------- user table -------------------------
create table [user](
	[user_name] varchar(20),
	[password] varchar(20) not null,
	person_id varchar(20) not null,
	health_status int,
	location_x float,
	location_y float,
	primary key([user_name]),
	foreign key(person_id)
		references person(person_id)
		on delete cascade
);
--------------------- u_p_check --------------------------
create procedure u_p_check
@u_name   varchar(20),
@pass  varchar(20)
as
begin
	if exists(select * from [user] where [user_name] = @u_name
				and [password] = @pass)
		select 1;
	else
		select 0;
	
end;
--------------------- return_x_y -------------------------
create procedure return_x_y
as
begin
		select location_x, location_y, health_status from [user];
end;
--------------------- data -------------------------------
insert into person values('123', 'el', 'ra');
insert into person values('234', 'fa', 'fa');
insert into person values('345', 'na', 'ab');
insert into [user] values('er', '123', '123', 0, 700.642912, 350.649940);
insert into [user] values('ff', '123', '234', 1, 200.643346, 550.654349);
insert into [user] values('na', '123', '345', 0, 309.640644, 180.652794);
