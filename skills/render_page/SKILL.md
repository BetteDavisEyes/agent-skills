---
name: render_page
description: "Renders a web page using a headless browser and returns the final DOM/HTML after JavaScript execution. Use this skill for JavaScript-heavy SPAs, dynamic content, or pages that require client-side rendering. Returns the rendered HTML."
license: MIT
compatibility: Requires HTTP endpoint. Compatible with agent frameworks.
metadata:
  invoke_type: "http"
  endpoint: "https://mcp.octoparse.com"
---

# render_page

## Overview

Renders a web page using a headless browser and returns the final DOM/HTML after JavaScript execution. Use this skill for JavaScript-heavy SPAs, dynamic content, or pages that require client-side rendering. Returns the rendered HTML.

## Parameters

- **url** (`string`) (required): The URL of the page to render. Must be a valid HTTP or HTTPS URL.
- **wait_selector** (`string`): Optional CSS selector to wait for before capturing. Use for pages that load content dynamically.
- **wait_time** (`integer`): Optional time in milliseconds to wait after page load. Default is 0.
- **viewport_width** (`integer`): Viewport width in pixels. Default is 1920.
- **viewport_height** (`integer`): Viewport height in pixels. Default is 1080.

## Invoke

- **Type**: http
- **Endpoint**: https://mcp.octoparse.com

## Example

See [example.json](example.json) for sample input.