import psycopg2
import config


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS vehicle (
            id SERIAL PRIMARY KEY NOT NULL,
            moto_type_name VARCHAR(50) NOT NULL,
            license_plate VARCHAR(15) NOT NULL,
            time_in TIMESTAMP,
            time_out TIMESTAMP,
            deposits INT
    )'''
    cursor.execute(query)
    conn.commit()
    conn.close()

def create_connection():
    #mở kết nối đến postgres db
    try:
        connect = psycopg2.connect(
                host = config.localhost,
                dbname = config.database,
                user = config.username,
                password = config.password,
                port = config.port_id
            )

        return connect

    except Exception as error:
        print(error)    

