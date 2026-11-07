# 📒 Contact Book

A simple command-line (CLI) contact manager written in Python.
This project is built as a practice exercise for object-oriented programming, CRUD operations, and the `prettytable` library.

## ✨ Features

- Add a new contact with a unique ID
- Update a contact's name, phone, and email
- View all contacts in a formatted table
- Delete a contact by ID
- Simple interactive menu in the terminal

## 📦 Requirements

- Python 3.8 or higher
- `prettytable` library

## 🚀 Installation

```bash
git clone git@github.com:Mahdi-Vm630/contact_book.git
cd contact_book
pip install prettytable
```

## ▶️ Usage

```bash
python source/app.py
```

## 🗂 Project Structure

```
contact_book/
├── source/
│   └── app.py          # ContactBook class and main menu
├── README.md
└── requirements.txt    
```

## 🖥 Example

```
welcome to contacts book application!
1. Add contact
2. Edit contact
3. View contact
4. Delete contact
5. Quit

please choose an option: 1
Enter contact id: 1
Enter contact name: Ali
Enter contact phone: 09121234567
Enter contact email: ali@example.com
Contact added successfully!
```

Output of the "View contact" option:

```
+----+------+-------------+-----------------+
| Id | Name |    Phone    |      Email      |
+----+------+-------------+-----------------+
| 1  | Ali  | 09121234567 | ali@example.com |
+----+------+-------------+-----------------+
```

## 📄 License

This project is released under the MIT License.