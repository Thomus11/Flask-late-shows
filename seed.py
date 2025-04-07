from app import app, db
from models import Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        episodes = [
            Episode(date="3/15/01", number=7),
            Episode(date="4/22/01", number=8),
            Episode(date="5/10/01", number=9)
        ]
        db.session.add_all(episodes)

        guests = [
            Guest(name="Joan Wambui", occupation="actress"),
            Guest(name="Thomus Maina", occupation="comedian"),
            Guest(name="Brian Iraru", occupation="talk show host")
        ]
        db.session.add_all(guests)

        appearances = [
            Appearance(rating=5, episode_id=7, guest_id=1),
            Appearance(rating=4, episode_id=8, guest_id=3),
            Appearance(rating=3, episode_id=9, guest_id=2)
        ]
        db.session.add_all(appearances)

        db.session.commit()

if __name__ == '__main__':
    seed_database()