from sqlalchemy.dialects.postgresql import UUID
import uuid
from .. import db

# Define the Wave model based on Base
class Wave(db.Model):
    __tablename__ = "wave"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    studyId = db.Column(UUID(as_uuid=True), db.ForeignKey('study.id'), nullable=False)
    time = db.Column(db.Float, nullable=False)
    # Define the type column as an enum
    type = db.Column(db.Enum('alfa', 'beta', 'gamma', 'delta', 'theta', name='wave_type'), nullable=False)
    channel1 = db.Column(db.Float, nullable=False)
    channel2 = db.Column(db.Float, nullable=False)
    channel3 = db.Column(db.Float, nullable=False)
    channel4 = db.Column(db.Float, nullable=False)
    channel5 = db.Column(db.Float, nullable=False)
    channel6 = db.Column(db.Float, nullable=False)
    channel7 = db.Column(db.Float, nullable=False)
    channel8 = db.Column(db.Float, nullable=False)
    channel9 = db.Column(db.Float, nullable=False)
    channel10 = db.Column(db.Float, nullable=False)
    channel11 = db.Column(db.Float, nullable=False)
    channel12 = db.Column(db.Float, nullable=False)
    channel13 = db.Column(db.Float, nullable=False)
    channel14 = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            'time': self.time,
            'channel1': self.channel1,
            'channel2': self.channel2,
            'channel3': self.channel3,
            'channel4': self.channel4,
            'channel5': self.channel5,
            'channel6': self.channel6,
            'channel7': self.channel7,
            'channel8': self.channel8,
            'channel9': self.channel9,
            'channel10': self.channel10,
            'channel11': self.channel11,
            'channel12': self.channel12,
            'channel13': self.channel13,
            'channel14': self.channel14
        }
    
    # Define the __repr__ method
    def __repr__(self):
        return f"<Wave '{self.id}-{self.studyId}'>"