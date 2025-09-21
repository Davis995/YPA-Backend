# Restaurant Admin Backend

A Django REST API backend for managing a restaurant's admin operations including menu items, bookings, orders, and customer messages.

## Features

- **Dashboard Statistics**: Real-time overview of restaurant operations
- **Menu Management**: CRUD operations for categories and menu items
- **Booking Management**: Handle table reservations and status updates
- **Order Management**: Process food orders with status tracking
- **Contact Management**: Handle customer inquiries and messages
- **Admin User Management**: Manage admin users and roles
- **Django Admin Interface**: Built-in admin panel for data management

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git
- PostgreSQL 12+ (for production) or SQLite (for development)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/restaurant-admin-backend.git
   cd restaurant-admin-backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Configuration:**
   ```bash
   # Copy the environment template
   cp env_template.txt .env
   
   # Edit .env file with your settings
   # Configure your DATABASE_URL for PostgreSQL
   # At minimum, change the SECRET_KEY for production
   ```

6. **PostgreSQL Setup (Recommended for Production):**
   ```bash
   # Install PostgreSQL (if not already installed)
   # Ubuntu/Debian:
   sudo apt-get install postgresql postgresql-contrib
   
   # macOS with Homebrew:
   brew install postgresql
   
   # Windows: Download from https://www.postgresql.org/download/windows/
   
   # Create database and user
   sudo -u postgres psql
   CREATE DATABASE restaurant_db;
   CREATE USER restaurant_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE restaurant_db TO restaurant_user;
   \q
   
   # Update your .env file with the correct DATABASE_URL:
   # DATABASE_URL=postgresql://restaurant_user:your_password@localhost:5432/restaurant_db
   ```

7. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
   # Or use the setup script for PostgreSQL:
   python setup_postgres.py
   ```

8. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

9. **Create sample data (optional):**
   ```bash
   # Create tables, menu items, and sample data
   python table.py
   
   # Or use the batch script (Windows):
   create_tables.bat
   
   # Or use the shell script (Unix/Linux/macOS):
   chmod +x create_tables.sh
   ./create_tables.sh
   ```

10. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://localhost:8000/api/`
The Django admin interface will be available at `http://localhost:8000/admin/`

### Sample Data

If you ran the `table.py` script, you'll have:

**Restaurant Tables:**
- 12 tables (T1-T12) with different capacities (2-10 people)

**Menu Categories:**
- Appetizers, Main Course, Seafood, Vegetarian, Desserts, Beverages, Grilled, Pasta

**Menu Items:**
- 22 sample menu items across all categories with realistic prices

**Admin Users:**
- `admin` (password: password123) - Full admin access
- `manager` (password: password123) - Manager access
- `waiter1`, `waiter2` (password: password123) - Waiter access
- `kitchen` (password: password123) - Kitchen staff access

**Sample Data:**
- Sample orders and table-based orders
- Sample bookings and contact messages
- Sample waiter requests

## API Endpoints

### Authentication
All endpoints require authentication. Use Django's session authentication or basic authentication.

### Dashboard
- `GET /api/dashboard/` - Get dashboard statistics

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create a new category
- `GET /api/categories/{id}/` - Get category details
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

### Menu Items
- `GET /api/menu/` - List all menu items
- `POST /api/menu/` - Create a new menu item
- `GET /api/menu/{id}/` - Get menu item details
- `PUT /api/menu/{id}/` - Update menu item
- `DELETE /api/menu/{id}/` - Delete menu item

### Contact Messages
- `GET /api/contacts/` - List all contact messages
- `GET /api/contacts/{id}/` - Get contact message details
- `PUT /api/contacts/{id}/` - Update contact message
- `DELETE /api/contacts/{id}/` - Delete contact message
- `PATCH /api/contacts/{id}/status/` - Update message status

### Bookings
- `GET /api/bookings/` - List all bookings
- `GET /api/bookings/{id}/` - Get booking details
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Delete booking
- `PATCH /api/bookings/{id}/status/` - Update booking status

### Orders
- `GET /api/orders/` - List all orders
- `POST /api/orders/` - Create a new order
- `GET /api/orders/{id}/` - Get order details
- `PUT /api/orders/{id}/` - Update order
- `DELETE /api/orders/{id}/` - Delete order
- `PATCH /api/orders/{id}/status/` - Update order status

### Admin Users
- `GET /api/admin-users/` - List all admin users
- `POST /api/admin-users/` - Create a new admin user
- `GET /api/admin-users/{id}/` - Get admin user details
- `PUT /api/admin-users/{id}/` - Update admin user
- `DELETE /api/admin-users/{id}/` - Delete admin user

## Data Models

### Category
```json
{
  "id": 1,
  "name": "Main Course",
  "description": "Delicious main dishes",
  "image": "/media/categories/main-course.jpg",
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### MenuItem
```json
{
  "id": 1,
  "name": "Grilled Chicken",
  "description": "Tender grilled chicken with herbs",
  "price": "15.99",
  "image": "/media/menu/grilled-chicken.jpg",
  "category": "Meals",
  "category_display": "Meals",
  "is_available": true,
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### Booking
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "date": "2024-01-15",
  "time": "19:00:00",
  "guests": 4,
  "status": "confirmed",
  "status_display": "Confirmed",
  "notes": "Window seat preferred",
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### Order
```json
{
  "id": 1,
  "customer_name": "Jane Smith",
  "customer_email": "jane@example.com",
  "customer_phone": "+1234567890",
  "total": "45.97",
  "status": "preparing",
  "status_display": "Preparing",
  "notes": "Extra spicy please",
  "items": [
    {
      "id": 1,
      "menu_item": 1,
      "name": "Grilled Chicken",
      "price": "15.99",
      "quantity": 2
    }
  ],
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### ContactMessage
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "phone": "+1234567890",
  "message": "Do you have vegetarian options?",
  "status": "new",
  "status_display": "New",
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### AdminUser
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@restaurant.com",
    "first_name": "Admin",
    "last_name": "User"
  },
  "role": "admin",
  "role_display": "Admin",
  "phone": "+1234567890",
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

## Status Values

### Booking Status
- `new` - New booking
- `confirmed` - Confirmed booking
- `cancelled` - Cancelled booking

### Order Status
- `pending` - Order pending
- `confirmed` - Order confirmed
- `preparing` - Order being prepared
- `ready` - Order ready for pickup/delivery
- `delivered` - Order delivered
- `cancelled` - Order cancelled

### Contact Message Status
- `new` - New message
- `handled` - Message handled

### Admin User Roles
- `admin` - Full admin access
- `manager` - Manager access

## File Uploads

The API supports file uploads for:
- Category images: `/media/categories/`
- Menu item images: `/media/menu/`

Use `multipart/form-data` for requests with file uploads.

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Internal Server Error

Error responses include a message describing the issue:
```json
{
  "error": "Invalid status value"
}
```

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Shell Access
```bash
python manage.py shell
```

## Production Deployment

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-production-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://username:password@localhost:5432/restaurant_db
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Deployment Steps

1. **Set environment variables:**
   - Generate a new SECRET_KEY for production
   - Set `DEBUG=False`
   - Configure your domain in `ALLOWED_HOSTS`
   - Set up a production database (PostgreSQL recommended)

2. **Database Setup:**
   ```bash
   # For PostgreSQL
   pip install psycopg2-binary
   python manage.py migrate
   ```

3. **Static Files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Production Server:**
   ```bash
   # Using Gunicorn
   gunicorn restaurant_admin.wsgi:application --bind 0.0.0.0:8000
   ```

### Docker Deployment (Optional)

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "restaurant_admin.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Heroku Deployment

1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: gunicorn restaurant_admin.wsgi:application --port $PORT
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   git push heroku main
   heroku run python manage.py migrate
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.





