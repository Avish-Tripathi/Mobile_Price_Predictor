import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('train.csv')
dataset = dataset.drop(['three_g','four_g','blue','clock_speed','dual_sim','m_dep','mobile_wt','n_cores','px_height','px_width','touch_screen','wifi'],axis=1)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.neighbors import KNeighborsClassifier
classifier =  KNeighborsClassifier(n_neighbors = 14, metric = 'minkowski')
#classifier = LogisticRegression(random_state=0)
classifier.fit(X,y)

pickle.dump(classifier, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
