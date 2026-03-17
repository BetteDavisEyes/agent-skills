# Linking Rules

Use these rules when deciding whether the output of one Octoparse template can feed the input of another template.

These rules exist to prevent false-positive template chains.

Always prefer explicit evidence from:
- `INPUT.md`
- `OUTPUT.md`
- official template detail pages
- stable template index records

If stronger evidence is missing, use these rules conservatively and label the conclusion as inferred.

## Core principle

A link is valid only when the upstream template produces the exact field type or URL type required by the downstream template.

Do not assume compatibility just because two fields both contain the word `URL`, `link`, `page`, `address`, `contact`, or `details`.

## URL Type Distinctions

Treat these as different field types unless documentation explicitly proves they are interchangeable:

- search result URL
- listing page URL
- place details page URL
- business website URL
- product listing URL
- product detail URL
- review page URL
- article page URL
- profile page URL
- category page URL

### Search result URL

This usually points to a search results page or map search page.

Examples:
- a Google Maps search URL for `restaurants in new york`
- a Google News search results URL

Typical use:
- valid input for `by URLs` listing/search-result templates

Usually not valid as:
- place details page URL
- business website URL
- review page URL

### Listing page URL

This usually points to a list of entities rather than one entity.

Examples:
- marketplace search result page
- category listing page
- map result page with many businesses

Typical use:
- valid input for listing-level templates

Usually not valid as:
- detail page URL
- review template input

### Place details page URL

This points to one specific place or business detail page.

Examples:
- a Google Maps place details page for one restaurant

Typical use:
- valid input for place detail scrapers
- valid input for review scrapers that explicitly ask for place detail URLs

Usually not valid as:
- website URL

### Business website URL

This points to the business's own external site.

Typical use:
- valid input for website/contact/email enrichment templates

Usually not valid as:
- place details page URL
- marketplace detail URL

### Product listing URL vs product detail URL

Treat product listing pages and product detail pages as different inputs.

Examples:
- category page of dresses
- single product page for one dress

Do not feed a category/listing URL into a product detail template unless the template explicitly accepts listing pages.

## Field Compatibility Rules

Only mark a field mapping as direct when the downstream input requirement matches the upstream output at the same semantic level.

Examples of semantic level:
- list of businesses
- single place
- single product
- business website
- review content

### Direct link

A direct link is valid when:
- the downstream input field name clearly matches the upstream output field type, and
- documentation or template description supports the match

Example:
- upstream output: `place_url`
- downstream input: `Google Maps Place Details Page URLs`

### Indirect link

An indirect link means the user needs an intermediate template or conversion step.

Example:
- listing template outputs a listing/search-level URL
- review template requires a place details page URL
- a detail-enrichment template may be needed in between

When this happens, recommend the intermediate template explicitly.

### Invalid link

A link is invalid when:
- the required object type is different
- the URL type is different
- the field is only superficially similar
- the upstream template does not reliably output the required field

## Common Valid Patterns

These are common link patterns that are generally safe when confirmed by template wording or output preview.

### Listing -> Details

Valid when the listing template outputs one-item detail URLs and the downstream detail template accepts those URLs.

Examples:
- marketplace listing template -> product detail template
- directory listing template -> business detail template

### Listing -> Reviews

Valid only when the listing template outputs the exact place/detail URLs required by the review template.

Example:
- Google Maps listing output `place_url` -> Google Maps Reviews Scraper input `Google Maps Place Details Page URLs`

Do not assume all Google Maps listing templates output place detail URLs unless the template page or docs say so.

### Details -> Reviews

Often valid when the details template preserves the original place/detail page URL.

Example:
- place details template output `place_url` -> review template input `place details page URLs`

### Details -> Contact or Email Enrichment

Often valid when the details template outputs a `website` field.

Example:
- business detail template output `website` -> website/contact/email scraper input `Website URL`

Important:
- `website` can support contact enrichment
- `website` does not automatically mean `email`

### Listing -> Contact or Email Enrichment

Only valid when the listing template already exposes `website`.

If the listing template does not expose a usable website URL, recommend:
- listing -> details -> contact/email enrichment

## Common Invalid Patterns

These patterns should be treated as invalid unless the template docs explicitly prove otherwise.

### Search result URL -> Review template

Invalid in most cases.

A review template usually needs a one-place details URL, not a search result page.

### Website URL -> Place details template

Invalid in most cases.

A business website is not the same as a platform-specific place detail page.

### Search keyword -> By-URL template

Invalid.

If a template expects URLs, a keyword is not a substitute.

### Phone -> Email

Invalid.

These are different contact types.

### Address -> Transportation convenience

Not a direct field mapping.

An address may support later reasoning about transportation access, but it is not itself a transportation-convenience field.

### Review text -> Contact enrichment

Invalid.

Review content is not a contact field source.

## Email Rules

Be especially strict with email claims.

Do not claim that a template can produce email unless at least one of these is true:
- `OUTPUT.md` explicitly lists an email field
- the official template page explicitly says it extracts emails
- output preview clearly shows email

If the template only provides:
- website
- phone
- contact page URL

then say:
- email is not confirmed
- a website/contact/email enrichment step may still be needed

## Review Rules

Review templates are usually downstream templates.

To link into a review template, confirm:
- the exact required input object type
- whether it needs one-item detail URLs
- whether the upstream template outputs that exact URL type

Do not assume:
- all listing templates can feed review templates
- all detail templates preserve the URL needed by review templates

## MultiInput Rules

If a downstream input is a `MultiInput` field:
- each line is usually a separate independent input item
- do not split one logical value across lines
- do not merge multiple object types into one line

Examples:
- valid: one URL per line
- valid: one keyword per line
- invalid: half of a query on one line and the other half on the next line

## Template Page Verification Rules

When local `INPUT.md` or `OUTPUT.md` is incomplete:
- check the official template detail page
- inspect the parameter label and examples
- inspect FAQ or "How to Use" sections
- inspect output preview if available

If the template is language-specific:
- prefer the native-language template page when it contains clearer usage rules

Example:
- Japanese template guidance should be checked on the Japanese template page if the English metadata is too thin

## Confidence Labels

Use these labels internally when reasoning, and reflect them in the user-facing answer when helpful.

### High confidence

Use when:
- the mapping is documented in `INPUT.md` and `OUTPUT.md`
- or the official template page clearly confirms both sides of the mapping

### Medium confidence

Use when:
- downstream input is explicit
- upstream output is strongly implied by output preview or description

### Low confidence

Use when:
- upstream output is inferred from template category or naming only
- no output preview or field documentation is available

Low-confidence links must be labeled as inferred.

## Recommended User-Facing Language

When a link is confirmed:
- `This is a direct link.`
- `This chain is supported by the downstream input requirement and the upstream output field.`

When a link needs an intermediate template:
- `This is not a direct link.`
- `You likely need an intermediate details step.`

When a link is inferred:
- `This link is likely valid, but the output field match is inferred from the template description.`

When a link is invalid:
- `These templates are not directly linkable because the downstream template requires a different field type.`

## Success Criteria

You are applying these rules correctly when:
- you do not confuse listing/search/detail/website URLs
- you do not over-claim email availability
- you recommend intermediate templates when needed
- you clearly separate documented links from inferred links
- the user can tell exactly which field connects each step
