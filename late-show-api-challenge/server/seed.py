from datetime import date
from server.app import create_app, db
from .models.guest import Guest
from .models.episode import Episode
from .models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Ali Sheikh", occupation="Comedian")
    guest2 = Guest(name="Nourah Noor", occupation="Musician")
    
    ep1 = Episode(date=date(2025, 6, 1), number=1)
    ep2 = Episode(date=date(2025, 6, 2), number=2)

    db.session.add_all([guest1, guest2, ep1, ep2])
    db.session.commit()

    app1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    app2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep2.id)

    db.session.add_all([app1, app2])
    db.session.commit()

    print("Seeded database 🎉")
