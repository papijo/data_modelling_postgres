# Relational Data Modelling with Postgres

This documentation outlines the Sparkify ETL (Extract, Transform, Load) Pipeline, a data engineering project that extracts, transforms, and loads data into a PostgreSQL database. The pipeline is designed to handle data related to a music streaming service.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [ETL Process](#etl-process)
- [Running the ETL Pipeline](#running-the-etl-pipeline)
- [Database Schema](#database-schema)
- [SQL Queries](#sql-queries)
- [License](#license)

## Overview

The Sparkify ETL Pipeline is a data engineering project that extracts data from log and song files, transforms it as needed, and loads it into a PostgreSQL database. This pipeline is designed to handle data related to a music streaming service.

## Prerequisites

Before running the Sparkify ETL pipeline, ensure that you have the following prerequisites:

- Python 3.x installed on your system.
- PostgreSQL database server installed and running.
- Required Python packages (`psycopg2`, `pandas`) installed. You can install them using `pip`.

## ETL Process

The ETL process consists of the following steps:

1. **Extract**: Read data from JSON files containing song and user activity logs.

2. **Transform**: Transform the data as needed to prepare it for insertion into the database. This includes filtering relevant events, converting timestamps, and selecting specific fields.

3. **Load**: Insert the transformed data into a PostgreSQL database with a predefined schema.

## Running the ETL Pipeline

To run the Sparkify ETL pipeline, follow these steps:

1. Make sure you have a PostgreSQL database server running.

2. Update the database connection details (host, dbname, user, password) in the `psycopg2.connect` call within the `main` function.

3. Open a terminal and navigate to the directory containing the ETL script.

4. Run the ETL script using the following command:

   ```bash
   python etl.py
   ```

   This command will start the ETL process, which will extract, transform, and load the data into the PostgreSQL database.

## Database Schema

The ETL pipeline loads data into the following tables in the PostgreSQL database:

- `users`: Contains user information.
- `songs`: Contains information about songs.
- `artists`: Contains information about artists.
- `time`: Contains timestamps and derived time-related information.
- `songplays`: Contains records of song plays, including foreign keys to the `songs`, `artists`, `time`, and `users` tables.

You can create these tables using the schema defined in the `sql_queries.py` file.

## SQL Queries

The Sparkify ETL Pipeline utilizes a set of SQL queries to create and manage the database schema and to insert records into the tables. These queries are defined in the `sql_queries.py` file and are an essential part of the ETL process.

### Table Creation Queries

These queries are responsible for creating the tables that will store the transformed data.

- **`users_table_create`**: This query creates the `users` table, which stores user information. It includes columns for user ID, first name, last name, gender, and level.

- **`songs_table_create`**: This query creates the `songs` table, which stores information about songs. It includes columns for song ID, title, artist ID, year, and duration.

- **`artists_table_create`**: This query creates the `artists` table, which stores information about artists. It includes columns for artist ID, name, location, latitude, and longitude.

- **`time_table_create`**: This query creates the `time` table, which contains timestamps and derived time-related information. It includes columns for start time, hour, day, week, month, year, and weekday.

- **`songplays_table_create`**: This query creates the `songplays` table, which stores records of song plays. It includes columns for song play ID, start time, user ID, level, song ID, artist ID, session ID, location, and user agent.

### Table Dropping Queries

These queries are used to drop the tables if they exist. They are typically executed before creating the tables to ensure a fresh start.

- **`songplays_table_drop`**: Drops the `songplays` table if it exists.

- **`users_table_drop`**: Drops the `users` table if it exists.

- **`songs_table_drop`**: Drops the `songs` table if it exists.

- **`artists_table_drop`**: Drops the `artists` table if it exists.

- **`time_table_drop`**: Drops the `time` table if it exists.

### Record Insertion Queries

These queries are responsible for inserting records into the tables after the data has been transformed.

- **`songplays_table_insert`**: Inserts records into the `songplays` table, including start time, user ID, level, song ID, artist ID, session ID, location, and user agent.

- **`users_table_insert`**: Inserts records into the `users` table, including user ID, first name, last name, gender, and level. It handles conflicts by updating the user's level.

- **`songs_table_insert`**: Inserts records into the `songs` table, including song ID, title, artist ID, year, and duration. It handles conflicts by doing nothing to avoid duplicates.

- **`artists_table_insert`**: Inserts records into the `artists` table, including artist ID, name, location, latitude, and longitude. It handles conflicts by doing nothing to avoid duplicates.

- **`time_table_insert`**: Inserts records into the `time` table, including start time, hour, day, week, month, year, and weekday. It handles conflicts by doing nothing to avoid duplicates.

### Find Songs Query

- **`song_select`**: This query is used to find songs in the `songs` and `artists` tables based on the song title, artist name, and song duration. It returns the `song_id` and `artist_id` for matching songs.

## Query Lists

- **`create_table_queries`**: A list of all table creation queries. These queries are executed to create the necessary tables.

- **`drop_table_queries`**: A list of all table dropping queries. These queries are executed to drop existing tables before creating new ones.

These SQL queries play a crucial role in the Sparkify ETL Pipeline, enabling the creation of a well-structured database schema and the insertion of data for analysis.

---

_Note: SQL queries are defined in the `sql_queries.py` file and are executed within the ETL pipeline to perform database operations._
