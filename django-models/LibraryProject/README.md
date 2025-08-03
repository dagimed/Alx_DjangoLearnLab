# LibraryProject

Library Project Permissions and Groups Setup
This document outlines the implementation of permissions and groups in the Django LibraryProject to control access to various functionalities.
Permissions Setup
Custom permissions are defined in the Book model in models.py to manage access to book-related actions:

can_view: Allows users to view book details.
can_create: Allows users to create new books.
can_edit: Allows users to edit existing books.
can_delete: Allows users to delete books.

These permissions are added to the Book model's Meta class:
class Meta:
    permissions = [
        ("can_view", "Can view books"),
        ("can_create", "Can create books"),
        ("can_edit", "Can edit books"),
        ("can_delete", "Can delete books"),
    ]

Groups Configuration
Three groups are created to manage user roles:

Viewers: Assigned can_view permission to view book details.
Editors: Assigned can_view, can_create, and can_edit permissions to view, create, and edit books.
Admins: Assigned all permissions (can_view, can_create, can_edit, can_delete) for full access.

Steps to Configure Groups

Access the Django admin site (/admin).
Navigate to Groups under the Authentication and Authorization section.
Create the following groups and assign permissions:
Viewers: Add library.can_view.
Editors: Add library.can_view, library.can_create, library.can_edit.
Admins: Add library.can_view, library.can_create, library.can_edit, library.can_delete.


Save the groups.

Assigning Users to Groups

In the Django admin site, go to Users under Authentication and Authorization.
Select or create a test user.
Assign the user to one of the groups (Viewers, Editors, or Admins) via the Groups field.
Save the user.

Permission Enforcement in Views
Permissions are enforced in views.py using the @permission_required decorator:

book_detail: Requires library.can_view.
book_create: Requires library.can_create.
book_edit: Requires library.can_edit.
book_delete: Requires library.can_delete.

Example:
@permission_required('library.can_edit', raise_exception=True)
def book_edit(request, pk):
    # View logic

Testing Permissions
To verify the permissions setup:

Create test users and assign them to different groups (e.g., ViewerUser to Viewers, EditorUser to Editors, AdminUser to Admins).
Log in as each user and attempt to:
View a book’s details (/books/<pk>/).
Create a new book (/books/create/).
Edit an existing book (/books/<pk>/edit/).
Delete a book (/books/<pk>/delete/).


Ensure that:
Viewers can only view books.
Editors can view, create, and edit books but not delete.
Admins can perform all actions.
Unauthorized users receive a permission-denied error.



Notes

Ensure migrations are applied after updating models.py to register the new permissions (python manage.py makemigrations and python manage.py migrate).
The library prefix in permissions (e.g., library.can_view) corresponds to the app name. Adjust if your app name differs.
Templates (book_list.html, book_detail.html, book_form.html, book_confirm_delete.html) and the BookForm in forms.py are assumed to exist. Create them if necessary, following standard Django practices.

This setup enhances the security and functionality of the LibraryProject by restricting access based on user roles.