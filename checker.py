import requests

# Read websites from file
with open("sites.txt", "r") as f:
    websites = [line.strip() for line in f if line.strip()]

# Dictionary to store website status
status = {}

# Use a browser User-Agent to avoid blocking by major websites
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

# Check each website
for site in websites:
    try:
        r = requests.get(site, headers=headers, timeout=5)
        if r.status_code == 200:
            status[site] = "OK"
        else:
            status[site] = f"Error {r.status_code}"
    except Exception:
        status[site] = "Down"

# Debug print
print("Website status dictionary:", status)

# Generate HTML report
report_file = "report.html"
with open(report_file, "w", encoding="utf-8") as f:
    f.write("<html><body style='font-family: Arial;'>")
    f.write("<h1>Website Status Report</h1>")
    f.write("<table border='1' style='border-collapse: collapse;'>")
    f.write("<tr><th>Website</th><th>Status</th></tr>")

    if not status:
        f.write("<tr><td colspan='2'>No websites found or all requests failed</td></tr>")
    else:
        for site, stat in status.items():
            color = "green" if stat == "OK" else "red"
            f.write(f"<tr><td>{site}</td><td style='color:{color}'>{stat}</td></tr>")

    f.write("</table></body></html>")

print("Website status report generated! Open report.html to view it.")
