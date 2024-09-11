

# Job Board System

A job board platform for job posting, categorization, user authentication, and more. The system is built with a full API, integrated with Docker, Celery, and Redis for background tasks, and enhanced with job filtering and notifications.

---

### Key Features:

#### **1. Job Posting:**
   - Add, update, and delete job listings with ease.

#### **2. Job Categorization:**
   - Organize and categorize job listings for better search and navigation.

#### **3. User Authentication:**
   - Secure user authentication system with login and logout functionality.
   - Roles for both job seekers and employers.

#### **4. Docker Integration:**
   - The entire system is containerized using Docker, making it portable and easy to deploy in any environment.

#### **5. Celery & Redis Integration:**
   - Background tasks like sending email notifications are handled using Celery and Redis.
   - Ensures efficient and reliable background job processing.

#### **6. Job Filtering:**
   - Search and filter jobs based on multiple criteria such as job title, location, and category.

#### **7. Notifications System:**
   - Users receive notifications for relevant job postings and updates.

#### **8. Full API:**
   - A comprehensive RESTful API is available for interacting with the platform.
   - Allows developers to integrate external systems with the job board, such as mobile applications or other web services.

---

### API Documentation

#### **User Authentication:**

1. **Sign Up**  
   `POST /api/signup/`  
   - Create a new user account.
   - **Request Body:**
     ```json
     {
       "username": "string",
       "email": "user@example.com",
       "password": "password123"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "User created successfully.",
       "user": {
         "id": 1,
         "username": "string",
         "email": "user@example.com"
       }
     }
     ```

2. **Login**  
   `POST /api/login/`  
   - Log in an existing user.
   - **Request Body:**
     ```json
     {
       "email": "user@example.com",
       "password": "password123"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Login successful.",
       "token": "your-auth-token"
     }
     ```

3. **User Profile**  
   `GET /api/user-profile/`  
   - Retrieve the profile information of the logged-in user.
   - **Headers:**
     ```http
     Authorization: Bearer your-auth-token
     ```
   - **Response:**
     ```json
     {
       "id": 1,
       "username": "string",
       "email": "user@example.com",
       "profile": {
         "bio": "string",
         "location": "string"
       }
     }
     ```

4. **Logout**  
   `POST /api/logout/`  
   - Log out the currently logged-in user.
   - **Headers:**
     ```http
     Authorization: Bearer your-auth-token
     ```
   - **Response:**
     ```json
     {
       "message": "Logout successful."
     }
     ```

5. **Forgot Password**  
   `POST /api/forgot-password/`  
   - Send a password reset link to the user's email.
   - **Request Body:**
     ```json
     {
       "email": "user@example.com"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Password reset link sent to email."
     }
     ```

6. **Reset Password**  
   `POST /api/reset-password/<token>/`  
   - Reset the user's password using a valid token.
   - **Request Body:**
     ```json
     {
       "new_password": "newpassword123"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Password has been reset."
     }
     ```

7. **Change Password**  
   `POST /api/change-password/`  
   - Change the logged-in user's password.
   - **Request Body:**
     ```json
     {
       "old_password": "oldpassword123",
       "new_password": "newpassword123"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Password changed successfully."
     }
     ```

---

#### **Job Listings:**

1. **List Jobs**  
   `GET /api/jobs/`  
   - Retrieve a list of all job postings.
   - **Response:**
     ```json
     [
       {
         "id": 1,
         "title": "Software Engineer",
         "category": "Engineering",
         "location": "Remote",
         "posted_date": "2024-09-11"
       },
       {
         "id": 2,
         "title": "Data Scientist",
         "category": "Data",
         "location": "New York",
         "posted_date": "2024-09-10"
       }
     ]
     ```

2. **Add Job**  
   `POST /api/jobs/add/`  
   - Create a new job posting.
   - **Request Body:**
     ```json
     {
       "title": "Software Engineer",
       "category": "Engineering",
       "location": "Remote",
       "description": "We are looking for a software engineer..."
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Job created successfully.",
       "job": {
         "id": 1,
         "title": "Software Engineer",
         "category": "Engineering",
         "location": "Remote",
         "description": "We are looking for a software engineer..."
       }
     }
     ```

3. **Job Details**  
   `GET /api/jobs/<slug>/`  
   - Retrieve details of a specific job posting.
   - **Response:**
     ```json
     {
       "id": 1,
       "title": "Software Engineer",
       "category": "Engineering",
       "location": "Remote",
       "description": "We are looking for a software engineer...",
       "posted_date": "2024-09-11"
     }
     ```

---

### Authentication:

Most API endpoints require the user to be authenticated. Ensure that you include the `Authorization: Bearer your-auth-token` header in your requests where necessary.

---

### Technologies Used:

- **Django** – Backend framework for building the web application.
- **Django REST Framework** – For building a full RESTful API.
- **Celery & Redis** – For handling background tasks and message queuing.
- **Docker** – For containerization and deployment.
- **SQLite** – Default database (can be swapped for PostgreSQL or MySQL).
- **Bootstrap** – For front-end design and responsiveness.

---

### Installation:

#### 1. **Clone the Repository:**

   ```sh
   git clone https://github.com/OmarMuhammmed/Job-board.git
   cd Job-board
   ```

#### 2. **Install Dependencies:**

   - **With Docker** (Recommended):
   
     The project is fully containerized using Docker. Ensure you have Docker installed, then run:

     ```sh
     docker-compose up --build
     ```

   - **Without Docker** (Manual Installation):
   
     If you prefer not to use Docker, follow these steps:

     1. Install the Python dependencies:
        ```sh
        pip install -r requirements.txt
        ```

     2. Run database migrations:
        ```sh
        python manage.py migrate
        ```

     3. Start the application:
        ```sh
        python manage.py runserver
        ```

#### 3. **Start Celery & Redis:**

   Celery is used for background tasks, and Redis acts as the message broker:

   - To start the Celery worker:
     ```sh
     celery -A Job-board worker -l info
     ```

   - Ensure Redis is running. If using Docker, Redis will start automatically. Otherwise, start Redis manually on your system.

#### 4. **Create a Superuser (Admin):**

   To access the Django admin panel for managing job posts, users, and more, create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

---

### License:

This project is licensed under the MIT License.

---

### Contact:

For any inquiries, please contact Omar Mohammed at `amorey2006@gmail.com`.