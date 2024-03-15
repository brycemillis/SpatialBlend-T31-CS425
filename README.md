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

4. Run the command to install libraries:
   ```pip install psycopg2```
   ```pip install pillow```
   <!-- ```pip install numpy``` -->


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
     
### Access to Admin Panel
To access the admin panel, you must first create a superuser account. Follow these steps to create one:

1. Ensure you are in the `src` project directory where the `manage.py` file is located.

2. Open a terminal and activate your virtual environment if it's not already activated.

3. Run the following command to create a superuser account:

```python manage.py createsuperuser```

4. When prompted, enter the following recommended credentials for demonstration purposes:
- Username: `admin`
- Email address: `admin@email.com`
- Password: `adminpass123`
- Password (again): `adminpass123`

**Note:** For security reasons, it is recommended to change these credentials when deploying the application in a production environment.

5. Once the superuser account has been created, you can access the admin panel by visiting the following URL:

```http://localhost:8000/admin```

By following these steps, you should now have access to the Django admin panel, where you can manage the application's data.

### Troubleshooting

If you encounter any issues, try the following:

- **CSS Not Displaying Correctly:** If CSS styles are not being applied properly, try clearing your browser's cache and refreshing the page.

- For any other issues, feel free to reach out for assistance.

### Functional Requirements & Other Needed Implemenation

Below are the functional requriements of this project that need to be implemented.


- ~ FR1. Image Upload: Application shall allow users to upload a minimum of two images for processing. ~
- FR2. Image Download: Application shall provide capability to download the processed/merged image.
- FR3. Spatial Frequency Adjustment: Application shall implement basic tools to alter spatial frequencies of uploaded images.
- FR4. Composite Image Creation: Application shall combine two images to produce a composite image.
- FR5. User Interface Design: Application shall present a simple layout with clear instruction for uploading, manipulating, and downloading images.
- FR6. Admin Page: Application shall contain an admin page to manage users and uploaded content.
- FR7. Enhanced Spatial Frequency Tools: Application shall offer enhanced tools for more control over spatial frequency alterations (possibly adjusting color and contrast of images).
- FR8.User Login and Registration: Application shall provide User Login and Registration.
- FR9. Database Management: Application shall contain a database to store user info and images.
- FR10. Custom Image Saving: Application shall allow the user to save images in a user-specified format and location in the application.
- FR11. Local Storage Download: Application shall provide the functionality to download images after processing to the user's local storage.
- FR12. Real-Time Visualization: Application shall implement a real-time feature for visualization changes.
- FR13. Composite Image Weightage Adjustment: Application shall allow users to adjust the weightage of each image in the composite.
- FR14. Design and Usability Update: Application shall update its design to provide more simple and modern visualization. It shall also provide more intuitive controls and navigation for users.
- FR15. Advanced Image Merging: Application shall support advanced image merging (e.g., selfies will be aligned based on facial structure).
- FR16. 3D Image Merging Tools: Application shall introduce tools for 3D image processing.
- FR17. Human Vision Tools: Application shall include tools to examine human vision concepts like depth perception.
- FR18. Visual Illusion Exploration: Application shall examine intricate visual illusions, such as the hollow face illusion.