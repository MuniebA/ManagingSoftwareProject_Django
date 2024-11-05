# ManagingSoftwareProject_Group1

!!! IMPORTANT !!!
We move our project to the branch named MinKhant because we decided to start fresh in the middle of sprint 1 because main is too hard to manage and messy

Please navigate to that branch to perform the step below or download the code from that branch

This project uses Django framework which requires preinstallation on different python library. Below are the dependacies that need to be install beforehand.
1. You need to clone this repository first inside your PC / download and extract to a place
2. You need to create a virtual environment first before running the project, ensure you have python install on your PC
   2.1 Navigate to the place where you save the repository in Command Prompt
   ![image](https://github.com/thadted/ManagingSoftwareProject_Group1/assets/136876851/fd3fd043-c72f-4b55-ad98-9798b39cf079)
   In my case is in this directory
   2.2 Create the virtual environment
   ![image](https://github.com/thadted/ManagingSoftwareProject_Group1/assets/136876851/b8807794-7863-4841-87fa-018e6f6db97f)
   2.3 Activate the environment
   ![image](https://github.com/thadted/ManagingSoftwareProject_Group1/assets/136876851/d0d7a373-4ca5-463b-ab55-c3322f9c4970)
   After pressing enter it should looks like this:
   ![image](https://github.com/thadted/ManagingSoftwareProject_Group1/assets/136876851/fbcf5f82-d580-409e-a31b-e9cb3ee2907b)
   2.4 Install Django and the python library, below are the command:
   pip install django
   pip install plotly
   python -m pip install Pillow
    
3. After all the setting up, you can try running the project, first you need to apply the migrations to initialize the database:
   python manage.py makemigrations (this will create the migration file)
   python manage.py migrate (this will apply the migrations)

  Troubleshoot:
  If Migrations failed:
  1. Delete db.sqlite3 file in the folder if it exist and try repeat step 3 again
  2. Delete all python file in foodcateringapp>migrations  and users>migrations

4. After the migration you can run the project by using the following command:
   python manage.py runserver

   ![image](https://github.com/thadted/ManagingSoftwareProject_Group1/assets/136876851/1207cef8-970b-4acb-8c0e-b8a6bd0a4e57)
   This means the project is successful running

5. Go to the link that are stated there in the browser

6. Create default admin account, use the code provided below
   py manage.py createsuperuser

   Follow the steps and the admin account will be created
   
  
