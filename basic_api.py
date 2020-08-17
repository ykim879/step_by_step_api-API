import requests

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
        response = requests.get(url)
        '''
        this check the status, you can optionally use raise_for_status() to deal with all exceptions
        '''
        if response.json()['status'] != 'ok':
            raise IOError('API key is probably overused :(')

        '''
        after status 'ok', coded below will be processed
        '''

        '''
        resquest.json() method convert json file in dictionary,
        '''
        sources = response.json()['sources'] 
        print(response.json()['sources'][0])
        '''
        for source in sources:
            self.sources[source['name']] = source['id']

        '''