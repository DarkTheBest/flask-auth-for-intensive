from application import create_app, db
from authentication import models

app = create_app()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
