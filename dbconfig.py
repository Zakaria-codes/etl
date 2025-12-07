import os
import dotenv
dotenv.load_dotenv()

config = {
    "host":os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database":os.getenv("DATABASE"),
    "allow_local_infile": True
}
