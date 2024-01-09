# Car Hub

## Description
This Django project is a Car Dealership Management System. It allows users to add and manage cars, brands, and comments. Users can also purchase cars and leave comments on specific cars.

## Features
- Car Management: Add, edit, and delete cars with details like brand, description, image, price, and quantity.
- Brand Management: Add and manage car brands.
- User Authentication: Users can sign up, log in, and log out. Some functionalities are restricted to authenticated users.
- Purchase System: Users can purchase cars, and the quantity is updated accordingly.
- Comment System: Users can leave comments on specific cars.

## Getting Started
1. Clone the repository: `git clone https://github.com/Nirob-Barman/Software-Development-Project.git`
2. Navigate to the project directory: `cd Car_Hub_Market`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Visit `http://localhost:8000/` in your web browser.

## Project Structure
- `cars`: Django app for managing cars and comments.
- `brands`: Django app for managing car brands.
- `templates`: HTML templates for rendering views.
- `static`: Static files (CSS, images, etc.).

## Usage
- Visit the homepage to see the list of cars: `http://localhost:8000/`
- Navigate to the 'Add Car' section to add new cars.
- Navigate to the 'Brands' section to add and view car brands.
- Users can purchase cars and leave comments on the car detail page.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
