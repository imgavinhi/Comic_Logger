import psycopg2
from psycopg2 import Error

def initialize_database(db_name, user, password, host, port="5432"):
    """
    Connects to the PostgreSQL database and creates the necessary tables
    for the comic logging project.
    """
    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True # Set autocommit to True to ensure DDL commands are committed immediately
        cursor = conn.cursor()

        print("Successfully connected to Archieve!")

        # SQL statements to create the tables
        # These are taken directly from the 'comic_database_tables_pg' immersive artifact.
        create_tables_sql = """
        -- 1. Series Table
        CREATE TABLE IF NOT EXISTS Series (
            SeriesID SERIAL PRIMARY KEY,
            SeriesName TEXT NOT NULL,
            Publisher TEXT,
            StartYear INTEGER,
            EndYear TEXT,
            Status TEXT,
            Genre TEXT,
            Writer TEXT,
            Artist TEXT,
            Notes TEXT,
            IsCompleteInCollection BOOLEAN
        );

        -- 2. Issue Table
        CREATE TABLE IF NOT EXISTS Issue (
            IssueID SERIAL PRIMARY KEY,
            SeriesID INTEGER NOT NULL,
            IssueNumber TEXT NOT NULL,
            Title TEXT,
            PublicationDate TEXT,
            CoverArtist TEXT,
            VariantCover BOOLEAN,
            Condition TEXT,
            DigitalOrPhysical TEXT,
            FOREIGN KEY (SeriesID) REFERENCES Series(SeriesID)
                ON DELETE CASCADE
        );

        -- 3. ReadingSession Table
        CREATE TABLE IF NOT EXISTS ReadingSession (
            ReadingSessionID SERIAL PRIMARY KEY,
            SeriesID INTEGER NOT NULL,
            DateRead TEXT NOT NULL,
            StartIssueNumberRead TEXT NOT NULL,
            EndIssueNumberRead TEXT NOT NULL,
            NumberOfIssuesRead INTEGER,
            Rating INTEGER,
            ReadingNotes TEXT,
            TimeSpentReading INTEGER,
            FOREIGN KEY (SeriesID) REFERENCES Series(SeriesID)
                ON DELETE CASCADE
        );
        """

        # Execute the SQL commands
        cursor.execute(create_tables_sql)
        print("Tables 'Series', 'Issue', and 'ReadingSession' created or already exist successfully!")

    except (Exception, Error) as err:
        print(f"Error while connecting to PostgreSQL or creating tables: {err}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection closed.")