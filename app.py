from flask import Flask,render_template,request,url_for
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        final = [np.array(features)]
        Predict = model.predict(final)

        output = int(Predict[0])
        if(output == 0):
            return (render_template('index.html', predicted_text='Cool ! The the price will be low !', col='pink'))
        elif(output == 1):
            return (render_template('index.html', predicted_text='The price will be medium !', col='pink'))
        elif (output == 2):
            return (render_template('index.html', predicted_text='The price will be high !!', col='orange'))
        elif (output == 3):
            return (render_template('index.html', predicted_text='OMG ! The price will be very high ! You may select some other features..', col='red'))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)