# COVID Vaccination Report

Fetches and displays daily reports of wordlwide vaccination progress. See the Google Data Studio Dashboard [here](https://datastudio.google.com/s/mAm4iISx1X0).

The data is pulled from [Daniel Preda's Kaggle Dataset](https://www.kaggle.com/gpreda/covid-world-vaccination-progress), which is in turn pulled from the public [Our World In Data COVID dataset](https://github.com/owid/covid-19-data).

## Files
* `fetch_data.py`: Uses Kaggle API to download and unzip dataset, saved to current project host folder.
	* Make sure you have kaggle installed (`pip install kaggle`)
	* Note: make sure you authenticate the API with your credentials, and that the `kaggle.json` file is located in `~/Users/$username/.kaggle`
* `save_data.py`: Saves data to Google Sheets
	* Before running, 
		1. Create a new project in Google API Console and enable Google sheets API. 
		2. Share a dummy Google Sheets with the email provided when you create the Service Account on the API Console. 
		3. Make sure you have pygsheets installed (`pip install pygsheets`)
	* The JSON file created with the Service account should be in your project host folder. 
* `refresh_data.py`: runs the above python scripts, set on a scheduler using Mac's `crontab` to fetch the data daily and send to Google Sheets.
* `country_vaccinations.csv`: COVID vaccination progress dataset
