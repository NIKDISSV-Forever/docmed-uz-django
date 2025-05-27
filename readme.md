# DocMed-Uz Platform

**Empowering Medical Professionals with Advanced Learning and Resources**

DocMed-Uz is a comprehensive Django-based web platform designed to provide medical professionals and students with access to high-quality educational courses, specialized modules, and up-to-date medical information. Our goal is to facilitate continuous learning and professional development within the medical community.

---

## ✨ Core Features

*   **Interactive Course Management:** Curated courses covering diverse medical specializations.
*   **Modular Learning:** Individual modules for focused learning, which can be part of larger courses or standalone.
*   **User Progress Tracking:** Monitor completion of video materials, downloaded files, and test results for modules and courses.
*   **Certificate Generation:** Automated certificate issuance upon successful completion of courses or modules.
*   **Rich Content:** Integration of video lectures, downloadable materials (PDFs, documents), and relevant drug information.
*   **Expert Speakers:** Profiles and contributions of leading medical experts.
*   **Tagging System:** Efficient content organization and discovery through tags for courses, modules, and drugs.
*   **RESTful API:** Comprehensive API for seamless integration with other services or mobile applications.
*   **User Authentication & Authorization:** Secure access control for users and administrators.

---

## 🛠️ Technology Stack

*   **Backend:** Python 3.13, Django 5.1, Django REST Framework
*   **Database:** SQLite (for development, configurable for PostgreSQL/MySQL in production)
*   **Frontend:** HTML, Bootstrap 5, JavaScript
*   **Dependency Management:** Poetry

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.13+
*   Poetry (Python dependency manager)

### Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NIKDISSV-Forever/docmed-uz-django
    cd docmed-uz-django
    ```

2.  **Install dependencies using Poetry:**
    ```bash
    poetry install --no-root
    ```

3.  **Activate the virtual environment:**
    ```bash
    poetry shell
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    ```

5.  **Load initial fixture data:**
    ```bash
    python manage.py loaddata fixtures.json
    ```

6.  **Create a superuser account:**
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the prompts to set username, email, and password)

7.  **Run the development server:**
    ```bash
    python manage.py runserver localhost:8000
    ```

### Accessing the Application

*   **Main User Interface:**
    *   Courses: `http://localhost:8000/courses/`
    *   Standalone Modules: `http://localhost:8000/courses/modules/`
*   **Admin Panel:** `http://localhost:8000/admin/`
*   **API Endpoints:**
    *   Courses API: `http://localhost:8000/courses/api/`
    *   Modules API: `http://localhost:8000/courses/modules/api/`

    Specific API endpoints include:
    *   `/courses/api/tags/`
    *   `/courses/api/speakers/`
    *   `/courses/api/drugs/`
    *   `/courses/api/courses/`
    *   `/courses/api/attaches/`
    *   `/courses/modules/api/list/` (for Modules)
    *   `/courses/modules/api/timecodes/`
    *   `/courses/modules/api/progress/`
    *   `/courses/modules/api/sponsors/`

---

## 📄 License

This project is licensed under the terms of the custom license. Please see the [LICENSE](./LICENSE) file for full details.
Third-party libraries and dependencies included in this project are subject to their own respective licenses.
