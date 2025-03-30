# littlelemon-backend-capstone

### **Project Overview**

The LittleLemon backend is a Django-based web application designed as part of the Meta Back-End Developer Capstone course. This project simulates a restaurant's backend system, providing API functionalities for menu items, table bookings, and user registration/authentication. The application integrates with a MySQL database to store and retrieve data dynamically.


## **Features**

- **Static HTML Pages**: Provides basic restaurant information.
- **Menu API**: Allows users to view available dishes from the menu.
- **Table Booking API**: Enables users to make reservations for tables.
- **User Authentication and Registration**: Supports new user registrations, login, and token-based authentication.
- **MySQL Database Integration**: All data is stored in a MySQL database.
- **Unit Tests**: Includes tests to ensure that key functionalities (models, views) are working as expected.


## **Setup**

Follow the steps below to get the LittleLemon backend up and running on your local machine.

### **Prerequisites**

- Python 3.8 or higher
- MySQL
- Virtual Environment (optional but recommended)



### **Step 1: Clone the repository**

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/freshwaterlemon/littlelemon-backend-capstone.git
cd littlelemon-backend-capstone
```

### Step 2: Set up a virtual environment
Create a virtual environment
```bash
python3 -m venv venv
```
Activate the virtual environment

###### On Windows
```bash
venv\Scripts\activate
```
###### On macOS/Linux
```bash
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL Database
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 5: Run Migrations
After setting up the database, apply the migrations to set up your database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser
To access the Django admin panel, you’ll need to create a superuser:
```bash
python manage.py createsuperuser
```

### Step 7: Start the Development Server
Now that everything is set up, you can start the Django development server:
```bash
python manage.py runserver
```

### Step 8: Test the APIs
#### The API endpoints can be tested using tools like Postman or Insomnia. Some of the main API routes are:

#### Authentication

> ###### Register a User  
Endpoint: /auth/users/  
Method: POST  
Description: Register a new user with username, password, and email.

> ###### Login  
Endpoint: /auth/token/login/  
Method: POST  
Description: Obtain an authentication token using username and password.

> ###### Logout  
Endpoint: /auth/token/logout/  
Method: POST  
Description: Logout the user and invalidate the token.

#### Menu API

> ###### Get All Menu Items
Endpoint: /restaurant/menu/
Method: GET
Description: Retrieve a list of all menu items.

> ##### Create a Menu Item  
Endpoint: /restaurant/menu/  
Method: POST  
Description: Add a new menu item to the restaurant's menu.

> ##### Get Single Menu Item  
Endpoint: /restaurant/menu/<int:pk>/  
Method: GET  
Description: Retrieve details of a specific menu item by its ID.

> ##### Update a Menu Item  
Endpoint: /restaurant/menu/<int:pk>/  
Method: PUT or PATCH  
Description: Update details of a specific menu item.

> ##### Delete a Menu Item
Endpoint: /restaurant/menu/<int:pk>/  
Method: DELETE  
Description: Delete a specific menu item from the menu.

#### Table Booking API

> ##### Get All Bookings  
Endpoint: /restaurant/booking/tables/  
Method: GET  
Description: Retrieve a list of all table bookings.

> ##### Create a Booking  
Endpoint: /restaurant/booking/tables/  
Method: POST  
Description: Create a new table booking.

> ##### Get Single Booking  
Endpoint: /restaurant/booking/tables/<int:pk>/  
Method: GET  
Description: Retrieve details of a specific booking by its ID.

> ##### Update a Booking  
Endpoint: /restaurant/booking/tables/<int:pk>/  
Method: PUT or PATCH  
Description: Update details of a specific booking.

> ##### Delete a Booking  
Endpoint: /restaurant/booking/tables/<int:pk>/  
Method: DELETE  
Description: Delete a specific booking.

#### Notes
1. All protected endpoints require an authentication token:
```text
Authorization: Token <YOUR_AUTH_TOKEN>
```
2. Use the /auth/token/login/ endpoint to obtain an authentication token after registering or logging in.
3. Endpoints follow RESTful principles and return appropriate HTTP status codes for success and error scenarios.


### Testing
To run the unit tests for models and views:
```bash
python manage.py test
```

---

