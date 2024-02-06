# GigaByte Careers Website

Welcome to GigaByte Careers Website! This is a web application developed using Flask and PostgreSQL to provide a platform for managing job listings and applications.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Job Listings**: Post and manage job openings easily.
- **Application Management**: Track and review job applications.
- **User Authentication**: Secure login and registration system for administrators and applicants.
- **Responsive Design**: Ensures a seamless experience across various devices.

## Requirements

Ensure you have the following dependencies installed before setting up the project:

- Python 3.x
- Flask
- PostgreSQL
- psycopg2

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/bugbreaker18/GigaByte-Careers-Website
    cd GigaByte-Careers-Website
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Database Configuration:**

    - Create a PostgreSQL database and update the Database Connection String with your database credentials.
    - Run the following command to set up the database:

        ```bash
        python database.py
        ```

6. **Run the Application:**

    ```bash
    flask run
    ```

7. **Access the Application:**

    Open your web browser and navigate to `http://localhost:<port_numer>`.

## Usage

- **Administrator Dashboard:**

    -Yet to be implemented

- **Applicant Experience:**

    - Users can register, log in, and apply for jobs.
    - Track application status and receive emails.

## Contributing

Feel free to contribute to the project. Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions are welcome.

## License

This project is licensed under the [MIT License](LICENSE).
