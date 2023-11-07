import kaggle
import argparse

parser = argparse.ArgumentParser(description='Загрузка датасета')

parser.add_argument('name', type=str, help='Имя датасета')
parser.add_argument('destination', type=str, help='Каталог назначения')
args = parser.parse_args()

name = args.name
destination = args.destination

kaggle.api.authenticate()
try:
    kaggle.api.dataset_download_files(name, destination, unzip=True)
    print('Downloading dataset')
except Exception as e:
    print('Download failed', '\n', e)
    