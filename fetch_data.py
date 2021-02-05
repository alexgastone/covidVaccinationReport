from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile

def auth():
	api = KaggleApi()
	api.authenticate()
	return api

def download_data(api):
	api.dataset_download_files('gpreda/covid-world-vaccination-progress')


def extract_data():
	zf = ZipFile('covid-world-vaccination-progress.zip')
	zf.extractall()
	zf.close()

def main():
	api = auth()
	download_data(api)
	extract_data()

if __name__ == '__main__':
	main()