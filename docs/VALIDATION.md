# Tests and limitations

Automated tests cover deterministic sample generation, end-to-end loading, repeated refresh without duplicate rows, missing sources, invalid price/date/stock/review rejection, deduplication counters, sentiment labels and negation.

No independently annotated sentiment benchmark or production accuracy metric exists; sarcasm and non-English code-switching may be mishandled. Default customer review samples are invented, and synthetic unit sales are not transaction records. No actual business uplift or verified retailer feeds.

Do not commit real PII or API secrets. Check each external data source license before importing.

## Advanced regressions

The advanced unit tests validate numeric alert thresholds, price jumps, latest-stock selection, report count (ten source-driven charts) and HTML escaping of untrusted product-name text. UI and Docker integration checks are described in the CI workflow; check the most recent completed GitHub Actions result for pass/fail status.

No prediction accuracy, model calibration, live-source SLA, public hosting or external business outcome is asserted.
