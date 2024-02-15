# Home Library Management System

The Home Library Management System is a web-based application designed to help book enthusiasts organize and manage their personal book collections. This system provides users with the ability to catalog their books, track their reading progress, and maintain a personalized reading log.

## Features

- **User Authentication**: Secure login and registration functionality for managing personal accounts.
- **Book Cataloging**: Add, edit, and delete books from your personal library with details such as title, author, ISBN, publication year, and format (e.g., Hardcover, Paperback, Ebook).
- **Reading Log**: Maintain a log of books you've read along with the date read and personal notes or thoughts about the book.
- **Search and Filter**: Easily search for books in your library and filter them by various criteria like read status, format, or publication year.

## Technologies Used

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Bootstrap**: For responsive design and stylish UI components.
- **SQLite**: As the default database for development. (Can be configured to use other databases for production.)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.8 or newer)
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine.
git clone https://github.com/crandquist/Home-Library-Management-System
2. Navigate into the project directory.
cd HomeLibraryManagementSystem
3. Create a virtual environment.
python -m venv myvenv
4. Activate the virtual environment.
- On Windows:
  ```
  myvenv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source myvenv/bin/activate
  ```
5. Install the required dependencies.
pip install -r requirements.txt
6. Migrate the database.
python manage.py migrate
7. Start the development server.
python manage.py runserver
8. Visit `http://127.0.0.1:8000/` in your web browser to view the application.

## Contributing

We welcome contributions to this project! Please consider the following steps to contribute:

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Django documentation and community for invaluable resources.
- Bootstrap team for their excellent front-end framework.

This project was built using the DjangoX starter project.
