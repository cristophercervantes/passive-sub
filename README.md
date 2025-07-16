# Passive Subdomain Enumerator

A **fast passive subdomain enumeration tool** that uses multiple free sources (no API key required).

## Features
- Async & fast
- Sources: crt.sh, AlienVault OTX, HackerTarget, ThreatCrowd, BufferOver.run
- Output to TXT/JSON/CSV
- pipx-installable CLI tool

## Installation
```bash
pipx install .
```

## Usage
```bash
passive-subenum example.com
passive-subenum example.com -o results.txt
passive-subenum example.com -o results.json -f json
```
