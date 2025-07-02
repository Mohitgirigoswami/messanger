# Messanger

## Project Title
Messanger: A Real-time Messaging Application

**GitHub Repository:** [https://github.com/Mohitgirigoswami/messanger](https://github.com/Mohitgirigoswami/messanger)

## Description
Messanger is a modern, real-time web-based messaging application designed to facilitate instant communication between users. Built with a robust Flask backend and a dynamic frontend powered by Flask-SocketIO and Tailwind CSS, it offers a seamless and interactive user experience. The application supports user authentication, one-on-one messaging, user profile management, and friend management, making it a comprehensive platform for personal communication.

If you find this project useful, please consider starring the repository! ⭐

## Features
*   **User Authentication:** Secure user registration, login, and logout functionalities with password hashing.
*   **Real-time Messaging:** Instant message delivery and display using WebSockets (Flask-SocketIO).
*   **User Profiles:** Customizable user profiles including username, first name, last name, bio, and avatar selection.
*   **Friend Management:** Ability to search for users, add them as friends, and manage friend lists.
*   **One-on-One Chat:** Dedicated chat interfaces for private conversations with friends.
*   **Database Integration:** Persistent storage of user data, messages, and friend relationships using SQLite (default) and SQLAlchemy.
*   **Responsive Design:** Modern and responsive user interface built with Tailwind CSS.

## Technologies Used
*   **Backend:**
    *   Python 3
    *   Flask: Web framework
    *   Flask-SocketIO: WebSocket integration for real-time communication
    *   Flask-SQLAlchemy: ORM for database interaction
    *   SQLAlchemy: Python SQL toolkit and Object Relational Mapper
    *   Werkzeug: Comprehensive WSGI utility library (for security features like password hashing)
    *   Flask-Session: Server-side session management
    *   Flask-WTF: Integration with WTForms for CSRF protection
    *   Eventlet: Asynchronous networking library for SocketIO
*   **Frontend:**
    *   HTML5
    *   CSS3 (Tailwind CSS for utility-first styling)
    *   JavaScript
*   **Database:**
    *   SQLite (default, configured via `DATABASE_URL` environment variable)
*   **Build Tools:**
    *   Node.js & npm: For managing frontend dependencies and Tailwind CSS CLI
    *   Tailwind CSS CLI: For compiling and minifying CSS
*   **Version Control:**
    *   Git

## Installation

To get a local copy up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohitgirigoswami/messanger.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd messanger
    ```
3.  **Set up Python environment:**
    *   Create a virtual environment (recommended):
        ```bash
        python -m venv flaskenv
        ```
    *   Activate the virtual environment:
        *   **Windows:**
            ```bash
            .\flaskenv\Scripts\activate
            ```
        *   **macOS/Linux:**
            ```bash
            source flaskenv/bin/activate
            ```
    *   Install Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```
5.  **Build Tailwind CSS:**
    ```bash
    npm run build:css
    ```
    This command compiles the Tailwind CSS from `app/static/css/input.css` to `app/static/css/output.css`.

## Usage

1.  **Configure Environment Variables:**
    *   Create a `.env` file in the root directory of the project.
    *   Copy the contents of `.env.example` into your new `.env` file.
    *   Update the values for `SECRET_KEY`, `WTF_CSRF_SECRET_KEY`, and `DATABASE_URL` (if you want to use a database other than the default SQLite).

2.  **Run the Flask application:**
    ```bash
    python run.py
    ```
    This will start the Flask development server and the SocketIO server, typically on `http://0.0.0.0:8000`.

3.  **Access the Application:**
    Open your web browser and navigate to `http://localhost:8000`.

    *   **Registration:** If you are a new user, register for an account.
    *   **Login:** Log in with your credentials.
    *   **Home:** View your friends and start new conversations.
    *   **Search:** Find other users by their username.
    *   **Profile:** View and edit your profile information, including changing your avatar.

## Demo

You can access a live demo of the Messanger application here: [https://messanger-j3aa.onrender.com/](https://messanger-j3aa.onrender.com/)

## Configuration

Environment variables are used for sensitive information and flexible configuration. A `.env.example` file is provided as a template.

*   **`.env` file:** Create this file in the project root.
*   **`SECRET_KEY`:** A strong, random string used by Flask for session management and other security-related operations. **Crucial for production environments.**
*   **`WTF_CSRF_SECRET_KEY`:** A separate strong, random string used by Flask-WTF for CSRF protection. **Crucial for production environments.**
*   **`DATABASE_URL`:** Specifies the database connection string. Defaults to a SQLite database file (`instance/messenger.db`). Example for PostgreSQL:
    ```
    DATABASE_URL="postgresql://user:password@host:port/database_name"
    ```

## Project Structure

```
.                                   # Project root
├── .git/                           # Git version control directory
├── app/                            # Main Flask application source code
│   ├── auth/                       # Authentication blueprint (login, register, logout)
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/                       # Main application blueprint (home, search, message, profile)
│   │   ├── __init__.py
│   │   ├── events.py               # SocketIO event handlers for real-time communication
│   │   └── routes.py
│   ├── static/                     # Static assets (CSS, JavaScript, images)
│   │   ├── css/
│   │   │   ├── input.css           # Tailwind CSS input file
│   │   │   └── output.css          # Compiled Tailwind CSS output file
│   │   ├── images/
│   │   └── js/
│   ├── templates/                  # Jinja2 HTML templates
│   ├── __init__.py                 # Flask app creation and configuration
│   ├── models.py                   # SQLAlchemy database models (Users, Message, user_friend, Avtar_links)
│   └── utils.py                    # Utility functions (e.g., password strength, username validation)
├── flaskenv/                       # Python virtual environment
├── instance/                       # Instance-specific files (e.g., SQLite database file)
├── node_modules/                   # Node.js dependencies installed by npm
├── .env.example                    # Example environment variables file
├── .gitignore                      # Specifies intentionally untracked files to ignore by Git
├── messanger.code-workspace        # VS Code workspace file
├── package-lock.json               # Records the exact dependency tree for Node.js projects
├── package.json                    # Node.js project metadata and dependencies
├── procfile                        # Process file for deployment (e.g., Heroku, defines commands to run)
├── requirements.txt                # Python dependencies (currently unreadable, manual installation required)
└── run.py                          # Entry point to run the Flask application
```

## Contributing
Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Contact/Support
For any questions or support, please open an issue on the GitHub repository: [https://github.com/Mohitgirigoswami/messanger/issues](https://github.com/Mohitgirigoswami/messanger/issues)
