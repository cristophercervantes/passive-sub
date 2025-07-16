import aiohttp
import asyncio

async def fetch_crtsh(session, domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        async with session.get(url, timeout=15) as resp:
            if resp.status == 200:
                data = await resp.json()
                return {
                    sub.strip()
                    for entry in data
                    for sub in entry.get("name_value", "").split("\n")
                    if sub.endswith(domain)
                }
    except:
        pass
    return set()

async def fetch_alienvault(session, domain):
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
    try:
        async with session.get(url, timeout=15) as resp:
            if resp.status == 200:
                data = await resp.json()
                return {
                    e["hostname"]
                    for e in data.get("passive_dns", [])
                    if e["hostname"].endswith(domain)
                }
    except:
        pass
    return set()

async def fetch_hackertarget(session, domain):
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    try:
        async with session.get(url, timeout=15) as resp:
            text = await resp.text()
            if "API count exceeded" not in text:
                return {
                    line.split(",")[0]
                    for line in text.splitlines()
                    if domain in line
                }
    except:
        pass
    return set()

async def fetch_threatcrowd(session, domain):
    url = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    try:
        async with session.get(url, timeout=15) as resp:
            if resp.status == 200:
                data = await resp.json()
                return set(data.get("subdomains", []))
    except:
        pass
    return set()

async def fetch_bufferover(session, domain):
    url = f"https://dns.bufferover.run/dns?q=.{domain}"
    try:
        async with session.get(url, timeout=15) as resp:
            if resp.status == 200:
                data = await resp.json()
                return {
                    entry.split(",")[1]
                    for entry in data.get("FDNS_A", [])
                    if entry.endswith(domain)
                }
    except:
        pass
    return set()

async def gather_all_sources(domain):
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_crtsh(session, domain),
            fetch_alienvault(session, domain),
            fetch_hackertarget(session, domain),
            fetch_threatcrowd(session, domain),
            fetch_bufferover(session, domain),
        ]
        results = await asyncio.gather(*tasks)
        merged = set()
        for res in results:
            merged |= res
        return sorted(merged)
