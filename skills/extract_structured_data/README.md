# extract_structured_data

Extracts structured data from HTML using CSS selectors or JSON-LD/schema.org markup. Use this skill to scrape product info, article metadata, tables, or any structured content from web pages. Returns data as JSON.

## Parameters

- **url** (string): The URL of the page to extract data from.
- **html** (string): Raw HTML content to extract from. Use when you already have the HTML.
- **selectors** (object): CSS selectors mapping field names to extraction rules. E.g., {"title": "h1", "price": ".price"}.
- **schema_type** (string): Optional schema.org type to extract (e.g., 'Product', 'Article'). Extracts JSON-LD if present.

## Invoke

- **Type**: http
- **Endpoint**: https://mcp.octoparse.com
- **Method**: tools/call
