

-- 12-2-2016 --
-- test table created to test some psql triggers
create table test_logs_movies_action_type (
	id int PRIMARY KEY not null default NULL, 
	row_id int not null, 
	action_text text not null 
);

-- Trigger, #1
create trigger movies_row_updated AFTER UPDATE on ajency_movies FOR EACH ROW EXECUTE PROCEDURE proc_movies_updated();

-- Function to run on Trigger #1
create or replace function proc_movies_updated() RETURNS trigger as $$ 
	BEGIN 
		INSERT INTO test_logs_movies_action_type( row_id, action_text) VALUES( OLD.id, NEW.title);
		RETURN NEW;
	END;
$$ LANGUAGE plpgsql;

-- 
create sequence test_logs_movies_action_type_id_seq;

-- but this deleted already existing data in table, the set default, or maybe it does not delete
alter table test_logs_movies_action_type alter id set default nextval('test_logs_movies_action_type_id_seq');


