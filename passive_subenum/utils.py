import json
import csv

def save_output(subdomains, output, fmt="txt"):
    if fmt == "txt":
        with open(output, "w") as f:
            f.write("\n".join(subdomains))
    elif fmt == "json":
        with open(output, "w") as f:
            json.dump(subdomains, f, indent=2)
    elif fmt == "csv":
        with open(output, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["subdomain"])
            for s in subdomains:
                writer.writerow([s])
    print(f"[+] Results saved to {output}")
