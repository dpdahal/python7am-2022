import mysql.connector


class Students:
    # connect database
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
        )
        self.instance = self.conn.cursor()
        self.instance.execute('CREATE DATABASE IF NOT EXISTS python8am')
        self.instance.execute('USE python8am')

    #     create table
    def create_table(self):
        self.instance.execute(
            '''
            CREATE TABLE IF NOT EXISTS python8am.students
            (id INT(11) PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            address VARCHAR(255) NOT NULL            
            )''')

    #     insert data
    def insert_data(self, name, email, address):
        self.instance.execute(
            'INSERT INTO students (name, email, address) VALUES (%s, %s, %s)',
            (name, email, address))
        self.conn.commit()

    #     select data
    def select_data(self):
        self.instance.execute('SELECT * FROM students')
        return self.instance.fetchall()

    #     update data
    def update_data(self, id, name, email, address):
        self.instance.execute(
            'UPDATE students SET name = %s, email = %s, address = %s WHERE id = %s',
            (name, email, address, id))
        self.conn.commit()

    #     delete data
    def delete_data(self, id):
        self.instance.execute('DELETE FROM students WHERE id = %s', (id,))
        self.conn.commit()

question = input("Do you want to insert data? (y/n) ")
if question == "y":
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    students = Students()
    students.insert_data(name, email, address)

if __name__ == '__main__':
    students = Students()
    students.create_table()
    print(students.select_data())
    students.delete_data(1)
