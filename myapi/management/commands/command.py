from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
import requests
import sqlite3
class Command(BaseCommand):
	help = 'Imports customers.csv into database, adds two columns and fills them with googleAPI'

	def handle(self, *args, **kwargs):
		# Create your connection.
		# NO NEED FOR ERROR-HANDLING
		#since it always creates a new database if that one does not exist
		con = sqlite3.connect('db.sqlite3')
		# LOGIC HERE
		api_key='AIzaSyBpP6Zdn5_Y1arUh3p6fCl9bxGjsy61Dm0'
		df = pd.read_csv('customers.csv')

		for i, row in df.iterrows():

			address = row['city']
			try:
				
				api_response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}&sensor=true')
				api_response_dict = api_response.json()
			except:
				print('Error while requesting data from the GOOGLE API')

			if api_response_dict['status'] == 'OK':
				lat = api_response_dict['results'][0]['geometry']['location']['lat']
				lon = api_response_dict['results'][0]['geometry']['location']['lng']

				df.loc[i, 'latitude'] = lat
				df.loc[i, 'longitude'] = lon
		#send data to sqlite databse
	 
		df.to_sql(name='myapi_customer', con=con)

#####		


### FETCH ALL DATA INSIDE OUR TABLE TO VERIFY
# con = sqlite3.connect('db.sqlite3')
# #query ="SELECT * FROM myapi_customer"
# query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
# #query="PRAGMA table_info(Customer)"
# cursor = con.execute(query)

# rows = cursor.fetchall()

# for row in rows:
# 	print(row)


