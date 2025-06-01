from pydantic import BaseModel, EmailStr, ValidationError, field_validator
import re
from typing import Optional

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "member" 

    @field_validator('password')
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r"[A-Z]", password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r"[a-z]", password):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r"[0-9]", password):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError('Password must contain at least one special character')
        return password


class UpdateUser(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None

# Example of how you might handle the role in the registration endpoint
def register_user(data: User):
    # Hash the password
    hashed_password = hash_password(data.password)
    
    # Create the user in the database
    user = create_user_in_db(
        full_name=data.full_name,
        username=data.username,
        email=data.email,
        password=hashed_password,
        role=data.role  # Save the role to the database
    )
    return user

# Example of how you might handle the role in the login endpoint
def login_user(data: LoginRequest):
    user = find_user_by_email(data.email)
    if not user or not verify_password(data.password, user.password):
        raise AuthenticationError("Invalid credentials")
    
    # Check the role and redirect accordingly
    if user.role == "admin":
        redirect_url = "/index"
    else:
        redirect_url = "/dashboard"
    
    return {"token": generate_jwt_token(user), "redirect_url": redirect_url}
