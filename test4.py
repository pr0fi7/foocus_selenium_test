
from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_json(div_id):

    URL = "https://1121c74759d28ebca4.gradio.live/file=/content/Fooocus/outputs/2024-06-06/log.html"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # Locate the div by ID and extract table data
    div = soup.find('div', {'id': div_id})
    if not div:
        print(f"No div with id {div_id} found.")
        return None

    # Assuming the table is inside this div
    table = div.find('table')
    if not table:
        print(f"No table found inside div with id {div_id}.")
        return None
        
    # Prepare to collect data
    data = []

    # Iterate through rows of the main table
    for row in table.find_all('tr'):
        # Each row has a main cell with an image and another table with metadata
        cells = row.find_all('td')
        if len(cells) < 2:
            continue  # Skip rows that don't have at least two cells (image and metadata)

        image_info = cells[0].text.strip()
        metadata_table = cells[1].find('table')
        
        if metadata_table:
            metadata = {}
            for meta_row in metadata_table.find_all('tr'):
                label_cell, value_cell = meta_row.find_all('td')
                label = label_cell.text.strip()
                value = value_cell.text.strip()
                metadata[label] = value

            # Add image info as part of metadata
            metadata['Image Info'] = image_info
            
            # Append to the data list
            data.append(metadata)
    
    # Convert the collected data into a DataFrame
    if data:
        df = pd.DataFrame(data)
        return df
    else:
        print("No data extracted.")
        return None

print(get_json("2024-06-06_14-23-59_5430_png"))   