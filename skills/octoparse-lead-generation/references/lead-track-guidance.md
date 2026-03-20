# Lead Track Guidance

Use this file after `request-classifier.md` and the split shortlist files.

Read order:

1. `references/request-classifier.md`
2. `references/lead-template-shortlist-core.json`
3. `references/lead-template-shortlist-regional.json` only when needed
4. this guidance file

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
- `1576 Google Maps Email Finder` when the user wants a more contact-focused Google Maps workflow
- `1683 Gelbe Seiten Details Scraper (Cloud by URLs)` for German directory detail enrichment
- `1682 Gelbe Seiten Listing Scraper (Cloud by keyword pairs)` or `901/902 11880.com Listing/Detail Scraper` for German regional directory workflows
- `1677/1844 iTown listing/detail templates` for Japan-specific directory workflows
- `1375 Pagesjaunes Business Info Scraper` for French directory-based local-business discovery
- `1865 Google Maps advanced Scraper for Japan` for Japan-focused Google Maps discovery

Regional triggers:

- the user explicitly asks for Japan, Germany, France, or another locale with dedicated directory templates
- the user expects a non-English workflow
- the user names a source such as Gelbe Seiten, 11880, Itown, PagesJaunes, or HelloAsso

Typical chains:

- `Google Maps Scraper -> Contact Details Scraper`
- `Google Maps Scraper -> Google Maps Reviews Scraper`
- `Superpages Scraper -> Contact Details Scraper`
- `Gelbe Seiten Listing Scraper (Cloud by keyword pairs) -> Gelbe Seiten Details Scraper (Cloud by URLs)`
- `11880.com Listing Scraper -> 11880.com Detail Scraper`

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
- `1816 Helloasso Association Emails Scraper` when the user wants directory-native email discovery for associations or organizations
- `2075 Social Media Finder` when the user wants public social profile discovery rather than website contact extraction

Regional triggers:

- the user needs a geography-specific company directory
- the user wants association or organization contacts from a dedicated local source
- the core search defaults are too broad for the requested market

Typical chains:

- `Google Search Email Finder (Premium)` as a standalone email-focused workflow
- `Clutch Scraper (Company Listing)` as a standalone B2B directory-discovery workflow
- `Helloasso Association Emails Scraper` as a standalone directory-email workflow
- `Social Media Finder` as a standalone social-profile discovery workflow

## Common Rules

- Prefer one primary recommendation.
- Add one alternative only when it covers a meaningfully different geography, directory source, or enrichment need.
- Do not widen to the full lead-generation category until the shortlist clearly fails.
- If an upstream template provides a website URL, prefer `Contact Details Scraper` as the default enrichment choice before exploring weaker alternatives.
- Do not present `Google Search Scraper -> Google Search Email Finder (Premium)` as a default direct chain unless there is explicit evidence of a true output-to-input linkage.
- For `b2b-company-leads`, use a simple split: no contact details -> `Google Search Scraper`; contact details needed -> `Google Search Email Finder (Premium)`.
