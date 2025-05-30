# 📚 Library Management System

A simple command-line based **Library Management System** built with **Python** and **SQLite**. This project supports managing books, students, and issuing/returning books, designed for educational or small library setups.

## 🚀 Features

- Add new students and books
- Issue books to students
- Return books with tracking
- Search for students and books
- View individual book history
- Easy-to-use CLI menu

## 📁 Tables Used

- `all_books`: Stores book details
- `all_stud`: Stores student records
- `all_issued`: Tracks issued books and return dates

## 🛠️ Technologies

- Python 3
- SQLite (file-based database)

## ⚙️ How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/siddhantrajguru/Library-Management-System.git
    cd library-management-system
    ```

2. Run the script:

    ```bash
    python main.py
    ```

3. Follow the on-screen menu to operate the library system.

> **Note**: Uncomment `create_all_tables()` if running the app for the first time to create necessary tables.

## 📌 Improvements You Can Make

- Add GUI using Tkinter or PyQt
- Add login/authentication for admin
- Handle input errors more gracefully
- Export issued book records to CSV

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
