from app import create_app
from config import *

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=Config.HOST, port=Config.PORT_API)