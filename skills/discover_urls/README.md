# discover_urls

Discovers and extracts all URLs from a web page or HTML content. Use this skill to find links for crawling, build site maps, or discover related pages. Can filter URLs by domain, pattern, or type.

## Parameters

- **url** (string): The URL of the page to extract links from. The page will be fetched and parsed.
- **html** (string): Raw HTML content to extract URLs from. Use instead of url when you already have the HTML.
- **domain_filter** (string): Optional domain to filter URLs (e.g., 'example.com' returns only same-domain links).
- **max_urls** (integer): Maximum number of URLs to return. Default is 100.

## Invoke

- **Type**: http
- **Endpoint**: https://mcp.octoparse.com
- **Method**: tools/call
