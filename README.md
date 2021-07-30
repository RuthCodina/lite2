# FLASK-PYTHON Y REACT APP

The application that contains the present code was developed with Python in the back end using the Flask library. The front end was developed with React JS and the styles were developed with bootswatch, which saves some bootstrap themes.

The database was developed with MongoDB. The database is called lite2, which you can connect to using MongoDB Compass, by copying the code from line 8 of the backend/app.py file.

However, you can rename the database, create a new one and connect to it, but remember to start mongodb in the console using the mongod command. Of course if you already have mondodb installed, if not you will need to install it.



## Endpoints

[] /users to get all Users and create new onces
[] /user/id to get, update and delete a user by id

### important!

Phyton runs on the port, so all the React routes was created using it. if your Python console, sttablish other connection, remember change it to don't crash de app.
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

### usage

When you are viewing the application, the first screen will be [http://localhost:5000](http://localhost:5000), where you can find the navbar and the form to create the user, use it and create your first character.

  <div>
  <img height="500" src="frontend/src/assets/create user form.jpg" />
  </div> 
you will also have the opportunity to click on 'User List' and there you will be able to visualize the list of users you have just created and from there you will have the opportunity to delete them and click on 'edit' to edit it After clicking on edit you will be directed to the edit form, which takes into account the id of the user you clicked and if you click on get info, it will fill the form with the data stored in the database of that user, in order to remind you and then you can change what you want to change, 'update' and then return to the list of users to delete, view or edit another user.
  <div>
     <img height="500" src="frontend/src/assets/userList.jpg" />
  </div>

After clicking on edit you will be directed to the edit form, which takes into account the id of the user you clicked and if you click on get info, it will fill the form with the data stored in the database of that user, in order to remind you and then you can change what you want to change, 'update' and then return to the list of users to delete, view or edit another user.

  <div>
     <img height="500" src="frontend/src/assets/updateUser.jpg" />
  </div>
