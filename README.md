# PROJECT NAME

Instagram Clone - Animated Fiesta

# Author

Collins Kiprutoh

# Description

This is a clone of Instagram. You can post, comment and view pictures posted on this App just like on Instagram.

# User Story

1. Users need to Sign in to the application to start using.

2. Users can view different photos.

3. Users can click on a single photo to view it.

4. Users can search for different photos.

5. Users can Upload their pictures to the application.

6. Users can see their profile with all their picture.

7. Users can view a picture and leave a comment on it.

# Installion and Setup instructions

1. Clone this repo: git clone https://github.com/wizzicollo/animated-fiesta.git.

2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

3. Open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

4. To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
5. On your terminal,Create database gallery using the command below.

CREATE DATABASE instagram; 
**if you opt to use your own database name, replace instagram your preferred name, then also update settings.py variable DATABASES > NAME
6. Migrate the database using the command below

python3.6 manage.py migrate
7. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver
8. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

9. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

10. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

11. To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
12. On your terminal,Create database gallery using the command below.

CREATE DATABASE instagram; 

13. Migrate the database using the command below

python3.6 manage.py migrate
14. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


# Running the tests
Use the command given below to run automated tests.

    python manage.py test instapp
    

# TECHNOLOGIES Used

Django - web framework used
Javascript - For DOM(Document Object Manipulation) scripts
HTML - For building Mark Up pages/User Interface
CSS - For Styling User Interface

# Contacts

kiprutohcollo@gmail.com

# live link

https://instagramfiesta.herokuapp.com/

# License
This project is licensed under the MIT License - see the LICENSE.md file for details