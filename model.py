import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('train.csv')
dataset = dataset.drop(['three_g','four_g','blue','clock_speed','dual_sim','m_dep','mobile_wt','n_cores','px_height','px_width','touch_screen','wifi'],axis=1)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)

from sklearn.svm import SVC
classifier =  SVC(kernel='linear', random_state=0)
classifier.fit(X_train,y_train)

pickle.dump(classifier, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
