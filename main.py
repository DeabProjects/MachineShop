from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/vehicle')
def open_vehicle():
    return render_template("vehicles.html")

@app.route('/vehicle', methods=['POST'])
def save_vehicle():
    vehicle_plate = request.form['vehicle_plate']
    owner = request.form['owner']
    model = request.form['model']
    brand = request.form['brand']
    year = request.form['year']
    return redirect(url_for('open_vehicle'))


if __name__ == '__main__':
    app.run(debug=True)