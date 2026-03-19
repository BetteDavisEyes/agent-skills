# Lead Track Guidance

Use this file after `lead-template-shortlist.json`.

## local-business-leads

Use this track when the user wants:

- restaurants
- salons
- clinics
- gyms
- shops
- map listings
- directory-based local businesses

Typical outputs:

- business name
- address
- phone
- website
- rating
- page URL

Default recommendations:

- `1577 Google Maps Scraper` for discovery
- `941 Google Maps Reviews Scraper` only when reviews are explicitly needed
- `1386 Contact Details Scraper` as the default website-based contact enrichment step
- `1463 Superpages Scraper` or `944 Yellow Pages Scraper (Cloud)` when a stable directory workflow is a better fit
- `1683 Gelbe Seiten Details Scraper (Cloud by URLs)` for German directory detail enrichment

Typical chains:

- `Google Maps Scraper -> Contact Details Scraper`
- `Google Maps Scraper -> Google Maps Reviews Scraper`
- `Superpages Scraper -> Contact Details Scraper`

## b2b-company-leads

Use this track when the user wants:

- company contacts
- outreach targets
- website-based discovery
- search-engine lead discovery
- email-oriented company prospecting

Typical outputs:

- result title
- result URL
- source URL
- company page URL
- search-discovered targets

Default recommendations:

- `15 Google Search Scraper` when the user wants company discovery without contact details
- `2150 Google Search Email Finder (Premium)` when the user explicitly needs contact details such as email or phone
- `858 Clutch Scraper (Company Listing)` when the user wants directory-style B2B company discovery, especially for agencies or service providers

Typical chains:

- `Google Search Email Finder (Premium)` as a standalone email-focused workflow
- `Clutch Scraper (Company Listing)` as a standalone B2B directory-discovery workflow

## Common Rules

- Prefer one primary recommendation.
- Add one alternative only when it covers a meaningfully different geography, directory source, or enrichment need.
- Do not widen to the full lead-generation category until the shortlist clearly fails.
- If an upstream template provides a website URL, prefer `Contact Details Scraper` as the default enrichment choice before exploring weaker alternatives.
- Do not present `Google Search Scraper -> Google Search Email Finder (Premium)` as a default direct chain unless there is explicit evidence of a true output-to-input linkage.
- For `b2b-company-leads`, use a simple split: no contact details -> `Google Search Scraper`; contact details needed -> `Google Search Email Finder (Premium)`.
