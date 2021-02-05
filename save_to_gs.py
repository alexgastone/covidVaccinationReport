import pygsheets
import pandas as pd

def main():
	#authorization
	gc = pygsheets.authorize(service_file='covidvaccinations-c3302809ceaa.json')

	# load csv file pandas
	data = pd.read_csv('country_vaccinations.csv')

	#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
	sh = gc.open('CovidVaccinations')

	#select the first sheet 
	wks = sh[0]

	#update the first sheet with df, starting at cell B2. 
	wks.set_dataframe(data, (0,0))

if __name__ == '__main__':
	main()