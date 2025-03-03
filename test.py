import os

from sqlalchemy.engine.url import make_url



DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ajitesh:Exponents%40123@localhost:5432/generative_ai_db")



try:

    parsed_url = make_url(DATABASE_URL)

    print(f"Driver: {parsed_url.drivername}")

    print(f"Username: {parsed_url.username}")

    print(f"Password: {parsed_url.password}")

    print(f"Host: {parsed_url.host}")

    print(f"Port: {parsed_url.port}")

    print(f"Database: {parsed_url.database}")

except Exception as e:

    print(f"Error parsing database URL: {e}")