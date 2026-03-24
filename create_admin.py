from app.db.session import SessionLocal, engine
from app.db import models
from app.core.security import hash_password

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

username = input("Nome de usuário: ")
email = input("Email: ")
password = input("Senha: ")

existing = db.query(models.User).filter(models.User.email == email).first()
if existing:
    print("Usuário já existe.")
else:
    user = models.User(
        username=username,
        email=email,
        password=hash_password(password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    print(f"Usuário '{username}' criado com sucesso!")

db.close()
