import pandas as pd
import requests
class parsingWDF:
	'''
	response:
	df_id:
	'''
	def __init__(self, response):
		self.response = response
		self.df_id = pd.DataFrame();
		for source in self.sources:
			row = pd.Series(source)
			self.df_id = self.df_id.append(row, ignore_index = True)
		self.df_id.set_index('name', inplace = True)
		print(self.df_id.columns)
		print(self.df_id)
		self.seeColumns()
		self.analyzeCategory()

	def seeColumns(self):
		for index in self.df_id.columns:
			print(index)
			print(self.df_id[index])
	
	def analyzeCategory(self):
		response = self.df_id['category'].value_counts()
		print(response)
		group = self.df_id.groupby(['category'])
		print(group['id'].value_counts())