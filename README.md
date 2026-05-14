# TrustMech

A Python tool to research and analyze any crypto or blockchain project. Paste any link and get a full due diligence report instantly.

## What is TrustMech?

TrustMech is a due diligence tool built for crypto investors, researchers, and community members. Instead of spending hours manually searching Twitter, LinkedIn, news sites, and on-chain explorers — TrustMech aggregates everything into one clean report with a trust score.

## What it analyzes

- Team — founders, developers, advisors, LinkedIn presence, anonymity check
- Funding — investors, rounds, amounts raised, VC reputation
- Social activity — Twitter/X followers, engagement rate, post frequency
- Red flags — past controversies, rug pulls, anonymous team, no audit
- On-chain data — token distribution, contract verification, wallet concentration
- Project vision — whitepaper summary, roadmap progress

## How it works

1. Paste any project URL (Twitter/X, website, CoinGecko, LinkedIn)
2. TrustMech scrapes and aggregates public data
3. An AI-powered analysis generates a structured report
4. Report includes a trust score from 0-100 with reasoning

## Example output
Project: Example Protocol
URL: https://x.com/trustmech 
Trust Score: 68/100

Team: 2 identified, 1 anonymous, no LinkedIn found
Funding: $3M seed, investor reputation: moderate
Red Flags: anonymous dev, no smart contract audit published
Green Flags: active Twitter, open source repo, known VC backing
On-chain: contract verified, no honeypot detected
## Stack

- Python 3.11
- requests + BeautifulSoup for scraping
- OpenAI API for report generation
- Rich for terminal output formatting

## Roadmap

- [x] URL input and platform detection
- [x] Web scraping and data aggregation
- [x] Trust scoring algorithm
- [x] Report generation (markdown + JSON)
- [ ] OpenAI-powered analysis
- [ ] Twitter/X API integration
- [ ] Frontend dashboard
- [ ] Browser extension
- [ ] API endpoint for developers

## Setup

pip install -r requirements.txt
python main.py https://x.com/trustmech

## Status

Work in progress — early development stage.
