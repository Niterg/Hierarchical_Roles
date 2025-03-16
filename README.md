## RBAC (Roles Based Access Control)

- ``Step 1:`` To initialize Django application
    ```ps
    python -m venv venv 
    ```
    - Before activating script check the Execution Policy
    ```ps1
    Get-ExecutionPolicy
    Restricted # If this is shown execute the command below in administrator mode
    
    # For the current process only
    Set-ExecutionPolicy Unrestricted -Scope Process

    # For permanently allowing scripts
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

    # Now it should show unrestricted
    Get-ExecutionPolicy
    Unrestricted

    # To list the users that has access to ExecutionPolicy
    Get-ExecutionPolicy -List
    ```
    - Activate the script
    ```ps1
    venv/Scripts/activate
    python -m django --version 
    # If django does not exits

    pip install django 
    pip install djangorestframework

    # ELSE
    pip install -r requirements.txt

    # To generate requirements.txt
    pip freeze > requirements.txt
    ```
- ``Step 2:`` To create new app 
    ```ps
    # Create a project
    django-admin startapp RBAC
    cd .\RBAC

    # Creat new app 'authentication' for the RBAC implementation 
    python manage.py startapp authentication 
    ```

- ``Step 3:`` To clarify the Permissions 
    ```ps
    # Perform following to run shell command
    python manage.py shell
    # Paste the manage.py.shell

    # ELSE
    python RBAC/populate_roles.py
    ```
    OR
    ```ps
    # Use migration to make the roles and permissions
    python manage.py makemigrations authentication
    python manage.py migrate
    ```
- ``Step 4:`` 
    ## For JWT Framework Implementation (API)
    ```ps
    pip install djangorestframework-simplejwt
    ```
    - Update ``settings.py ``
    ```py
    INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ]

    # Add JWT authentication to the Django Rest Framework settings
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    }
    ```
    - To create JWT Token for 1 hour, in ``settings.py ``
    ```py
    from datetime import timedelta

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
    }
    ```
    - Token view in ``urls.py``
    ```py
    from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

    urlpatterns = [
        ...
        # JWT Token view (Obtain access and refresh tokens)
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
    ```

