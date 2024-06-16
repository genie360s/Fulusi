# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dotenv import load_dotenv
import os
# load environment variables from .env file
load_dotenv()
import psycopg

class FinscrapPipeline:
    def open_spider(self, spider):
        self.connection = psycopg.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
        

        self.cursor = self.connection.cursor()
        # create all the tables
        self.create_tables()

    def create_tables(self):
        #amana bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS amana_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #azania bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS azania_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #baroda bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS baroda_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #bank of india table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_india (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #bank of Tanzania table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_tanzania (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #dasheng table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dasheng_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)
        #bank of baroda table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_baroda (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #tanzania commercial bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tanzania_commercial_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #dcb commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dcb_commercial_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #habib african bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS habib_african_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #mkombozi bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mkombozi_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #national_microfinance_bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS national_microfinance_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #tanzania commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tanzania_commercial_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL
            )
        """)

        #international commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS international_commercial_bank (
                id SERIAL PRIMARY KEY,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                currency VARCHAR(255) NOT NULL,
                buying_price_tt_od FLOAT NOT NULL,
                selling_price_tt_od FLOAT NOT NULL
                selling_fc_notes FLOAT NOT NULL,
                buying_fc_notes_less_50_euro_usd FLOAT NOT NULL,
                buying_fc_notes_more_50_euro_usd FLOAT NOT NULL
            )
        """)

        self.connection.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
    
    def process_item(self, item, spider):
        # insert the data into the database
        if spider.name == "amana":
            self.cursor.execute("""
                INSERT INTO amana_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "azania":
            self.cursor.execute("""
                INSERT INTO azania_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "boi":
            self.cursor.execute("""
                INSERT INTO bank_of_india (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "bot":
            self.cursor.execute("""
                INSERT INTO bank_of_tanzania (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "dasheng":
            self.cursor.execute("""
                INSERT INTO dasheng_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "baroda":
            self.cursor.execute("""
                INSERT INTO bank_of_baroda (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "tcb":
            self.cursor.execute("""
                INSERT INTO tanzania_commercial_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "dcb":
            self.cursor.execute("""
                INSERT INTO dcb_commercial_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "habib":
            self.cursor.execute("""
                INSERT INTO habib_african_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))   
        elif spider.name == "mkombozi":
            self.cursor.execute("""
                INSERT INTO mkombozi_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "nmb":
            self.cursor.execute("""
                INSERT INTO national_microfinance_bank (currency, buying_price, selling_price)
                VALUES (%s, %s, %s)
            """, (item["currency"], item["buying_price"], item["selling_price"]))
        elif spider.name == "icb":
            self.cursor.execute("""
                INSERT INTO international_commercial_bank (currency, buying_price_tt_od, selling_price_tt_od, selling_fc_notes, buying_fc_notes_less_50_euro_usd, buying_fc_notes_more_50_euro_usd)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (item["currency"], item["buying_price_tt_od"], item["selling_price_tt_od"], item["selling_fc_notes"], item["buying_fc_notes_less_50_euro_usd"], item["buying_fc_notes_more_50_euro_usd"]))
        self.connection.commit()
        return item

