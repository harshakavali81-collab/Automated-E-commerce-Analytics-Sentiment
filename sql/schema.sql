PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS prices(
 product_id TEXT NOT NULL,product_name TEXT NOT NULL,category TEXT NOT NULL,
 seller TEXT NOT NULL,observed_date TEXT NOT NULL,
 price REAL NOT NULL CHECK(price>0),list_price REAL NOT NULL CHECK(list_price>0),
 inventory INTEGER NOT NULL CHECK(inventory>=0),units_sold INTEGER NOT NULL CHECK(units_sold>=0),
 PRIMARY KEY(product_id,observed_date));
CREATE TABLE IF NOT EXISTS reviews(
 review_id TEXT PRIMARY KEY,product_id TEXT NOT NULL,review_date TEXT NOT NULL,
 rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),review_text TEXT NOT NULL,
 sentiment TEXT NOT NULL CHECK(sentiment IN ('positive','negative','neutral')));
CREATE INDEX IF NOT EXISTS idx_prices_date ON prices(observed_date);
CREATE INDEX IF NOT EXISTS idx_prices_category ON prices(category);
CREATE INDEX IF NOT EXISTS idx_reviews_product ON reviews(product_id);
