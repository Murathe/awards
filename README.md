### Gram (instagram)
### Description
##### Gram is a platform where users can display their photos forthe worldto see, they can also see other peoples photos.
### Author
Murathe Isaac

![image](https://user-images.githubusercontent.com/29546502/74370737-a7220f00-4de8-11ea-9400-0a3884fca4ff.png)

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python3
  - Install and activate virtual
  - Setup Database
  - Install Django

### Set up Process
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```.
  - ```python --version``` to confirm that python has been installed.

##### Git clone the project on your current directory by:
  - ```git clone https://github.com/Murathe/iinstagram.git```.
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
##### As a user, I would like to view different photos that interest me.
##### As a user, I would like to click on a single photo to expand it and also view the details of the photo.
##### As a user, I would like to search for different categories of photos.
##### As a user, I would like to copy a link to the photo to share with my friends.
##### As a user, I would like to view photos based on the location they were taken.

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

