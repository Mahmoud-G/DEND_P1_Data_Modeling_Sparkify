# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays;"
user_table_drop = "DROP table IF EXISTS users;"
song_table_drop = "DROP table IF EXISTS songs;"
artist_table_drop = "DROP table IF EXISTS artists;"
time_table_drop = "DROP table IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time timestamptz, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar UNIQUE NOT NULL, title varchar, artist_id varchar, year int, duration numeric);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id varchar UNIQUE NOT NULL, name varchar,  location varchar, latitude decimal, longitude decimal);

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamptz, hour int, day int, week int, month int, year int, weekday varchar);

""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
                 VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (user_id) 
                        DO UPDATE SET (first_name, last_name, gender, level) = (EXCLUDED.first_name, EXCLUDED.last_name, EXCLUDED.gender, EXCLUDED.level);

""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (song_id) 
                        DO UPDATE SET (title, artist_id, year, duration) = (EXCLUDED.title, EXCLUDED.artist_id, EXCLUDED.year, EXCLUDED.duration);
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (artist_id) 
                        DO UPDATE SET (name, location, latitude, longitude) = (EXCLUDED.name, EXCLUDED.location, EXCLUDED.latitude, EXCLUDED.longitude);
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                 VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS
# based on the title, artist name, and duration of a song
song_select = ("""
SELECT
    sng.song_id,
    sng.artist_id 
FROM
    artists as art
    JOIN songs as sng ON art.artist_id = sng.artist_id 
WHERE
    sng.title = %s
    AND art.name = %s
    AND sng.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]