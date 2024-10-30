# Creating a Custom Addon in Odoo to Add a Dropdown Field

This guide will help you create a custom addon in Odoo that adds an extra dropdown field in the equipment view of the maintenance module.

## Step-by-Step Guide

### 1. Set Up Your Development Environment
- Ensure you have Odoo installed and running.
- Activate developer mode in Odoo.

### 2. Create a New Module
- Navigate to your Odoo addons directory.
- Create a new directory for your custom module, e.g., `equipment_donor_info`.

### 3. Define the Module Structure
- Inside your module directory, create the following structure:
```
equipment_donor_info/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── equipment.py
├── views/
│   └── equipment_view.xml
└── static/
    └── description/
        └── icon.png
```
