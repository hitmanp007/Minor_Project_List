import requests
from bs4 import BeautifulSoup


def decode_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if table is None:
        raise ValueError("No table found in the document.")

    points = []

    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])

        if len(cells) < 3:
            continue

        x_text = cells[0].get_text(strip=True)
        character = cells[1].get_text(strip=True)
        y_text = cells[2].get_text(strip=True)

        try:
            x = int(x_text)
            y = int(y_text)
        except ValueError:
            continue

        points.append((x, character, y))

    if not points:
        raise ValueError("No valid coordinate data found.")

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    grid = [
        [" "] * (max_x + 1)
        for _ in range(max_y + 1)
    ]

    for x, character, y in points:
        grid[y][x] = character

    for row in reversed(grid):
        print("".join(row))


url = "https://docs.google.com/document/d/e/2PACX-1vTGiOWO-6-AEZpK9Yi3aTkebfXRxmoqmE0tMaRIld99aNRXgRLnWjTsyBmenSl7sXfVfJ3vtpj5CYiG/pub"

decode_secret_message(url)