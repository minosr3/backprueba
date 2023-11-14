from app import createApp, db

app = createApp('development')

with app.app_context():
    db.create_all()  

if __name__ == '__main__':
    app.run()