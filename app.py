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
            return (render_template('index.html', predicted_text='Low price!', col='pink', link='https://www.digit.in/top-products/top-10-android-smartphones-under-rs-15-000-18.html'))
        elif(output == 1):
            return (render_template('index.html', predicted_text='Medium price!', col='pink', link='https://pricebaba.com/mobile/pricelist/trending-mobile-phones-in-india'))
        elif (output == 2):
            return (render_template('index.html', predicted_text='Moderately higher price!', col='orange', link='https://www.91mobiles.com/top-10-mobiles-in-india'))
        elif (output == 3):
            return (render_template('index.html', predicted_text='High price!', col='red', link='https://www.gadgetsnow.com/slideshows/worlds-10-most-expensive-smartphones/15-most-expensive-smartphones-in-the-world/photolist/65072793.cms'))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
