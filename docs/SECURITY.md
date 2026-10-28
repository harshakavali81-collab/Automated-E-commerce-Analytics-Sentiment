# Security, data privacy and limitations

CommerceLens is an educational, single-user analytics prototype, not a regulated multi-tenant service.

- Default CSVs are fictional. No website scraping, customer contact details, retailer login or API credentials are used.
- Real review CSVs must be lawfully obtained, properly licensed and free of personal data that may not be processed.
- Raw CSVs, SQLite databases and generated reports are Git-ignored so local imports do not automatically become public. Users must also avoid manually committing private files.
- The HTML report escapes product names and labels and contains aggregates, not raw review text.
- Streamlit has no built-in project authentication; do not publicly expose a real-data instance without secure authentication, HTTPS, authorization, privacy review and professional assessment.
- Docker runs as uid 10001 with Linux capabilities dropped. Compose binds port 8501 to localhost rather than all network interfaces.
- Installing dependencies and deploying beyond a controlled local environment require vulnerability review, correct secrets management, network restrictions, backups and monitoring.
- Ingestion deduplication uses product plus day. Multiple merchants with the same product/day are collapsed; normalize identities before analyzing an external source.
- Simulated revenue, sentiment and price movement alerts must not be represented as actual sales, forecast accuracy or verified market signals.

To disclose a vulnerability, avoid placing confidential data in public issues.
