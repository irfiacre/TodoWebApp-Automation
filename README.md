# To do App Automation tests

This is a simple project to automate the tests for this [To Do App](https://qa-test-todo-fa6994894c02.herokuapp.com/):
The tests include adding items, marking them as completed, and deleting them.

## Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

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

| Test Name                         |                                                                                 Note |
|-----------------------------------|-------------------------------------------------------------------------------------:|
| test_adding_a_new_to_do_item      |                          Test opens the web app and add a new item on the to do list |
| test_mark_to_do_item_as_completed | Test opens the web app, add a new item on the to do list, and then marks it as done. |
| test_delete_to_do_item            |       Test opens the web app, add a new item on the to do list, and then deletes it. |
| test_combined_tests               |                                               Combines all the above mentioned tests |

NB: After each test(s) execution a report will be created in the `report` directory(folder).

### Contributors
[IRADUKUNDA Allelua Fiacre](https://github.com/irfiacre)
