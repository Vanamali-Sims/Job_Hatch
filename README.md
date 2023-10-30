# Job Hatch - Job Hunter and Recruiter Platform

Job Hatch is a web application designed to bridge the gap between job hunters and recruiters. It provides a dynamic platform where job seekers can connect with job opportunities and recruiters can find suitable candidates. The application is built using Django for the backend, HTML, CSS with Bootstrap, and JavaScript for the frontend. It utilizes SQLite3 for its database and offers valuable resources for students to upskill themselves in the platforms of their choice. Job Hatch supports two types of logins: recruiter and candidate.

## Features

### For Job Seekers (Candidates)

- **Create and Manage Profiles:** Job seekers can create and manage their profiles, showcasing their skills, experiences, and interests.

- **Browse Job Listings:** Candidates can browse through a variety of job listings and search for positions that align with their qualifications and career goals.

- **Apply to Jobs:** Candidates can apply to job listings directly through the platform.

- **Resources for Upskilling:** Job Hatch provides resources, including courses and tutorials, to help candidates upskill and prepare for job applications.

### For Recruiters

- **Post Job Listings:** Recruiters can post job listings with detailed job descriptions and requirements.

- **Search for Candidates:** Recruiters can search for potential candidates using various filters and criteria.

- **Manage Job Listings:** Recruiters can edit, update, or remove job listings as needed.

### General Features

- **User Authentication:** Job Hatch supports two types of logins: recruiter and candidate.

- **Responsive Interface:** The frontend is designed with Bootstrap, providing a responsive and user-friendly interface.

- **Dynamic and Interactive:** The application is dynamic, offering real-time updates and interactions to enhance the user experience.

- **SQLite3 Database:** The platform uses SQLite3 for the database, ensuring data integrity and security.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/job-hatch.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application by opening a web browser and navigating to [http://localhost:8000](http://localhost:8000).

## Configuration

You can configure the application by modifying the settings in the `jobhatch/settings.py` file. Update database settings, email settings, and other configuration options as needed.

## Usage

1. Create an account based on your role (Recruiter or Candidate).

2. Log in to the portal using your credentials.

3. For Candidates: Create and manage your profile, browse job listings, apply to jobs, and utilize the available resources to upskill.

4. For Recruiters: Post job listings, search for candidates, manage job listings, and communicate with potential candidates through the messaging system.

5. Regularly check for updates and new job opportunities.
