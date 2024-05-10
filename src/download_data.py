import requests

def download_csv_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)

    with open(destination, 'wb') as f:
        f.write(response.content)

# Замените 'YOUR_FILE_ID' на фактический ID файла CSV на Google Диске
file_id = '1Q591z13d4Q71Lh8t8Hte_r-LAUGS6kFx'
destination = 'data/raw/mushroom_dataset.csv'

download_csv_from_google_drive(file_id, destination)
