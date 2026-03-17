# Output Inference Rules

Use these rules when a template's output fields are not fully documented in local files such as `OUTPUT.md`.

The purpose of this file is to help the skill make careful, useful output-field inferences without over-claiming what a template can produce.

Always prefer documented output fields over inferred ones.

## Evidence Priority

Infer output fields using the strongest available evidence in this order:

1. Local `OUTPUT.md`
2. Structured template index records
3. Official template page output preview
4. Official template page description
5. Official FAQ or "How to Use" content
6. Template category and naming pattern

If the inference depends mostly on steps 4 to 6, label the result as inferred.

## Core Principle

Only infer fields that are strongly supported by the template's purpose, wording, or preview.

Do not infer fields just because users commonly want them.

Common example:
- users often want `email`
- many templates do not explicitly provide `email`
- do not infer `email` unless the template page clearly supports it

## Confidence Levels

Use these confidence levels internally and reflect them in user-facing answers when the evidence is not fully documented.

### High confidence

Use when:
- the official template page preview visibly shows the field
- the template description explicitly says it extracts the field
- multiple evidence sources point to the same field

Recommended user-facing wording:
- `This template clearly outputs ...`
- `The template page explicitly shows ...`

### Medium confidence

Use when:
- the field is not shown directly in a preview
- but the template type and description strongly imply it

Recommended user-facing wording:
- `This template likely outputs ...`
- `Based on the template description, it appears to support ...`

### Low confidence

Use when:
- the field is inferred mainly from naming convention or template category
- there is no visible output preview
- there is no field-level confirmation

Recommended user-facing wording:
- `This field is only weakly inferred.`
- `This output is not documented and should be treated as uncertain.`

Avoid recommending low-confidence fields as critical link fields unless no better option exists.

## What Can Be Safely Inferred

The following patterns are often safe to infer at medium or high confidence when the template page supports the overall purpose.

### Listing templates

A listing template often outputs:
- name or title
- category or type
- rating
- address
- location text
- page URL or entity URL

Sometimes it may also output:
- phone
- website
- review count

Do not assume it outputs:
- email
- full reviews
- opening hours
- owner contact person

### Detail templates

A detail template often outputs:
- name
- address
- phone
- website
- opening hours
- category
- rating
- additional business attributes

Sometimes it may also output:
- coordinates
- menu link
- booking link

Do not assume it outputs:
- email
- full review text

### Review templates

A review template often outputs:
- reviewer name
- rating
- review text
- review date
- likes or engagement count
- business reply or owner reply

Sometimes it may also output:
- reviewer profile URL
- translated text

Do not assume it outputs:
- phone
- website
- email

### Contact or website enrichment templates

A website/contact enrichment template often outputs:
- email
- phone
- contact page URL
- social links
- address

Do not assume it outputs:
- platform-native detail URLs
- marketplace review content

### News/article templates

A news or article template often outputs:
- title
- publication date
- source
- article URL
- summary
- article body

Do not assume it outputs:
- author email
- company contact details

### Product listing templates

A product listing template often outputs:
- product name
- price
- discount
- product URL
- image URL
- rating
- review count

Do not assume it outputs:
- full product description
- specifications
- seller email

### Product detail templates

A product detail template often outputs:
- product name
- product URL
- price
- specifications
- description
- SKU or item code
- seller/store name

Do not assume it outputs:
- seller email
- full review bodies unless explicitly stated

## High-Risk Fields

These fields should never be inferred casually.

Only mark them as available when explicit evidence exists:
- email
- WhatsApp
- WeChat
- direct contact person name
- transportation convenience
- exact latitude/longitude
- internal IDs not shown in preview
- owner reply
- menu link
- booking link

These fields are often desirable, but not reliably present across templates.

## URL Inference Rules

Be strict with URL field inference.

Do not simply infer `URL`.

Instead, infer the specific URL type if possible:
- search result URL
- listing page URL
- detail page URL
- place details page URL
- website URL
- article URL
- review page URL

If the exact URL subtype is unclear, say:
- `The template likely outputs a URL field, but the exact URL subtype is not fully confirmed.`

Do not treat an unclear URL field as sufficient for downstream linking.

## Platform-Specific Caution

Some platforms use multiple URL types for different layers of data.

Examples:
- Google Maps search result URL vs Google Maps place details page URL
- marketplace category URL vs product detail URL
- publisher homepage vs article URL

For these platforms, do not rely on generic output labels like `URL` or `Page_URL` unless the template page clarifies what they represent.

## Input-to-Output Shape Heuristic

Sometimes the output shape can be inferred from the input requirement.

Example:
- if the input is a list of place detail URLs
- and the template is a review scraper
- the output likely contains review-level records for those places

Use this heuristic carefully.

It is useful for understanding record granularity:
- business-level
- review-level
- product-level
- article-level

But it should not be used to invent unsupported fields.

## Granularity Rule

Always ask what the output record represents.

Common record granularities:
- one business per row
- one review per row
- one product per row
- one article per row

This matters because a field can be valid only at one granularity.

Example:
- a business-level template may output one `website` per business
- a review-level template may output one `review_text` per review

Do not assume review-level rows also contain full business contact details.

## Language-Specific Template Pages

If a template belongs to a language-specific site and its native-language page contains clearer descriptions or examples:
- prefer the native-language template page
- use it to refine output inference

Example:
- Japanese templates may describe supported output examples more clearly on the Japanese page than in English metadata

## Recommended User-Facing Language

When output is documented:
- `This template outputs ...`

When output is strongly inferred:
- `This template likely outputs ... based on the template page and description.`

When output is uncertain:
- `This field is not documented and is only weakly inferred.`

When a field should not be promised:
- `Email is not confirmed from the available template evidence.`

## What Not To Do

Do not:
- infer email from the existence of a website field
- infer review text from the existence of a rating field
- infer place detail URLs from any generic URL field
- infer transportation convenience from address alone
- infer contact-person names from business listings
- infer article body from article title only

## Success Criteria

You are using these rules correctly when:
- documented outputs are always preferred
- inferred outputs are clearly labeled
- high-risk fields are not over-claimed
- URL subtype ambiguity is treated carefully
- downstream links are based on field type, not wishful guessing
