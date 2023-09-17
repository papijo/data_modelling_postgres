# Drop Table Queries

# Fact Table
songplays_table_drop = "DROP TABLE IF EXISTS songplays"

# Dimension Tables
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# Create Tables
# users table
users_table_create = """
    CREATE TABLE IF NOT EXISTS users
    (
        user_id int PRIMARY KEY, 
        first_name text NOT NULL, 
        last_name text NOT NULL, 
        gender text, 
        level text
    )
"""

# songs table
songs_table_create = """
    CREATE TABLE IF NOT EXISTS songs
    (
        song_id text PRIMARY KEY, 
        title text NOT NULL, 
        artist_id text NOT NULL, 
        year int, 
        duration float NOT NULL
    )
"""

#
artists_table_create = """
    CREATE TABLE IF NOT EXISTS artists
    (
        artist_id text PRIMARY KEY,
        name text NOT NULL, 
        location text, 
        lattitude float, 
        longitude float
     )
"""

time_table_create = """
    CREATE TABLE IF NOT EXISTS time
    (
        start_time TIMESTAMP PRIMARY KEY,
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday text
    )
"""

# songplays table
songplays_table_create = """
    CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id SERIAL PRIMARY KEY, 
        start_time TIMESTAMP REFERENCES time(start_time), 
        user_id int NOT NULL REFERENCES users(user_id), 
        level text, 
        song_id text REFERENCES songs(song_id), 
        artist_id text REFERENCES artists(artist_id), 
        session_id int, 
        location text, 
        user_agent text
    )
"""

# INSERT RECORDS
songplays_table_insert = """
    INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

users_table_insert = """
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
"""

songs_table_insert = """
    INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
"""

artists_table_insert = """
    INSERT INTO artists
    (artist_id, name, location, lattitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
"""


time_table_insert = """
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
"""
# FIND SONGS

song_select = """
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
"""

# QUERY LISTS
create_table_queries = [
    users_table_create,
    artists_table_create,
    songs_table_create,
    time_table_create,
    songplays_table_create,
]
drop_table_queries = [
    songplays_table_drop,
    users_table_drop,
    songs_table_drop,
    artists_table_drop,
    time_table_drop,
]
