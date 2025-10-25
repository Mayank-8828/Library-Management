# Library Management System

A comprehensive Library Management System built on Frappe Framework.

## Features

- **Book Management**: Add, edit, and manage books with ISBN, author, and publisher details
- **Member Management**: Manage library members with membership tracking
- **Transaction System**: Issue and return books with proper validation
- **Membership System**: Track active memberships with expiry dates
- **Settings Configuration**: Configure loan periods and maximum book limits
- **Role-based Permissions**: Separate roles for Librarians and Library Members

## Installation

1. Get the app from GitHub:
```bash
bench get-app https://github.com/yourusername/library_management
```

2. Install on your site:
```bash
bench --site your-site-name install-app library_management
```

## Usage

1. **Configure Library Settings**: Set loan period and maximum books per member
2. **Add Books**: Create book records with details like title, author, ISBN
3. **Register Members**: Add library members
4. **Create Memberships**: Set up memberships for library members
5. **Manage Transactions**: Issue and return books

## DocTypes

- **Book**: Manages book information
- **Library Member**: Member details and information  
- **Library Membership**: Membership records with validity
- **Library Transaction**: Book issue/return transactions
- **Library Settings**: System configuration

## License

MIT