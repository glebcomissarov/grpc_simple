import os
import duckdb


def create_database(path: str):
    con = duckdb.connect(
        database=os.path.join(path, "server_db.duckdb"), read_only=False
    )

    con.execute(
        """
        DROP TABLE IF EXISTS purchases;
        DROP TABLE IF EXISTS products_info;
        DROP TABLE IF EXISTS categories_info;

        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INTEGER,
            purchase_date TIMESTAMP,
            transaction_id INTEGER,
            product_id INTEGER,
            amount INTEGER,
        );

        CREATE TABLE IF NOT EXISTS products_info (
            product_id INTEGER,
            category_id INTEGER,
            product_info VARCHAR,
            price REAL,
        );

        CREATE TABLE IF NOT EXISTS categories_info (
            categogy_id INTEGER,
            categogy_info VARCHAR,
        );

        INSERT INTO categories_info
        VALUES
            (10, 'electric toothbrush'),
            (15, 'blender');

        INSERT INTO products_info
        VALUES
            (102, 10, 'Oral-B Vitality Pro Protect X Clean Electric Toothbrush White', 4093),
            (154, 10, 'Philips One Electric Toothbrush by Sonicare', 5600);

        INSERT INTO purchases
        VALUES
            (1, '2023-05-01 10:00:00', 100, 102, 1),
            (2, '2023-05-01 10:05:00', 101, 102, 1);
        """
    )
    print("Database './data/server_db.duckdb' has been created")
    print(con.sql("SHOW TABLES;"))


if __name__ == "__main__":
    create_database("./grpc_stream/data")
