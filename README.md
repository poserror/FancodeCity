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

Project Structure:
Copy code
├── services/
│   ├── base_service.py        # Handles the base API request logic
│   ├── user_service.py        # Service to handle user-related logic
│   └── todo_service.py        # Service to handle todo-related logic
├── test_fancode_users.py      # Contains test cases for FanCode and non-FanCode users
├── README.md                  # Project documentation
├── requirements.txt           # Project dependencies

Service Files:
  user_service.py:
  - Fetches users from the API.
  - Filters users based on whether they belong to the "FanCode" city using latitude and longitude criteria.
  
  todo_service.py:
  - Fetches todos for a specific user.
  - Calculates the completion percentage of the user's tasks.
  
  base_service.py
  - GET/POST/PUT/DELETE endpoints

Test Files:
test_fancode_users.py  
- Contains two test cases
- Tests that users from the FanCode city have completed more than 50% of their tasks.

Installation
1) Clone the repository: git clone https://github.com/your-username/fancode-todo-automation.git
2) cd fancode-todo-automation
3) pip install -r requirements.txt
4) To run the test cases, use pytest with the following command:
5) pytest test_fancode_users.py --disable-warnings -s
   (The -s option ensures that the output from print() statements is shown.)
