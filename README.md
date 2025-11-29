# Website Status Checker

A beginner-friendly Python project that checks whether a list of websites are online or offline and generates a simple HTML report.

## Features

- Reads a list of websites from a `sites.txt` file.
- Checks each website’s status using HTTP requests.
- Generates an **HTML report** showing the status of each website:
  - **Green** → Online / OK
  - **Red** → Down / Error
- Handles exceptions gracefully so offline or unreachable websites do not crash the script.
- Uses a **browser User-Agent** to increase compatibility with major websites.
- Applies a **5-second timeout** to prevent hanging on slow websites.
- Some major websites like Netflix, Hulu, Amazon, YouTube may show as Down even though they are online.
- These websites actively block automated requests to prevent bots or scraping.
- Using a browser User-Agent helps with compatibility but does not guarantee access for these sites.

---

## Requirements

- Python 3.7+  
- `requests` library  

Install requests using:

```bash
python -m pip install requests


