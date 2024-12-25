from db.db_engine import SessionLocal


# Dependency для получения DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
