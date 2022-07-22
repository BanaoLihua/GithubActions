from flask_todo import app
from dotenv import load_dotenv
load_dotenv()

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT") , debug=True)