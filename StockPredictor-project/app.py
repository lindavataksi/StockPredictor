from flask import Flask, render_template, request, url_for
from model import predict_stock_price

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        ticker = request.form['Ticker']
        current_price, future_price, accuracy_percentage = predict_stock_price(ticker)
        prediction_text = f"The current price of {ticker} is ${current_price} and the predicted price after 1 year is ${future_price}."
        accuracy = f"Accuracy : {accuracy_percentage}%"
    # elif request.method == 'GET':
        image_urls = {
            'image1': url_for('static', filename='plot1.png'),
            'image2': url_for('static', filename='plot2.png'),
            'image3': url_for('static', filename='plot3.png')
        }
        return render_template('index.html', prediction_text=prediction_text, accuracy = accuracy, image_urls = image_urls)
        # return render_template('index.html', image_urls = image_urls)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
