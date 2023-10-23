from . import ai_blueprint
from .. import db
from ..models.wave import Wave
from ..models.study import Study
from ...scripts.source import get_preprocessed_data
from flask import jsonify, request
import uuid
import random

@ai_blueprint.route('/waves', methods=['POST'])
def get_waves():
    data = request.get_json()
    study_id = data['study_id']
    # Parse the study_id to UUID
    waves = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id).all()]
    
    preproccesed = get_preprocessed_data(waves)

    return jsonify({
        'result': 20
    }), 200