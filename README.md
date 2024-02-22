# SpatialBlend-T31-CS425

## Senior Capstone Project

### Application Software (DO NOT INSTALL, see ‘Setup Instructions’ below)

Below is a list of the necessary software components used in the application. DO NOT download here; refer to the ‘Setup Instructions’ section for installation guidance:

- Python: Version 3.11.7
- Node.js: Version 20.11.0 LTS
- Visual Studio Code (VS Code)
- Django: Version 4.1
- Tailwind CSS: Version v3.4.1
- PostgreSQL: Version 16.2  

### Setup Instructions

To set up the project environment and run the application, follow these steps:  

**Prerequisites**

If you do not already have the following installed, please install them from their origin website:

1. Visual Studio Code (VS Code)
2. Python 3.11.7
3. Node.js 20.11.0 LTS
4. PostgreSQL 16.2  (Skip stack builder)  

Clone the repository from Github and open it in VS Code. Open a terminal and navigate to the main project directory.

**In the main project directory, run the following commands:**

1. Create a Python Virtual Environment:
   ```python -m venv venv```

2. Activate the Virtual Environment:

   On Windows: 
   ```.\venv\Scripts\activate```

   On MacOS:
   ```source venv/bin/activate```

3. Install Required Python Packages:
   ```python -m pip install -r src/requirements.txt```

4. Run the command:
   ```pip install psycopg2```

5.  Install Tailwind CSS:
```npm install tailwindcss@v3.4.1```  

**Next, navigate to the 'src' directory:**

1. ```cd src```

2. Run ```npm run dev``` in the terminal then exit it using Ctrl+C.

3. Collect Static Files:
   ```python manage.py collectstatic```
   When prompted, type 'yes' to confirm.

4. Migrate files:
   ```python manage.py migrate```

5. Run the Development Server:
   ```python manage.py runserver```  

### Troubleshooting

If you encounter any issues, try the following:

- **CSS Not Displaying Correctly:** If CSS styles are not being applied properly, try clearing your browser's cache and refreshing the page.

- For any other issues, feel free to reach out for assistance.