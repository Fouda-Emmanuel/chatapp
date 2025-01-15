Simple Chat App

Welcome to the Chat App repository! This project is a Django-based real-time messaging application that allows users to communicate seamlessly.

## Features

- **Real-Time Messaging**: Send and receive messages instantly.
- **User Authentication**: Secure login and registration system.
- **Responsive Design**: Optimized for both desktop and mobile users.
- **Chat Rooms**: Join or create chat rooms for group discussions.
- **Admin Panel**: Manage users and chat rooms through the Django admin interface.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## Installation

Follow the steps below to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Fouda-Emmanuel/chatapp.git
   cd chatapp
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Project Structure

The project is organized as follows:

```
chatapp/
├── chatproj/          # Project configuration files
├── chat/              # Main chat application files
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── db.sqlite3         # SQLite database
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## Usage

1. Navigate to the homepage.
2. Register for a new account or log in.
3. Join an existing chat room or create a new one.
4. Start messaging in real time!

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request with a detailed description of your changes.


## Contact

For any inquiries or support, please reach out to:
- **Author**: Fouda Emmanuel
- **Email**: leoemmanuelson46@gmail.com

Thank you for using the Chat App!

