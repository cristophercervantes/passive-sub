import argparse
import asyncio
from .sources import gather_all_sources
from .utils import save_output

def main():
    parser = argparse.ArgumentParser(description="Passive Subdomain Enumerator (No API Key)")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--output", "-o", help="Save results to file")
    parser.add_argument("--format", "-f", choices=["txt", "json", "csv"], default="txt", help="Output format")

    args = parser.parse_args()

    domain = args.domain.strip()
    print(f"[+] Enumerating subdomains for: {domain}")

    subdomains = asyncio.run(gather_all_sources(domain))

    print("\n[+] Found Subdomains:")
    for s in subdomains:
        print(s)
    print(f"\n[+] Total: {len(subdomains)}")

    if args.output:
        save_output(subdomains, args.output, args.format)

if __name__ == "__main__":
    main()
