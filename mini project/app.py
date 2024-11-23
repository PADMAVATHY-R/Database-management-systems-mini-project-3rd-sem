from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        database='ApartmentManagement'
    )

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/add_resident', methods=['GET', 'POST'])
def add_resident():
    if request.method == 'POST':
        name = request.form['name']
        contact_no = request.form['contact_no']
        email = request.form['email']
        apartment_id = request.form['apartment_id']
        role = request.form['role']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Residents (Name, ContactNo, Email, ApartmentID, Role) VALUES (%s, %s, %s, %s, %s)",
            (name, contact_no, email, apartment_id, role)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_residents'))
    
    return render_template('add_resident.html', title="Add Resident")

@app.route('/view_residents')
def view_residents():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Residents")
    residents = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_residents.html', residents=residents, title="View Residents")


@app.route('/add_apartment', methods=['GET', 'POST'])
def add_apartment():
    if request.method == 'POST':
        apartment_id = request.form['apartment_id']
        apartment_no = request.form['apartment_no']
        type = request.form['type']
        rent = request.form['rent']
        size = request.form['size']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `Apartments`(`ApartmentID`, `ApartmentNo`, `Type`, `Rent`, `Size`) VALUES (%s,%s,%s,%s,%s)",
            (apartment_id, apartment_no, type, rent, size)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_apartments'))
    
    return render_template('add_apartment.html', title="Add Apartment")

@app.route('/view_apartments')
def view_apartments():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Apartments")
    apartments = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('view_apartments.html', apartments=apartments, title="View Apartments")


if __name__ == '__main__':
    app.run(debug=True)
