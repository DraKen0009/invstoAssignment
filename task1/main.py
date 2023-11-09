import pandas
import psycopg2

data = pandas.read_excel("task1/HINDALCO_1D.xlsx")

stock_data_list = data.values.tolist()

for value in stock_data_list:
    (value[0]) = str(value[0])

hostname = "localhost"
database = "my_pgdb"
username = "postgres"
pwd = "postgres"
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    )

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS stock_data")
    create_script = """
        CREATE TABLE IF NOT EXISTS stock_data (
        serial_no SERIAL PRIMARY KEY,
        datetime TIMESTAMP NOT NULL ,
        close DECIMAL NOT NULL,
        high DECIMAL NOT NULL,
        low DECIMAL NOT NULL,
        open DECIMAL NOT NULL,
        volume INT NOT NULL,
        instrument VARCHAR(20)
        )
    """

    cur.execute(create_script)

    insert_script = "INSERT INTO stock_data (datetime,close,high,low,open,volume,instrument) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    for value in stock_data_list:
        value = tuple(value)
        cur.execute(insert_script, value)

    conn.commit()

except Exception as error:
    print(error)

finally:
    cur.close()
    conn.close()
