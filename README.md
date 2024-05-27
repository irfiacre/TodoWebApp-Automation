# To do App Automation tests

This is a simple project to automate the tests for this [To Do App](https://qa-test-todo-fa6994894c02.herokuapp.com/):
The tests include adding items, marking them as completed, and deleting them.

## Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

### 0. Clonning the repo
```sh
$ git clone https://github.com/irfiacre/TodoWebApp-Automation.git
```
### 1. Creating and activating a virtual environment
```sh
$ python3 -m venv venv   (If you have python version 3.11*, replace python3 with python3.11)
# Activate the virtual environment
$ source venv/bin/activate (or for windows use "source venv\Scripts\activate")
```

### 2. Install dependencies
```sh
pip3 install -r requirements.txt
```

### 3. How to Run the project
```sh
 pytest tests_automations.py -v
```
#### To run an individual test
```sh
 $ pytest tests_automations/test_combined_automation.py::<test_name> -v
```

## Test Descriptions

| Test Name                   | Note                                                     |
|-----------------------------|:---------------------------------------------------------|
| test_add_new_items          | Test scenarios for adding item(s) to the to do list      |
| test_mark_item_as_completed | Test scenarios for marking item(s) as completed          |
| test_delete_items           | Test scenarios for deleting item(s) from the list        |
| test_combined_tests         | Test scenario that contains all actions combined         |

NB: After each test(s) execution a report will be created in the `report` directory(folder).
