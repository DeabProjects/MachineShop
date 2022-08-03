from flask import Flask, redirect, render_template, request, url_for
from dao.vehicle import Vehicle

app = Flask(__name__)

@app.route('/vehicle')
def open_vehicle():
    return render_template("vehicles.html")

@app.route('/vehicle', methods=['POST'])
def save_vehicle():
    
    vehicle = Vehicle()
    vehicle.vehicle_plate = request.form['vehicle_plate']
    vehicle.owner = request.form['owner']
    vehicle.model = request.form['model']
    vehicle.brand = request.form['brand']
    vehicle.year = request.form['year']
    return redirect(url_for('open_vehicle'))


if __name__ == '__main__':
    app.run(debug=True)