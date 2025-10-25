# Library Management System - Installation & Usage Guide

## 🧠 Concept Overview

The Library Management System is a comprehensive Frappe app that helps librarians manage:
- **Books**: Complete book catalog with ISBN, author, and publisher details
- **Members**: Library member registration and management
- **Memberships**: Time-bound membership tracking with validation
- **Transactions**: Book issue and return system with due date tracking
- **Settings**: Configurable loan periods, maximum book limits, and fine rates

## 🏗️ System Design / Architecture

### DocTypes Structure:
1. **Book** (Master Data)
   - Fields: Title, Author, ISBN, Publisher, Status, Image, Description
   - Statuses: Available, Issued
   - Validation: Unique ISBN, auto-status management

2. **Library Member** (Master Data)
   - Fields: First Name, Last Name, Full Name (auto-generated), Email, Phone, Address
   - Auto-naming: By Email ID
   - Validation: Email format, auto full name generation

3. **Library Membership** (Transactional, Submittable)
   - Fields: Member link, From/To dates, Payment status
   - Naming: LMS-.#### series
   - Business Logic: Prevents overlapping memberships, auto-calculates end date

4. **Library Transaction** (Transactional, Submittable)
   - Fields: Type (Issue/Return), Member, Book, Date, Due Date
   - Naming: LT-.#### series
   - Business Logic: Validates membership, book availability, member limits

5. **Library Settings** (Single DocType)
   - Fields: Loan Period, Max Books per Member, Fine per Day
   - Global configuration for the entire system

### Role-Based Access Control:
- **Librarian**: Full access to all DocTypes, can create, modify, delete, submit
- **Library Member**: Read-only access to view their own records

## ⚙️ Step-by-Step Installation

### Prerequisites
- Frappe Framework v15+ installed
- Active Frappe bench setup
- Git installed on your system

### Installation Steps

1. **Clone/Download from GitHub**
   ```bash
   # From your frappe-bench directory
   cd frappe-bench

   # Get the app from GitHub
   bench get-app https://github.com/yourusername/library_management
   ```

2. **Install on Site**
   ```bash
   # Install the app on your site
   bench --site your-site-name install-app library_management
   ```

3. **Migrate Database**
   ```bash
   # Run migrations to create DocTypes
   bench --site your-site-name migrate
   ```

4. **Build Assets**
   ```bash
   # Build JavaScript and CSS assets
   bench build --app library_management
   ```

5. **Restart Bench**
   ```bash
   # Restart the bench to load new app
   bench restart
   ```

## 💻 Usage Guide

### Initial Setup

1. **Configure Library Settings**
   - Go to Library Settings
   - Set Loan Period (default: 14 days)
   - Set Maximum Books per Member (default: 3)
   - Set Fine per Day (optional)

2. **Create Roles and Users**
   - Assign "Librarian" role to library staff
   - Assign "Library Member" role to library users

### Daily Operations

1. **Add Books**
   ```
   Navigation: Library Management > Books > Book > New
   - Enter book title, author, ISBN
   - Add publisher and description
   - Upload book cover image
   - Save the record
   ```

2. **Register Members**
   ```
   Navigation: Library Management > Members > Library Member > New
   - Enter member details (name, email, phone)
   - Address information
   - Save the record
   ```

3. **Create Memberships**
   ```
   Navigation: Library Management > Members > Library Membership > New
   - Select library member
   - Set membership dates (auto-calculated based on settings)
   - Mark as paid if applicable
   - Submit the membership
   ```

4. **Issue Books**
   ```
   Navigation: Library Management > Transactions > Library Transaction > New
   - Select Type: Issue
   - Choose library member and book
   - Set transaction date
   - Submit the transaction
   ```

5. **Return Books**
   ```
   Navigation: Library Management > Transactions > Library Transaction > New
   - Select Type: Return
   - Choose library member and book
   - Submit the transaction
   ```

## 🚀 Advanced Features & Customizations

### Custom Validations
- **Membership Overlap Prevention**: System prevents creating overlapping memberships
- **Book Availability Check**: Validates book status before issuing
- **Member Limit Enforcement**: Prevents exceeding maximum book limits
- **Due Date Calculation**: Automatically calculates due dates based on settings

### Form Scripts & Automation
- **Auto-completion**: Member names, book titles auto-populate
- **Quick Actions**: Custom buttons for creating related records
- **Status Indicators**: Visual indicators for membership and transaction status

### Extensibility Options
1. **Add Fine Calculation**: Extend transactions to calculate overdue fines
2. **Email Notifications**: Send reminders for due books
3. **Reporting**: Create custom reports for library analytics
4. **Web Portal**: Allow members to view their issued books online
5. **Barcode Integration**: Add barcode scanning for books

### API Endpoints
The app automatically provides REST APIs for all DocTypes:
```
GET /api/resource/Book
POST /api/resource/Book
PUT /api/resource/Book/{name}
DELETE /api/resource/Book/{name}
```

## 🔧 Development & Customization

### File Structure Overview
```
library_management/
├── library_management/
│   ├── library_management/
│   │   └── doctype/
│   │       ├── book/
│   │       ├── library_member/
│   │       ├── library_membership/
│   │       ├── library_transaction/
│   │       └── library_settings/
│   ├── config/
│   ├── public/
│   ├── templates/
│   └── www/
├── setup.py
├── requirements.txt
└── README.md
```

### Customization Points
1. **Add Custom Fields**: Extend DocTypes with additional fields
2. **Custom Scripts**: Add client/server scripts for specific business logic  
3. **Reports**: Create custom reports for analytics
4. **Print Formats**: Design custom print formats for receipts/cards
5. **Web Pages**: Create public-facing pages for member portal

This comprehensive system provides a solid foundation for library management while remaining highly extensible for specific organizational needs.
