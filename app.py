from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/donate')
def donate():
    return render_template('payment.html')

@app.route('/process_payment', methods=['POST'])
def process_payment():
    upi_id = request.form['upi_id']
    bitcoin_address = request.form['bitcoin_address']
    amount = request.form['amount']

    # Process payment here
    # You can use the provided UPI ID, Bitcoin address, and donation amount

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
