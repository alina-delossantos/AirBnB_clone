# Project: 0x00. AirBnB Clone.

`Release date: March-07-2022`

![hbnb](https://i.imgur.com/XyXPuZ9.png)

## 0x00.Table of contents
* [0x01 Introduction](#0x01-Introduction)
* [0x02 Environment](#0x02-Environment)
* [0x03 Installation](#0x03-Installation)
* [0x04 Testing](#0x04-Testing)
* [0x05 Usage](#0x05-Usage)
* [0x06 Authors](#0x06-Authors)

## 0x01 Introduction

-   School project to develop an Airbnb clone.
-   Our console is a command interpreter that performs the below tasks
    - create a new object
    - retrieve an object
    - performs a number of operations on an object
    - destroy an object

### Storage
All the classes are handled by our `Storage` engine within our `FileStorage` Class.

## 0x02 Environment
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

## 0x03 Installation
```bash
git clone https://github.com/Lulimsky/AirBnB_clone.git
```
change to the `AirBnB_clone` directory and run the below command:
```bash
 ./console.py
```
### Execution
Interactive mode
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

## 0x04 Testing
Tests are located within our `tests` folder.

### Python Unit Tests
* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```
### run test in interactive mode
```bash
echo "python3 -m unittest discover tests" | bash
```
### run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:
```bash
python3 -m unittest discover tests
```

## 0x05 Usage
* Start the console in interactive mode:
```bash
$ ./console.py
(hbnb)
```
* Use help to see the available commands:
```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```
* Quit the console:
```bash
(hbnb) quit
$
```

### Commands

* Create
> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*
```bash
create <class>
```
```bash
(hbnb) create BaseModel
7dhe56v4-b748-5df7-bf02-6754765f8765
(hbnb)
```

* Show
```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```
* Destroy
> *Deletes an instance of a given class with a given id and updates the JSON file*
```bash
(hbnb) create BaseModel
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy BaseModel 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show BaseModel 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```
* all
> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*
```bash
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```

## 0x06 Authors

> *Lucila Mociulsky & Alina de los Santos*
