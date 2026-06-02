from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

DEFAULT_MODEL = os.environ.get('DEFAULT_MODEL')

AI_API_KEY = os.environ.get('AI_API_KEY')
AI_BASE_URL = os.environ.get('AI_BASE_URL')
DEFAULT_MODEL = os.environ.get('DEFAULT_MODEL')