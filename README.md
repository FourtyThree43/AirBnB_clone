# AirBnB Clone

![Optional Text](hbnb.png)

## Table of Contents
- [Description-of-the-project](#description-of-the-project)
- [Installation](#installation)
- [Description-of-the-command-interpreter](#description-of-the-command-interpreter)
- [Usage](#usage)
- [Examples](#examples)
- [Project-Structure](#project-structure)
- [Packages](#packages)
- [Contributors](#contributors)
- [License](#license)

## Description of the project

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the [Airbnb Website](https://www.airbnb.com/).

You won’t implement all the features, but be implemented in phases. After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Installation

To Use the AIrBnB clone, clone the repository to your local machine and run the `console.py` file:

```bash
$ git clone https://github.com/FourtyThree43/AirBnB_clone.git
$ cd AirBnB_clone
$ ./console.py

```

## Description of the command interpreter

## Usage

Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Contributors

This program was written by `FourtyThree43` and `joyce-source`. See the [AUTHORS](AUTHORS) file for more information.

## License

The project is licensed under the MIT license. See the LICENSE file for more information.
