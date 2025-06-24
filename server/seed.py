from server.app import create_app
from server.models import db, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    
    g1 = Guest(name="Robert Downey Jr.", occupation="Actor")
    g2 = Guest(name="Beyoncé", occupation="Singer")
    g3 = Guest(name="Elon Musk", occupation="Entrepreneur")

    
    e1 = Episode(date="2025-06-01", number=1)
    e2 = Episode(date="2025-06-02", number=2)


    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e1)
    a3 = Appearance(rating=3, guest=g3, episode=e2)

    
    db.session.add_all([g1, g2, g3, e1, e2, a1, a2, a3])
    db.session.commit()

    print("✅ Done seeding!")
