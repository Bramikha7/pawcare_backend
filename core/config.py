from dotenv import load_dotenv
import os
load_dotenv()

USERNAME=os.getenv("DB_USERNAME")
PASSWORD=os.getenv("DB_PASSWORD")
HOSTNAME=os.getenv("DB_HOSTNAME")
PORT=os.getenv("DB_PORT")
DATABASE=os.getenv("DB_DATABASE")
