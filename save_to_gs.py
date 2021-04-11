import pygsheets
import pandas as pd
import os
from datetime import datetime, timedelta

def main():

	path="/Users/alexandra/Documents/DS_projects/covidVaccination"
	os.chdir(path)

	#authorization
	gc = pygsheets.authorize(service_file='covidvaccinations-c3302809ceaa.json')

	# load csv file pandas
	data = pd.read_csv('country_vaccinations.csv')

	# select last n days
	num_days = 20
	this_date = datetime.date(datetime.now() - timedelta(days=num_days)).strftime('%Y-%m-%d')

	fil_data = data.loc[data.date >= this_date]

	#open the google spreadsheet
	sh = gc.open('CovidVaccinations')

	#select the first sheet 
	wks = sh[0]

	#update the first sheet with df, starting at cell B2. 
	wks.set_dataframe(fil_data, (0,0))

if __name__ == '__main__':
	main()