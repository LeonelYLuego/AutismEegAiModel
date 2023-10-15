from . import ai_blueprint
from ..models.wave import Wave
from flask import jsonify, request
import uuid
from ...scripts.source import get_preprocessed_data

@ai_blueprint.route('/waves', methods=['POST'])
def get_waves():
    data = request.get_json()
    study_id = data['study_id']
    # Parse the study_id to UUID
    study_id = uuid.UUID(study_id)
    alfa = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='alfa').all()]
    beta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='beta').all()]
    gamma = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='gamma').all()]
    delta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='delta').all()]
    theta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='theta').all()]

    preproccesed = get_preprocessed_data([alfa, beta, delta, gamma, theta])

    return jsonify({
        'executive_function': 20,
        'sensory_processing': 20,
        'repetitive_behaviors': 20,
        'motor_skills': 20,
        'persevering thought': 20,
        'social_conscience': 20,
        'verbal_non-verbal_communication': 20,
        'information_processing':20
    })