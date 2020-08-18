import requests
from bs4 import BeautifulSoup
import pandas as pd
class apiExplantor:
	'''
	this explains the process of using API to retrieve data from the servers
	'''
	def getSources(self):
		'''
		url contains API which is form of list. You have to get API call from the Internet to do so.
		'''
		url = ('https://newsapi.org/v2/sources?'
			   'language=en&country=us&'
			   'apiKey=55b9f473b6e642ac862d315a124c6619')
		'''
		by using requests.get() method, we will get request object which contains data in json format
		you can optionally use timeout to prevent being blocked indefinitely
		'''
		self.response = requests.get(url)
		'''
		this check the status, you can optionally use raise_for_status() to deal with all exceptions
		'''
		if self.response.json()['status'] != 'ok':
			raise IOError('API key is probably overused :(')

		'''
		after status 'ok', coded below will be processed
		'''
		'''
		resquest.json() method convert json file in dictionary,
		since it is dictionary it is easy to convert to dataframe
		'''
		sources = self.response.json()
		#print(self.response.json())
		self.parsingWDF()
		'''
		for source in sources:
			self.sources[source['name']] = source['id']

		'''
		'''
		this method will convert data into DataFrame which will be easier to view
		'''
	def parsingWDF(self):
		self.df = pd.DataFrame(self.response.json()) #move it into __init__ later
		self.df.drop(columns = ['status'], inplace = True) # the status columnn is true for every column so no longer needed
		print(self.df)
		'''The data frame is consisted of sources which is consisted of list so we are gonna put it into individual dataframe
		'''
		self.df_id = pd.DataFrame();
		self.sources = self.response.json()['sources']
		for source in self.sources:
			row = pd.Series(source)
			self.df_id = self.df_id.append(row, ignore_index = True)
		self.df_id.set_index('name', inplace = True)
		print(self.df_id.columns)
		print(self.df_id)
		self.seeColumns()
		self.analyzeCategory()

	def parsingWSoup(self):
		self.soup = BeautifulSoup(self.response.content, "lxml")
		for link in self.soup.find_all('a'):
			print(link)
			print(link['href'])

	def seeColumns(self):
		for index in self.df_id.columns:
			print(index)
			print(self.df_id[index])
	
	def analyzeCategory(self):
		response = self.df_id['category'].value_counts()
		print(response)
		group = self.df_id.groupby(['category'])
		print(group['id'].value_counts())

	def getHeadlines(self, ID):
		"""
		This procedure will take in the id and find the articles from the
		source associated with that id. It then puts them into a list and puts
		that list into a queue for processing.
		"""
		url = ('https://newsapi.org/v2/top-headlines?sources=' + ID + 
			'&apiKey=55b9f473b6e642ac862d315a124c6619')
		response = requests.get(url)
		json = response.json()
		if json['status'] != 'ok':
			raise IOError('API key is probably overused :(')
		topNews = [] 
		for elem in json['articles']:
			label = elem['source']['name'] + ': ' + elem['title']
			item = (label, elem['url'])
			topNews.append(item)
if __name__ == "__main__":
	apiExplantor(). getSources()