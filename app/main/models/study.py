from sqlalchemy.dialects.postgresql import UUID, VARCHAR
import uuid
# Import the Base class
from .. import db

# Define the Study model based on Base
class Study(db.Model):
    __tablename__ = "study"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    patientId = db.Column(UUID(as_uuid=True), db.ForeignKey('patient.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    result = db.Column(VARCHAR(255), nullable=False)

    # Define the __init__ method
    def __init__(self, patient_id, datetime, result):
        self.patient_id = patient_id
        self.datetime = datetime
        self.result = result
    
    # Define the __repr__ method
    def __repr__(self):
        return f"<Study '{self.id}-{self.datetime}'>"
