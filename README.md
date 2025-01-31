1.Create and Activate a Virtual Environment

  `python -m venv myenv`

  `myenv\Scripts\activate`

2.Install Dependencies

  `pip install -r requirements.txt`

3.Apply Database Migrations

`python manage.py makemigrations`

`python manage.py migrate`

4.Create a Superuser (For Admin Panel)

`python manage.py createsuperuser`

5.Run the Development Server

`python manage.py runserver`

7. Access the Application

`Admin Panel → http://127.0.0.1:8000/admin/ (Login with the superuser credentials)`

`Product List → http://127.0.0.1:8000/`

`Place an Order → http://127.0.0.1:8000/order/`

`Order Success Page → http://127.0.0.1:8000/order/success/`
