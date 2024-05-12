import requests


# Download a dataset file from Google drive
def download_csv_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)

    with open(destination, 'wb') as f:
        f.write(response.content)


file_id = '1grulrrGM2CQIDt-d1vI6Y-4VklAjc8Jv'
destination = 'data/raw/mushroom_dataset.csv'

download_csv_from_google_drive(file_id, destination)
