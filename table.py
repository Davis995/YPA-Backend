#!/usr/bin/env python
"""
Table Creation Script for Restaurant Admin

This script creates table instances and sample data for the restaurant admin application.
Run this script after setting up your PostgreSQL database and running migrations.

Usage:
    python table.py
"""

import os
import sys
import django
from pathlib import Path
from decimal import Decimal
from datetime import datetime, date, time, timedelta
import random

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_admin.settings')
django.setup()

from django.contrib.auth.models import User
from admin_app.models import (
    Category, MenuItem, ContactMessage, Booking, Order, OrderItem, 
    AdminUser, WaiterRequest, Table, OrderMenu, orderMenuItem
)

def create_tables():
    """Create restaurant tables"""
    print("Creating restaurant tables...")
    
    tables_data = [
        {"number": 1, "capacity": 2},
        {"number": 2, "capacity": 2},
        {"number": 3, "capacity": 4},
        {"number": 4, "capacity": 4},
        {"number": 5, "capacity": 6},
        {"number": 6, "capacity": 6},
        {"number": 7, "capacity": 8},
        {"number": 8, "capacity": 2},
        {"number": 9, "capacity": 4},
        {"number": 10, "capacity": 6},
        {"number": 11, "capacity": 8},
        {"number": 12, "capacity": 10},
    ]
    
    created_tables = []
    for table_data in tables_data:
        table, created = Table.objects.get_or_create(
            number=table_data["number"],
            defaults={"number": table_data["number"]}
        )
        if created:
            created_tables.append(table)
            print(f"  ✓ Created table {table.number}")
        else:
            print(f"  - Table {table.number} already exists")
    
    return created_tables

def create_categories():
    """Create menu categories"""
    print("\nCreating menu categories...")
    
    categories_data = [
        {
            "name": "Appetizers",
            "description": "Start your meal with our delicious appetizers",
        },
        {
            "name": "Main Course",
            "description": "Hearty main dishes to satisfy your hunger",
        },
        {
            "name": "Seafood",
            "description": "Fresh seafood dishes from the ocean",
        },
        {
            "name": "Vegetarian",
            "description": "Healthy and delicious vegetarian options",
        },
        {
            "name": "Desserts",
            "description": "Sweet treats to end your meal perfectly",
        },
        {
            "name": "Beverages",
            "description": "Refreshing drinks and beverages",
        },
        {
            "name": "Grilled",
            "description": "Perfectly grilled meats and vegetables",
        },
        {
            "name": "Pasta",
            "description": "Italian-inspired pasta dishes",
        }
    ]
    
    created_categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults=cat_data
        )
        if created:
            created_categories.append(category)
            print(f"  ✓ Created category: {category.name}")
        else:
            print(f"  - Category '{category.name}' already exists")
    
    return created_categories

def create_menu_items(categories):
    """Create menu items"""
    print("\nCreating menu items...")
    
    menu_items_data = [
        # Appetizers
        {
            "name": "Buffalo Wings",
            "description": "Spicy chicken wings served with ranch dip",
            "price": Decimal("25000"),
            "category": "Appetizers"
        },
        {
            "name": "Mozzarella Sticks",
            "description": "Crispy mozzarella sticks with marinara sauce",
            "price": Decimal("18000"),
            "category": "Appetizers"
        },
        {
            "name": "Caesar Salad",
            "description": "Fresh romaine lettuce with caesar dressing and croutons",
            "price": Decimal("15000"),
            "category": "Appetizers"
        },
        
        # Main Course
        {
            "name": "Grilled Chicken Breast",
            "description": "Tender grilled chicken breast with herbs and spices",
            "price": Decimal("35000"),
            "category": "Main Course"
        },
        {
            "name": "Beef Steak",
            "description": "Juicy beef steak cooked to perfection",
            "price": Decimal("45000"),
            "category": "Main Course"
        },
        {
            "name": "BBQ Ribs",
            "description": "Slow-cooked BBQ ribs with our signature sauce",
            "price": Decimal("40000"),
            "category": "Main Course"
        },
        
        # Seafood
        {
            "name": "Grilled Salmon",
            "description": "Fresh Atlantic salmon grilled with lemon butter",
            "price": Decimal("55000"),
            "category": "Seafood"
        },
        {
            "name": "Fish and Chips",
            "description": "Beer-battered fish with crispy fries",
            "price": Decimal("28000"),
            "category": "Seafood"
        },
        {
            "name": "Shrimp Scampi",
            "description": "Large shrimp in garlic butter sauce over pasta",
            "price": Decimal("42000"),
            "category": "Seafood"
        },
        
        # Vegetarian
        {
            "name": "Veggie Burger",
            "description": "Plant-based burger with fresh vegetables",
            "price": Decimal("20000"),
            "category": "Vegetarian"
        },
        {
            "name": "Quinoa Bowl",
            "description": "Healthy quinoa bowl with roasted vegetables",
            "price": Decimal("22000"),
            "category": "Vegetarian"
        },
        {
            "name": "Mushroom Risotto",
            "description": "Creamy risotto with wild mushrooms",
            "price": Decimal("30000"),
            "category": "Vegetarian"
        },
        
        # Desserts
        {
            "name": "Chocolate Cake",
            "description": "Rich chocolate cake with chocolate ganache",
            "price": Decimal("12000"),
            "category": "Desserts"
        },
        {
            "name": "Tiramisu",
            "description": "Classic Italian dessert with coffee and mascarpone",
            "price": Decimal("15000"),
            "category": "Desserts"
        },
        {
            "name": "Ice Cream Sundae",
            "description": "Vanilla ice cream with chocolate sauce and nuts",
            "price": Decimal("8000"),
            "category": "Desserts"
        },
        
        # Beverages
        {
            "name": "Fresh Orange Juice",
            "description": "Freshly squeezed orange juice",
            "price": Decimal("5000"),
            "category": "Beverages"
        },
        {
            "name": "Coffee",
            "description": "Freshly brewed coffee",
            "price": Decimal("3000"),
            "category": "Beverages"
        },
        {
            "name": "Soft Drinks",
            "description": "Assorted soft drinks (Coke, Pepsi, Sprite)",
            "price": Decimal("4000"),
            "category": "Beverages"
        },
        
        # Grilled
        {
            "name": "Grilled Vegetables",
            "description": "Seasonal vegetables grilled to perfection",
            "price": Decimal("18000"),
            "category": "Grilled"
        },
        {
            "name": "Grilled Pork Chops",
            "description": "Thick-cut pork chops with apple glaze",
            "price": Decimal("38000"),
            "category": "Grilled"
        },
        
        # Pasta
        {
            "name": "Spaghetti Carbonara",
            "description": "Classic Italian pasta with eggs, cheese, and bacon",
            "price": Decimal("25000"),
            "category": "Pasta"
        },
        {
            "name": "Fettuccine Alfredo",
            "description": "Creamy fettuccine with parmesan cheese sauce",
            "price": Decimal("23000"),
            "category": "Pasta"
        }
    ]
    
    created_items = []
    category_dict = {cat.name: cat for cat in categories}
    
    for item_data in menu_items_data:
        category_name = item_data.pop("category")
        category = category_dict.get(category_name)
        
        if category:
            item, created = MenuItem.objects.get_or_create(
                name=item_data["name"],
                defaults={**item_data, "category": category}
            )
            if created:
                created_items.append(item)
                print(f"  ✓ Created menu item: {item.name}")
            else:
                print(f"  - Menu item '{item.name}' already exists")
    
    return created_items

def create_admin_users():
    """Create admin users"""
    print("\nCreating admin users...")
    
    users_data = [
        {
            "username": "admin",
            "email": "admin@restaurant.com",
            "first_name": "Restaurant",
            "last_name": "Admin",
            "role": "admin",
            "phone": "256701234567"
        },
        {
            "username": "manager",
            "email": "manager@restaurant.com",
            "first_name": "James",
            "last_name": "Mukasa",
            "role": "manager",
            "phone": "256702345678"
        },
        {
            "username": "waiter1",
            "email": "waiter1@restaurant.com",
            "first_name": "Grace",
            "last_name": "Nakato",
            "role": "waiter",
            "phone": "256703456789"
        },
        {
            "username": "waiter2",
            "email": "waiter2@restaurant.com",
            "first_name": "Peter",
            "last_name": "Ochieng",
            "role": "waiter",
            "phone": "256704567890"
        },
        {
            "username": "kitchen",
            "email": "kitchen@restaurant.com",
            "first_name": "Chef",
            "last_name": "Musoke",
            "role": "kitchen_staff",
            "phone": "256705678901"
        }
    ]
    
    created_users = []
    for user_data in users_data:
        role = user_data.pop("role")
        phone = user_data.pop("phone")
        
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults=user_data
        )
        
        if created:
            user.set_password("password123")  # Default password
            user.save()
            
            admin_user, admin_created = AdminUser.objects.get_or_create(
                user=user,
                defaults={"role": role, "phone": phone}
            )
            
            if admin_created:
                created_users.append(admin_user)
                print(f"  ✓ Created user: {user.username} ({role})")
            else:
                print(f"  - Admin user for '{user.username}' already exists")
        else:
            print(f"  - User '{user.username}' already exists")
    
    return created_users

def create_sample_orders(menu_items, tables):
    """Create sample orders"""
    print("\nCreating sample orders...")
    
    # Create some traditional orders
    orders_data = [
        {
            "customer_name": "Aisha Nalubega",
            "customer_email": "aisha@email.com",
            "customer_phone": "256706123456",
            "total": Decimal("85000"),
            "status": "confirmed",
            "payment_method": "cash",
            "notes": "Table 3, extra spicy"
        },
        {
            "customer_name": "David Kato",
            "customer_email": "david@email.com",
            "customer_phone": "256707234567",
            "total": Decimal("62000"),
            "status": "preparing",
            "payment_method": "airtel_money",
            "notes": "Allergic to nuts"
        },
        {
            "customer_name": "Catherine Namukasa",
            "customer_email": "catherine@email.com",
            "customer_phone": "256708345678",
            "total": Decimal("54000"),
            "status": "delivered",
            "payment_method": "mtn_momo",
            "notes": ""
        }
    ]
    
    created_orders = []
    for order_data in orders_data:
        order, created = Order.objects.get_or_create(
            customer_email=order_data["customer_email"],
            created_at__date=date.today(),
            defaults=order_data
        )
        if created:
            created_orders.append(order)
            print(f"  ✓ Created order for: {order.customer_name}")
        else:
            print(f"  - Order for '{order_data['customer_email']}' already exists")
    
    # Create table-based orders using OrderMenu
    print("\nCreating table-based orders...")
    for i, table in enumerate(tables[:3]):  # Create orders for first 3 tables
        order_menu, created = OrderMenu.objects.get_or_create(
            table=table,
            created_at__date=date.today(),
             defaults={
                 "status": random.choice(["pending", "confirmed", "preparing"]),
                 "total_price": random.randint(25000, 75000),
                 "payment_method": random.choice(["cash", "airtel_money", "mtn_momo"])
             }
        )
        
        if created:
            print(f"  ✓ Created table order for {table.number}")
            
            # Add some menu items to this order
            selected_items = random.sample(menu_items, random.randint(2, 4))
            for item in selected_items:
                quantity = random.randint(1, 3)
                order_item, item_created = orderMenuItem.objects.get_or_create(
                    ordermenu=order_menu,
                    item=item,
                    defaults={
                        "quantity": quantity,
                        "price": int(item.price),
                        "special_request": random.choice(["", "Extra spicy", "No onions", "Well done"]) if random.random() > 0.7 else ""
                    }
                )
                if item_created:
                    print(f"    - Added {item.name} x{quantity}")
    
    return created_orders

def create_sample_bookings():
    """Create sample bookings"""
    print("\nCreating sample bookings...")
    
    bookings_data = [
        {
            "name": "John Muwanga",
            "email": "john@email.com",
            "phone": "256709456789",
            "date": date.today() + timedelta(days=1),
            "time": time(19, 0),
            "guests": 4,
            "status": "confirmed",
            "notes": "Anniversary dinner"
        },
        {
            "name": "Jane Nakamya",
            "email": "jane@email.com",
            "phone": "256710567890",
            "date": date.today() + timedelta(days=2),
            "time": time(18, 30),
            "guests": 2,
            "status": "new",
            "notes": "Window seat preferred"
        },
        {
            "name": "Michael Kiggundu",
            "email": "michael@email.com",
            "phone": "256711678901",
            "date": date.today() + timedelta(days=3),
            "time": time(20, 0),
            "guests": 6,
            "status": "confirmed",
            "notes": "Business dinner"
        }
    ]
    
    created_bookings = []
    for booking_data in bookings_data:
        booking, created = Booking.objects.get_or_create(
            email=booking_data["email"],
            date=booking_data["date"],
            time=booking_data["time"],
            defaults=booking_data
        )
        if created:
            created_bookings.append(booking)
            print(f"  ✓ Created booking for: {booking.name}")
        else:
            print(f"  - Booking for '{booking_data['email']}' already exists")
    
    return created_bookings

def create_sample_contacts():
    """Create sample contact messages"""
    print("\nCreating sample contact messages...")
    
    contacts_data = [
        {
            "name": "David Ssemwogerere",
            "email": "david@email.com",
            "phone": "256712789012",
            "message": "Do you have vegetarian options?",
            "status": "handled"
        },
        {
            "name": "Lisa Namukasa",
            "email": "lisa@email.com",
            "phone": "256713890123",
            "message": "What are your opening hours on weekends?",
            "status": "new"
        },
        {
            "name": "Thomas Kiggundu",
            "email": "thomas@email.com",
            "phone": "256714901234",
            "message": "Can I make a reservation for a large group?",
            "status": "handled"
        }
    ]
    
    created_contacts = []
    for contact_data in contacts_data:
        contact, created = ContactMessage.objects.get_or_create(
            email=contact_data["email"],
            created_at__date=date.today(),
            defaults=contact_data
        )
        if created:
            created_contacts.append(contact)
            print(f"  ✓ Created contact message from: {contact.name}")
        else:
            print(f"  - Contact message from '{contact_data['email']}' already exists")
    
    return created_contacts

def create_sample_waiter_requests(tables):
    """Create sample waiter requests"""
    print("\nCreating sample waiter requests...")
    
    requests_data = [
        {
            "table_number": "3",
            "message": "Need more napkins",
            "status": "completed"
        },
        {
            "table_number": "5",
            "message": "Ready to order",
            "status": "acknowledged"
        },
        {
            "table_number": "7",
            "message": "Check please",
            "status": "pending"
        }
    ]
    
    created_requests = []
    for request_data in requests_data:
        request, created = WaiterRequest.objects.get_or_create(
            table_number=request_data["table_number"],
            created_at__date=date.today(),
            defaults=request_data
        )
        if created:
            created_requests.append(request)
            print(f"  ✓ Created waiter request for: {request.table_number}")
        else:
            print(f"  - Waiter request for '{request_data['table_number']}' already exists")
    
    return created_requests

def main():
    """Main function to create all table instances"""
    print("=" * 60)
    print("RESTAURANT ADMIN - TABLE INSTANCE CREATION")
    print("=" * 60)
    
    try:
        # Create all instances
        tables = create_tables()
        categories = create_categories()
        menu_items = create_menu_items(categories)
        admin_users = create_admin_users()
        orders = create_sample_orders(menu_items, tables)
        bookings = create_sample_bookings()
        contacts = create_sample_contacts()
        waiter_requests = create_sample_waiter_requests(tables)
        
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"✓ Tables created: {len(tables)}")
        print(f"✓ Categories created: {len(categories)}")
        print(f"✓ Menu items created: {len(menu_items)}")
        print(f"✓ Admin users created: {len(admin_users)}")
        print(f"✓ Orders created: {len(orders)}")
        print(f"✓ Bookings created: {len(bookings)}")
        print(f"✓ Contact messages created: {len(contacts)}")
        print(f"✓ Waiter requests created: {len(waiter_requests)}")
        
        print("\n🎉 All table instances created successfully!")
        print("\nNext steps:")
        print("1. Run the Django server: python manage.py runserver")
        print("2. Visit http://localhost:8000/admin/ to access the admin panel")
        print("3. Use the created admin users to log in")
        print("4. Visit http://localhost:8000/api/ to access the API endpoints")
        
        print("\nDefault admin credentials:")
        print("Username: admin")
        print("Password: password123")
        
    except Exception as e:
        print(f"\n❌ Error creating table instances: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure PostgreSQL is running")
        print("2. Check your DATABASE_URL in .env file")
        print("3. Run migrations: python manage.py migrate")
        sys.exit(1)

if __name__ == "__main__":
    main()
