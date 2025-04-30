import requests
from bs4 import BeautifulSoup

# Your published Google Docs URL (must be in "published to web" format)
url = "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub"

def fetch_document_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch document. Status code: {response.status_code}")

def extract_table_data(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    coords = []

    if not table:
        raise Exception("No table found in the document.")

    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 3:
            try:
                x = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))
                coords.append((x, y, char))
            except ValueError:
                continue
    return coords

def render_grid(coords, max_x=100, max_y=10):
    grid = [[" " for _ in range(max_x)] for _ in range(max_y)]

    for x, y, char in coords:
        if 0 <= x < max_x and 0 <= y < max_y:
            grid[y][x] = char

    for y in range(max_y - 1, -1, -1):  # Print from top (highest y) to bottom
        print("".join(grid[y]))

def main():
    html = fetch_document_html(url)
    coords = extract_table_data(html)
    render_grid(coords)

if __name__ == "__main__":
    main()
