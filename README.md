### Aawards
### Description
##### Awaards is a web application where one can have their projects rated after creatring an account and posting them.
### Author
Murathe Isaac

![Landing page ss](https://raw.githubusercontent.com/Murathe/awards/master/media/screenshot.png)
### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python3
  - Install and activate virtual
  - Install Django
  - Setup Database (postgresql)
  

### Set up Process
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```.
  - ```python --version``` to confirm that python has been installed.

##### Git clone the project on your current directory by:
  - ```git clone https://github.com/Murathe/aawards.git```.
##### Open the project on your terminal:
  - ```atom . or code .``` , 
##### Move to your project directory:
  - ```cd Innstagram```.
##### Install virtual environment using python:
  - ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  
##### To open python shell:
  - ```python3.6``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After confirming you have all this
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)



### User Stories
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page

### Behavior Driven Development
##### The application should display photos.
##### When a user clicks on a photo, the photo should expand and the details of the photo to be displayed on a modal within the main page.
##### When a user enters a search term on the search input and submits it, then they should be able to get a result of what they are looking for or if the term does not exist, they should get a message to inform them.
##### When a user clicks on the copy button, then they should be able to have the image link copied to their machine clipboard.

### Technologies Used
1. Python
2. Django
3. PostgreSQL


### Licence
[MIT](LICENSE)

