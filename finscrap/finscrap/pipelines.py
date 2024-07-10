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
import logging
import psycopg

class FinscrapPipeline:
    def open_spider(self, spider):
        self.connection = psycopg.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME"),
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
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #azania bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS azania_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #baroda bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS baroda_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #bank of india table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_india (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #bank of Tanzania table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_tanzania (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #dasheng table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dasheng_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        #bank of baroda table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_of_baroda (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #tanzania commercial bank table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tanzania_commercial_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #dcb commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dcb_commercial_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #habib african bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS habib_african_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #mkombozi bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mkombozi_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #national_microfinance_bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS national_microfinance_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #tanzania commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tanzania_commercial_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price FLOAT NOT NULL,
                selling_price FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #international commercial bank
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS international_commercial_bank (
                id SERIAL PRIMARY KEY,
                currency VARCHAR(255) NOT NULL,
                buying_price_tt_od FLOAT NOT NULL,
                selling_price_tt_od FLOAT NOT NULL,
                selling_fc_notes FLOAT NOT NULL,
                buying_fc_notes_less_50_euro_usd FLOAT NOT NULL,
                buying_fc_notes_more_50_euro_usd FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #faida_fund table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS faida_fund (
                id SERIAL PRIMARY KEY,
                date VARCHAR(255) NOT NULL,
                net_asset_value_tzs FLOAT NOT NULL,
                outstanding_number_of_units FLOAT NOT NULL,
                nav_per_unit_tzs FLOAT NOT NULL,
                sales_price_per_unit_tzs FLOAT NOT NULL,
                repurchase_price_per_unit_tzs FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #uttamis_fund table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS uttamis_fund (
                id SERIAL PRIMARY KEY,
                fund_name VARCHAR(255) NOT NULL,
                fund_date VARCHAR(255) NOT NULL,
                net_asset_value_tzs FLOAT NOT NULL,
                outstanding_number_of_units FLOAT NOT NULL,
                nav_per_unit_tzs FLOAT NOT NULL,
                sales_price_per_unit_tzs FLOAT NOT NULL,
                repurchase_price_per_unit_tzs FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #government bonds table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS government_bonds (
                id SERIAL PRIMARY KEY,
                issuer VARCHAR(255) NOT NULL,
                issued_date VARCHAR(255) NOT NULL,
                maturity_date VARCHAR(255) NOT NULL,
                coupon_rate FLOAT NOT NULL,
                issued_amount FLOAT NOT NULL,
                term_years INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #corporate bonds table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS corporate_bonds (
                id SERIAL PRIMARY KEY,
                issuer VARCHAR(255) NOT NULL,
                issued_date VARCHAR(255) NOT NULL,
                maturity_date VARCHAR(255) NOT NULL,
                coupon_rate FLOAT NOT NULL,
                issued_amount FLOAT NOT NULL,
                term_years INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
    
    def process_item(self, item, spider):
        try:
            # Log the item being processed
            logging.info(f"Processing item: {item}")

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
            elif spider.name == "faida":
                self.cursor.execute("""
                    INSERT INTO faida_fund (date, net_asset_value_tzs, outstanding_number_of_units, nav_per_unit_tzs, sales_price_per_unit_tzs, repurchase_price_per_unit_tzs)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (item["date"], item["net_asset_value_tzs"], item["outstanding_number_of_units"], item["nav_per_unit_tzs"], item["sales_price_per_unit_tzs"], item["repurchase_price_per_unit_tzs"]))
            elif spider.name == "utt_amis":
                self.cursor.execute("""
                    INSERT INTO uttamis_fund (fund_name, fund_date, net_asset_value_tzs, outstanding_number_of_units, nav_per_unit_tzs, sales_price_per_unit_tzs, repurchase_price_per_unit_tzs)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (item["fund_name"], item["fund_date"], item["data"]["net_asset_value_tzs"], item["data"]["outstanding_number_of_units_tzs"], item["data"]["net_asset_value_per_unit_tzs"], item["data"]["sale_price_per_unit_tzs"], item["data"]["purchase_price_per_unit_tzs"]))
            elif spider.name == "government_bonds":
                self.cursor.execute("""
                    INSERT INTO government_bonds (issuer, issued_date, maturity_date, coupon_rate, issued_amount, term_years)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (item["issuer"], item["issued_date"], item["maturity_date"], item["coupon_rate"], item["issued_amount"], item["term_years"]))
            elif spider.name == "corporate_bonds":
                self.cursor.execute("""
                    INSERT INTO corporate_bonds (issuer, issued_date, maturity_date, coupon_rate, issued_amount, term_years)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (item["issuer"], item["issued_date"], item["maturity_date"], item["coupon_rate"], item["issued_amount"], item["term_years"]))
            # Commit the transaction
            self.connection.commit()
            logging.info(f"Item successfully processed: {item}")
        except Exception as e:
            # Log the error
            logging.error(f"Error processing item: {item}, error: {e}")
            self.connection.rollback()
        return item