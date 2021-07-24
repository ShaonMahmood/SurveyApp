# Project Title

A simple survey application powered by django

## Description

This project is based on the following requirements. 
* Create a SURVEY app in Django that will hold questions of three types: 

  - Text field type question
  - Radio type question
  - Checkbox multiple select
    
* Admin will be able to set up a survey, it’s questions, offered answer choices and a timer (for example 5 mins or 30 mins).
* No need to create any user management forms like login/logout etc. 
* For now the participant can login with the admin login form then can directly visit the url containing the survey list and can start a survey. (Only logged in users can see the survey list and participate in a survey).
* Ensure one user can participate in the survey only once.
* For each user when participating in the survey, create a survey session for that user and record answers & questions under that session so that the admin may review the survey later.
* During the survey the user should be able to navigate back and forth between the questions and change answers. 
* Show a timer anywhere in the survey and after the timer ends, end the survey immediately.
* Use bootstrap 4+ and any type of JS libraries or frameworks (jQuery should work fine alone). Just make a basic design for the app.

All the requirements are addressed accordingly.

## Getting Started

### Dependencies

* Latest version of Docker and Docker Compose 
* Any Operating system supporting docker

### Installing

* Clone the repo from this url
* From the terminal(powershell, bash etc) change the directory into the repo folder.

### Executing program

* Run the command below from the terminal.
```
   docker-compose up -d --build
```
* A superuser will be created automatically following the .env.dev file specification.
* Add surveys from the admin panel
* Create users with staff privileges for testing
* Go to http://localhost:8000/survey url for the dashboard.
* There on participate the survey
* Admin can see all the surveys answered, any other user sees only his/her answered surveys.
* A survey can be answered only once by a user.

To stop the containers with the volumes associated, type:
```
   docker-compose down -v
```

## Help

For any help give a mail to "mahmood.habib.cuet@gmail.com"

## Authors

Md Mahmood Bin Habib
[@Mahmood](https://github.com/ShaonMahmood)

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the [MIT] License

## Acknowledgments

Inspiration, code snippets, etc.
* [Awesome-article-for-survey-design](https://mattsegal.dev/django-survey-project.html)
* [Pyplane Quiz App](https://blog.pyplane.com/blog/django-and-javascript-quiz-app/)
* [Ajax calls](https://django.cowhite.com/blog/different-cases-of-sending-data-in-ajax-request-in-django/)