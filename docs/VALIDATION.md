# Tests and limitations

Automated tests cover deterministic sample generation, end-to-end loading, repeated refresh without duplicate rows, missing sources, invalid price/date/stock/review rejection, deduplication counters, sentiment labels and negation.

No independently annotated sentiment benchmark or production accuracy metric exists; sarcasm and non-English code-switching may be mishandled. Default customer review samples are invented, and synthetic unit sales are not transaction records. No actual business uplift or verified retailer feeds.

Do not commit real PII or API secrets. Check each external data source license before importing.
