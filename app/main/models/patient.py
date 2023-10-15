from sqlalchemy.dialects.postgresql import UUID
import uuid
from .. import db

# Define the Patient model based on Base
class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    # Define the __repr__ method
    def __repr__(self):
        return f"<Patient '{self.name}'>"
