# SpatialBlend-T31-CS425
## Senior Capstone Project

### Prerequisites
Before you begin, ensure you have the following software installed on your system:

- Python: Version 3.11.7. Download and install from Python's official site.

- Node.js: Version 20.11.0 LTS. Node.js is essential for running JavaScript on the server side. Download from Node.js official site.

- Visual Studio Code (VS Code): A text editor. Download from VS Code's official site.

- Django: Version 4.1. Django is a high-level Python web framework. **NOTE:** Django will download automatically when you run the command ```python -m pip install -r src/requirements.txt```. Follow instrctions below in order **DO NOT INSTALL NOW.**

- Tailwind CSS: Version 3.41. A utility-first CSS framework for creating custom designs.

- PostgreSQL: Version 16.2. Ensure it is installed with pgAdmin for database management. Download from PostgreSQL's official site.

### Setup Instructions
Follow these steps to set up the project environment and run the application:

1. Create a Python Virtual Environment:
```python -m venv venv```

2. Activate the Virtual Environment:
On Windows:
```.\venv\Scripts\activate```

On MacOS:
```source venv/bin/activate```

3. Install Required Python Packages:
```python -m pip install -r src/requirements.txt```

4. Navigate to the Project Directory:
```cd src```

5. Collect Static Files:
```python manage.py collectstatic```
When prompted, type yes to confirm.


6. un the Development Server:
```python manage.py runserver```

### Troubleshooting
- CSS Not Displaying Correctly: If you notice that CSS styles are not being applied properly, try clearing your browser's cache and refreshing the page.

- **Any other issues reach out to me and I'll help you set it up**
