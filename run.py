import os
from app.application import create_app
from flask import g

app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000))
   	)