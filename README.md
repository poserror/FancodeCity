# FancodeCity

FanCode User Todo Automation
- This project automates the process of testing whether user is in a FanCode city, should have completed more than 50% of their todo tasks. 
- The users' locations are filtered based on latitude and longitude, and their todos are fetched and analyzed using pytest.

Scenario
Task: All users of the city FanCode should have more than half of their todo tasks completed.

Criteria:
A user belongs to the FanCode city if their latitude is between -40 to 5, and their longitude is between 5 to 100.
Users' tasks are fetched from a /todos API.
The completion percentage for each user's tasks is calculated.
If a user has completed more than 50% of their tasks, they pass the test.

Key highlight:
- The structure is such that any new testcase can be easily automated by using the services.

Service Files:
  user_service.py:
  - Fetches users from the API.
  - Filters users based on whether they belong to the "FanCode" city using latitude and longitude criteria.
  
  todo_service.py:
  - Fetches todos for a specific user.
  - Calculates the completion percentage of the user's tasks.
  
  base_service.py
  - GET/POST/PUT/DELETE endpoints

Test:
test_fancode_users.py  
- Contains two test cases
- Tests that users from the FanCode city have completed more than 50% of their tasks.

Installation
1) Clone the repository: git clone https://github.com/your-username/fancode-todo-automation.git
2) cd fancode-todo-automation
3) python3 -m pip install -r requirements.txt
4) To run the test cases, use pytest with the following command:
   pytest test_fancode_users.py --disable-warnings -s
   (The -s option ensures that the output from print() statements is shown when running through pytest.)


Sample output
HP@LAPTOP-SQ3RMDF9 MINGW64 ~/Downloads/FanCode (main)
$ pytest test_fancode_users.py --disable-warnings -s
============================= test session starts =============================
platform win32 -- Python 3.12.2, pytest-6.2.5, py-1.11.0, pluggy-1.5.0
rootdir: C:\Users\HP\Downloads\FanCode
plugins: django-4.5.2, timeout-2.2.0
collected 1 item

test_fancode_users.py
Completion percentage for user Leanne Graham is 55.00000000000001%.

Completion percentage for user Chelsey Dietrich is 60.0%.

Completion percentage for user Clementina DuBuque is 60.0%.
.

============================== 1 passed in 1.98s ==============================


Additional Report: Visualize.py
How to run: 
python Visualize.py
It creates 2 png and a pdf file containing pie chart and a graph. It help in visualizing the data in a better way.