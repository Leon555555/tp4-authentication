# TP4 - Authentication System

## Project Overview
This project implements an authentication system using FastAPI, JWT (JSON Web Tokens), and Redis for session management. Users can register, log in, validate tokens, and log out securely.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.11+
- Docker
- Redis

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/tp4-authentication.git
   cd tp4-authentication
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start Redis in Docker:
   ```bash
   docker run -d -p 6379:6379 --name redis-server redis
   ```
4. Run the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Access the API documentation:
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
### Authentication
- **Register a User** (`POST /auth/register`)
  - **Input:** `username`, `password`, `full_name`
  - **Output:** Success or error message

- **Login** (`POST /auth/token`)
  - **Input:** `username`, `password`
  - **Output:** JWT access token

- **Token Validation** (`GET /auth/introspect`)
  - **Input:** `token`
  - **Output:** Token validity status

- **Logout** (`POST /auth/logout`)
  - **Input:** `token`
  - **Output:** Logout confirmation message

## Testing
Perform the following test cases:
1. Register a user.
2. Obtain a token via login.
3. Validate the token.
4. Logout and ensure the token is invalidated.
5. Test with multiple users to verify independent sessions.
6. Attempt authentication with an expired or invalid token.

## Deployment
1. **Build and publish Docker image:**
   ```bash
   docker build -t your-username/tp4-authentication .
   docker push your-username/tp4-authentication
   ```
2. **Setup GitHub Actions for CI/CD:**
   - Add a workflow to run tests and check formatting on pull requests.

## Additional Features (Optional)
- **Improved UI:** Create a frontend for better user interaction.
- **Security Enhancements:** Implement password complexity checks and login attempt limits.

## Deliverables
- Source code (.zip format)
- Commit hash matching the uploaded code
- README.md with installation and usage instructions

## Author
Leandro Videla

---
This README provides a comprehensive guide for setting up and using the authentication system, ensuring a smooth deployment and testing process.

