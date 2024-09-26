# RestoTrack - Restaurant Management System

RestoTrack is a comprehensive restaurant management system designed to streamline operations for cashiers, managers, and administrators. The system incorporates role-based access control, allowing users to perform specific tasks based on their roles, such as taking orders, managing inventory, and predicting stock requirements for future months.

## Key Features

### Role-Based Access
- **Cashier**:
  - Take customer orders and process payments.
  - Limited access to functionalities related to orders.
  
- **Manager**:
  - Manage menu items and categorize them.
  - Add or update ingredients for menu items.
  - Monitor and manage inventory based on orders.
  - If an ingredient is not in the inventory, it can be added.
  
- **Admin**:
  - Full access to the system, including user management and overseeing both cashiers and managers.
  - Admin can access all system functionalities like viewing reports, managing users, etc.

### Inventory Management
- Automatically updates the inventory when an order is placed.
- Ingredients required for each menu item are specified by the manager, and they are deducted from the stock when an order is placed.
  - For example: If the stock of chicken patties is 20 and an order is placed for 2 chicken burgers, the inventory will reduce by 2, leaving 18 chicken patties.
  
### Predictive Inventory Restocking
- RestoTrack predicts month-wise inventory requirements based on order history, helping managers maintain an adequate supply of ingredients and ensuring efficient stock replenishment.

## Workflow Overview

1. **Cashier**: Takes customer orders, such as a "Chicken Burger."
2. The "Chicken Burger" consists of ingredients such as chicken patty, cheese, and bun.
3. Once the order is placed, the system deducts the quantity of ingredients used (e.g., 2 chicken patties for 2 burgers).
4. The inventory automatically updates, reflecting the adjusted quantity (e.g., 20 chicken patties become 18).
5. The system forecasts inventory needs for the upcoming month, assisting the manager in planning restocks.

## Installation

To set up the RestoTrack system on your local machine, follow the steps below:

## Installation and Setup


1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/restotrack.git
   cd restotrack
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt


2.**Set up the database**:

```bash
   python manage.py migrate

3.**Create a superuser (admin)**:

```bash
  python manage.py createsuperuser

4. **Run the development server**:

```bash
   python manage.py runserver

5. **Open your web browser and navigate to http://127.0.0.1:8000 to access the system**.

## Usage

- **Login**: Use the credentials of the cashier, manager, or admin to log in.
- **Cashier**: Navigate to the "Orders" section to process customer orders and payments.
- **Manager**: Go to the "Inventory" section to manage ingredients, menu items, and categories. The manager can monitor stock levels and add new inventory as needed.
- **Admin**: Use the "Admin Panel" to manage all aspects of the system, including user roles, menu items, inventory, and reports.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (can be configured for other databases)
- **Authentication**: Django's built-in authentication system for role-based access

## Future Enhancements

- **Sales Reporting**: Add detailed sales analysis reports.
- **Payment Integration**: Integrate with online payment gateways.
- **Mobile Application**: Create a mobile app for better accessibility and usage.
- **Advanced Forecasting**: Improve predictive algorithms for inventory management.

## Contributing

If you'd like to contribute to the project:
- Fork the repository.
- Create a new feature branch.
- Commit your changes.
- Submit a pull request.

Feel free to open issues or feature requests to enhance the project further!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
