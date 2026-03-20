# Request Classifier

Use this file before reading the lead shortlist.

Its job is to normalize a user request into four routing decisions:

1. `lead_track`
2. `needs_contact_details`
3. `source_preference`
4. `regional_mode`

Once those four decisions are clear, load:

- `references/lead-template-shortlist-core.json` first
- `references/lead-template-shortlist-regional.json` only when `regional_mode = true`

## Step 1: Determine `lead_track`

Choose the user's primary lead goal:

- `local-business-leads`
  - restaurants, salons, clinics, gyms, retail stores, local services, map listings, directory businesses
- `b2b-company-leads`
  - SaaS companies, agencies, service providers, company lists, outreach targets, business websites
- `mixed`
  - the request spans both business discovery and downstream enrichment across different source types

If mixed, still choose one primary track and say why.

## Step 2: Determine `needs_contact_details`

Set this to `true` when the user explicitly wants:

- email
- phone
- contact info
- social links
- outreach-ready leads

Set this to `false` when the user only wants:

- company discovery
- business names
- websites
- listing pages
- result URLs
- review enrichment

Important:

- `website` alone is not the same as `contact details`
- `reviews` alone do not imply contact enrichment

## Step 3: Determine `source_preference`

Prefer the strongest explicit source signal:

- `maps`
  - Google Maps, map leads, nearby businesses, places
- `directory`
  - Yellow Pages, Superpages, Clutch, Gelbe Seiten, 11880, Itown, PagesJaunes, HelloAsso
- `search`
  - Google Search, search engine discovery, SERP-based company discovery
- `website-only`
  - the user already has website URLs and only wants enrichment
- `unknown`
  - no clear source specified

When the source is unknown:

- default to `maps` for `local-business-leads`
- default to `search` for `b2b-company-leads`

## Step 4: Determine `regional_mode`

Set `regional_mode = true` when any of these are true:

- the user explicitly names Japan, Germany, France, or another locale with a dedicated shortlist template
- the user asks for a local directory that is not part of the default English/global core set
- the user uses a non-English keyword or expects a non-English site workflow
- the core shortlist cannot satisfy the geography or language requirement

Otherwise keep `regional_mode = false`.

## Step 5: Determine `wants_reviews`

Set this to `true` only when the user explicitly asks for:

- reviews
- review text
- sentiment
- review-based ranking

Do not widen into review templates unless this signal is present.

## Routing Matrix

Use these defaults once the request is classified:

- `local-business-leads` + `needs_contact_details = false` + `source_preference in {maps, unknown}`
  - default to `Google Maps Scraper`
- `local-business-leads` + `needs_contact_details = true` + upstream can provide website URLs
  - default to `Google Maps Scraper -> Contact Details Scraper`
- `local-business-leads` + `wants_reviews = true`
  - add `Google Maps Reviews Scraper` after discovery
- `b2b-company-leads` + `needs_contact_details = false`
  - default to `Google Search Scraper`
- `b2b-company-leads` + `needs_contact_details = true`
  - default to `Google Search Email Finder (Premium)`
- `source_preference = website-only`
  - default to `Contact Details Scraper`
- `source_preference = directory` + `regional_mode = true`
  - load the regional shortlist before deciding

## Examples

**Example 1**
Prompt: `I need New York restaurant leads with websites and review summaries.`

- `lead_track = local-business-leads`
- `needs_contact_details = false`
- `source_preference = maps`
- `regional_mode = false`
- `wants_reviews = true`

Recommended starting point:
- `Google Maps Scraper -> Google Maps Reviews Scraper`

**Example 2**
Prompt: `Find me US SaaS companies, I only need company pages and websites.`

- `lead_track = b2b-company-leads`
- `needs_contact_details = false`
- `source_preference = search`
- `regional_mode = false`
- `wants_reviews = false`

Recommended starting point:
- `Google Search Scraper`

**Example 3**
Prompt: `I need Tokyo dental clinic emails.`

- `lead_track = local-business-leads`
- `needs_contact_details = true`
- `source_preference = directory`
- `regional_mode = true`
- `wants_reviews = false`

Recommended starting point:
- load the regional shortlist first, then choose between Japan-specific directory and Google Maps workflows

## Guardrails

- Do not choose a chain just because two templates use similar search inputs.
- Do not bypass the regional shortlist when the request clearly depends on locale-specific sources.
- Do not treat review templates as lead sources.
- If the user already has website URLs, do not force a discovery template first.
