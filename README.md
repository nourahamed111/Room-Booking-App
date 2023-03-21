# MY FINAL PROJECT
A one or two sentence description of your project here.
        Room Booking App
- What does it do?  
 "This is a Flask web application that manages available time slots for different rooms.
    -When you login as User:
       You can see all the available Room and each room has it's details div(Title, Id and available Time) you can choose what time do you want and book the room and after that the time wiil deleted from json file and when all the time in the room are booked the details button will be booked and disabled.
    -When you login as Admin:
       you can only login when you enter the password(123456)
       you can add a new room which is added in the json file 
       you can also Reset the availability time to the rooms and if the room wna fully booked when you update the time the details button will return back and the user can booked this room again.

- What is the "new feature" which you have implemented that we haven't seen before?  
  Use Static Method.
  It Deleted data from the json file using the ID.
  It Updated data to the json file using the ID.
  Use jinja

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? 
List those here (if any).

## Project Checklist
- [X] It is available on GitHub.
- [X] It uses the Flask web framework.
- [X] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: redirect, render_template, request, json
- [X] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name:room.py
  - Line number(s):6
  - Name of two properties: id, title, description, image, available
  - Name of two methods:load_time_from_json, static method(get_details())
- [X] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [X] It uses modern JavaScript (for example, let and const rather than var).
- [X] It makes use of the reading and writing to a file feature.
- [X] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name:room.py
  - Line number(s):142
- [X] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name:room.py
  - Line number(s):18
- [X] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [X] It doesn't generate any error message even if the user enters a wrong input.
- [X] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [X] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.