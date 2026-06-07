from app.core.database import SessionLocal
from app.models.officer import Officer, OfficerRole
from app.core.security import hash_password

def create_first_admin():
    db = SessionLocal()
    try:
        # Check if an admin already exists to prevent duplicates
        existing_admin = db.query(Officer).filter(Officer.username == "admin").first()
        if existing_admin:
            print("Admin user 'admin' already exists!")
            return

        # Create the new admin officer
        new_admin = Officer(
            full_name="System Administrator",
            username="admin",
            password_hash=hash_password("admin123"), # Securely hashing the password
            assigned_place="Headquarters",
            role=OfficerRole.admin
        )
        
        db.add(new_admin)
        db.commit()
        
        print("✅ Successfully created the first admin user!")
        print("➡️ Username: admin")
        print("➡️ Password: admin123")
        
    except Exception as e:
        print(f"❌ Error creating admin: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_first_admin()