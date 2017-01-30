import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#getting the input
F,N = [int(i) for i in raw_input().strip().split()]
#gttng training input
xtrain=[]
for i in range(N):
    xtrain.append( map(float, raw_input().split() ))
#getting testing input
xtest=[]
T= int(raw_input())    

for i in range(T):
    xtest.append( map(float, raw_input().split() ))

#Process/structure the data
xtrain= np.array(xtrain)
ytrain= xtrain[:, -1]
xtrain =xtrain[:, :-1]
xtest=np.array(xtest)

#Model Building 
poly = PolynomialFeatures(3)
processed_xtrain = poly.fit_transform(xtrain)
model = make_pipeline(PolynomialFeatures(3), LinearRegression())
model.fit(xtrain, ytrain)

#Making predictions
preds = list(model.predict(xtest))
for pred in preds:
    print pred