# Request Classifier

Use this file to classify social media competitor monitoring requests before selecting templates.

## Primary Track

Choose one:

- `competitor-account-monitoring`
- `brand-mention-monitoring`
- `comment-monitoring`

### `competitor-account-monitoring`

Use when the user wants:

- competitor account posts
- competitor profile activity
- channel or account updates
- owned-content monitoring

Typical clues:

- account
- profile
- channel
- handle
- competitor page

### `brand-mention-monitoring`

Use when the user wants:

- posts mentioning a brand
- hashtag tracking
- keyword-based social listening
- videos or threads that mention a competitor

Typical clues:

- mention
- keyword
- hashtag
- who is talking about
- brand discussion

### `comment-monitoring`

Use when the user wants:

- comments
- replies
- user reactions
- complaint collection
- feedback collection
- comment collection for sentiment analysis

Typical clues:

- comments
- replies
- sentiment
- complaints
- feedback
- reactions

## Platform Scope

Choose one when possible:

- `twitter-x`
- `tiktok`
- `reddit`
- `youtube`
- `multi-platform-core`
- `all-core-platforms`
- `naver-blog`
- `weibo`
- `xiaohongshu`
- `linkedin`
- `gab`
- `unknown`

If the user does not specify a platform, prefer:

- `twitter-x`
- `tiktok`
- `reddit`
- `youtube`

Use `multi-platform-core` when the user wants several of the main supported platforms.

Use `all-core-platforms` when the user clearly wants coverage across:

- `twitter-x`
- `tiktok`
- `reddit`
- `youtube`

## Direct URL Availability

Choose:

- `yes`
- `no`

Use `yes` when the user already has:

- account URLs
- profile URLs
- post URLs
- video URLs
- channel URLs

## Monitoring Scope

Choose:

- `owned-content`
- `brand-mentions`
- `both`

## Track Scope

Choose:

- `single-track`
- `multi-track`
- `full-chain`

Use `single-track` when the user only wants one of:

- competitor account monitoring
- brand mention monitoring
- comment monitoring

Use `multi-track` when the user wants more than one track, but not all three.

Use `full-chain` when the user wants:

- competitor account monitoring
- brand mention monitoring
- comment monitoring

in one overall monitoring workflow.

## Core vs Secondary Decision

Use the `core` shortlist by default.

Only read the `secondary` shortlist when:

- the user explicitly names a secondary platform
- the user explicitly needs a regional platform
- the core shortlist does not fit the request
