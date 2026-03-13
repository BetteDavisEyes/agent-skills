---
name: crawl_page
description: "Crawls a web page and returns its HTML content. Use this skill when you need to fetch the raw HTML of a URL for further processing, analysis, or extraction. Supports custom headers and timeout configuration."
license: MIT
compatibility: Requires HTTP endpoint. Compatible with agent frameworks.
metadata:
  invoke_type: "http"
  endpoint: "https://mcp.octoparse.com"
---

# crawl_page

## Overview

Crawls a web page and returns its HTML content. Use this skill when you need to fetch the raw HTML of a URL for further processing, analysis, or extraction. Supports custom headers and timeout configuration.

## Parameters

- **url** (`string`) (required): The URL of the web page to crawl. Must be a valid HTTP or HTTPS URL.
- **timeout** (`integer`): Request timeout in seconds. Default is 30.
- **headers** (`object`): Optional custom HTTP headers to send with the request (e.g., User-Agent).

## Invoke

- **Type**: http
- **Endpoint**: https://mcp.octoparse.com

## Example

See [example.json](example.json) for sample input.