import random
from app.db.database import SessionLocal
from app.db.models import Order

db = SessionLocal()
for i in range(200):
    db.add(Order(user_id=random.randint(1,50),
                 amount=round(random.uniform(5,200),2),
                 status=random.choice(["paid","refunded","pending"])))
db.commit()
print("Seeded 200 orders.")