import sqlite3
from customer import Customer

# If we need an in-memory database use ":memory:"
# each time our application runs database will be flush from
# the RAM and create new database.
connection = sqlite3.connect(':memory:')
#connection = sqlite3.connect('customer.db')

# A cursor allows us to execute SQL commands. We can create a cursor 
# by executing the cursor() function of our connection object.
cursor = connection.cursor()

'''
I use triple quotes for wrapping the SQL command. We called it a “docstring”. 
The benefit of using docstring is that it allows us to write string 
values in multiple lines.
'''
cursor.execute("""CREATE TABLE customer(
    first_name text,
    last_name text,
    age integer,
    city text,
    country text
)""")

'''
After creating the table, we need to commit our changes to the database. 
For that, we use the commit() method. Finally, close the database connection 
using the close() method.
'''

connection.commit()


def create_customer(customer):
    with connection:
        cursor.execute("INSERT INTO customer VALUES (:first, :last, :age, :city, :country)", 
        {'first':customer.first_name, 'last':customer.last_name,
         'age':customer.age, 'city':customer.city, 'country':customer.country})

def get_customers(city):
    cursor.execute("SELECT * FROM customer WHERE city=:city", {'city':city})
    return cursor.fetchall()

def update_city(customer, city):
    with connection:
        cursor.execute("""UPDATE customer SET city=:city 
        WHERE first_name=:first AND last_name=:last""",
        {'first':customer.first_name, 'last':customer.last_name, 'city':city})

def delete_customer(customer):
    with connection:
        cursor.execute("DELETE FROM customer WHERE first_name=:first AND last_name=:last",
        {'first':customer.first_name,'last':customer.last_name})


customer_1 = Customer('john', 'doe', 30, 'perth', 'Australia')
customer_2 = Customer('sara', 'migel', 25, 'perth', 'Australia')

create_customer(customer_1)
create_customer(customer_2)

customers = get_customers('perth')

print(customers)

update_city(customer_1,'sydney')

delete_customer(customer_2)

print(get_customers('perth'))
print(get_customers('sydney'))

connection.close()