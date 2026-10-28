# Logical data model

Both tables retain a product identifier. Product-day price rows are a fact table; review IDs are separate. The product_id relationship is validated during ingestion rather than enforced as a physical SQLite foreign key because prices contain multiple rows per product.

~~~mermaid
erDiagram
  PRICES {
    string product_id PK
    string observed_date PK
    string product_name
    string category
    string seller
    float price
    float list_price
    int inventory
    int units_sold
  }
  REVIEWS {
    string review_id PK
    string product_id
    string review_date
    int rating
    string review_text
    string sentiment
  }
  PRICES }o--o{ REVIEWS : "conceptual join on product_id"
~~~

Analysis joins reviews to a distinct product/category dimension to prevent repeated product-day rows from inflating review counts. A production normalization should add products and sellers tables with explicit foreign keys and time-stamped price observations.
