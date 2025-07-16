# Passive Subdomain Enumerator

🚀 **Passive Subdomain Enumerator** is a **fast, async, and API-key-free** tool for enumerating subdomains from multiple **passive sources**.

It collects subdomains from:
✅ [crt.sh](https://crt.sh/)
✅ [AlienVault OTX](https://otx.alienvault.com/)
✅ [HackerTarget](https://hackertarget.com/)
✅ [ThreatCrowd](https://www.threatcrowd.org/)
✅ [BufferOver.run](https://dns.bufferover.run/)

No authentication. No API keys. Just **free passive enumeration**.

---

## ✨ Features

- ✅ **No API keys needed** – all public sources
- ✅ **Multiple sources** for better coverage
- ✅ **Asynchronous requests** → faster enumeration
- ✅ **Deduplicated results**
- ✅ **Output formats:** TXT, JSON, CSV
- ✅ **pipx-installable CLI tool**

---

## 📦 Installation

You can install it as a standalone CLI tool with **pipx**.

1. **Clone or download this repo**

```bash
git clone https://github.com/YOURUSERNAME/passive-subenum.git
cd passive-subenum
```

(or unzip the provided archive)

2. **Install with pipx**

```bash
pipx install .
```

If you don’t have pipx:
```bash
python3 -m pip install --user pipx
pipx ensurepath
```

---

## 🚀 Usage

Once installed, you can run it from anywhere:

### Basic Usage

```bash
passive-subenum example.com
```

This will:
✅ Enumerate subdomains from all passive sources
✅ Print deduplicated results
✅ Show the total count

---

### Save Results

You can save the output to a file:

```bash
passive-subenum example.com -o subdomains.txt
```

Or save as JSON:

```bash
passive-subenum example.com -o subdomains.json -f json
```

Or as CSV:

```bash
passive-subenum example.com -o subdomains.csv -f csv
```

---

### Examples

```bash
# Enumerate & print results
passive-subenum github.com

# Save to TXT
passive-subenum github.com -o github_subs.txt

# Save to JSON
passive-subenum github.com -o github_subs.json -f json

# Save to CSV
passive-subenum github.com -o github_subs.csv -f csv
```

---

## 🛠 How It Works

The tool performs **asynchronous HTTP requests** to multiple passive data sources:

- **crt.sh** → Certificate Transparency logs
- **AlienVault OTX** → Passive DNS records
- **HackerTarget** → Host search API
- **ThreatCrowd** → Open threat intelligence API
- **BufferOver.run** → Historical DNS records

It merges and deduplicates the results, giving you a clean subdomain list.

---

## 📂 Project Structure

```
passive_subenum/
 ├── passive_subenum/
 │   ├── cli.py        # CLI entrypoint
 │   ├── sources.py    # Passive sources
 │   ├── utils.py      # Output helpers
 │   └── __init__.py   # Version info
 ├── pyproject.toml    # Package metadata for pipx install
 └── README.md         # This file
```

---

## 🏗 Development

Want to modify or add features?

1. Clone the repo
2. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run locally

```bash
python -m passive_subenum.cli example.com
```

---

## 📌 Roadmap

✅ Add more sources (Wayback Machine, RapidDNS, etc.)
✅ Add colorized output with `rich`
✅ Add progress bars
✅ Add concurrency limits for better rate handling

---

## ⚠️ Disclaimer

This tool is for **educational & security research** purposes only.
Use it only on domains you own or have permission to test.

---

## 🖤 Credits

- Inspired by open-source recon tools
- Uses free APIs & public data sources
