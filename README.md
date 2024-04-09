# Project DAILY-MATE

## Introduction
Daily-mate project is a web application built using Django. It allows users to create, manage, and organize their daily notes and entries in a convenient manner. Users can register, log in, create, edit, and delete notes and daily entries, search for specific entries, and manage their profile.

## Installation
To run this project locally, follow these steps:
1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/artem-andreyev/DailyMate-project.git
    ```
3. Navigate to the project directory.
    ```bash
    cd /project_directory/
    ```
4. Install the required Python packages using pip.
    ```bash
    pip install -r requirements.txt
    ```
5. Start the Django development server.
    ```bash
    python manage.py runserver
    ```
6. Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the application.

## Features
- **User Authentication:** Users can register, log in, and log out securely.
- **Profile Management:** Users can manage their profiles, including adding a bio and avatar image.
- **Note Management:** Users can create, edit, and delete notes.
- **Daily Book:** Users can create, edit, and delete daily entries, categorized by emotions.
- **Search:** Users can search for specific entries using keywords.
- **Permissions:** Users can only manage their own notes and daily entries.

## Usage
1. **Registration:** Users can register for a new account by providing the necessary details.
2. **Login:** Registered users can log in using their credentials.
3. **Profile:** Users can manage their profiles by adding a bio and avatar image.
4. **Note Management:** Users can create, edit, and delete notes.
5. **Daily Book:** Users can create, edit, and delete daily entries, categorized by emotions.
6. **Search:** Users can search for specific entries using keywords.
7. **Logout:** Users can securely log out of their accounts.

## Contributors
This project was developed by Teodors Čalijs and Artjems Andrejev

## Development Environment
- **Django:** The web framework used for building the application.
- **Python:** The programming language used for backend development.
- **SQLite:** The default database system used by Django for development.
- **HTML/CSS:** Frontend technologies used for rendering views.
- **Git:** Version control system used for managing project files.

## Testing
This project includes unit tests to ensure the functionality of various components. To run the tests, use the following command:
```bash
python manage.py test
```
