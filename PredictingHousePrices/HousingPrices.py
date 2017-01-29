import numpy as np
from sklearn.linear_model import LinearRegression

class predictHousePrices:

	def __init__(self):
		self.xtrain = []
		self.xtest  = []
		self.ytrain=[]
		self.T = None

	def get_input(self):
		#Features , No of samples - input 
		F, N = [ int(i) for i in raw_input().strip().split() ]
		#Training data - input
		for i in range(N):
    			self.xtrain.append(map(float, raw_input().split() ))			
		#No of test cases for test data - input
		self.T = int(raw_input())
		#Test data - input
		for i in range(self.T):
    			self.xtest.append(map(float, raw_input().split()) )

	def format_data(self):
		self.xtrain= np.array(self.xtrain)
		self.ytrain= self.xtrain[:, -1] #Last column
		self.xtrain= self.xtrain[:, :-1] #Except the Last column
		self.xtest = np.array(self.xtest)

	def predict_prices(self):
		lr = LinearRegression().fit(self.xtrain,self.ytrain)
		preds = list(lr.predict(self.xtest))
		return preds

if __name__=="__main__":
	phouse = predictHousePrices()
	phouse.get_input()
	phouse.format_data()

	print phouse.predict_prices()