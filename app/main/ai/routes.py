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
    study_id = uuid.UUID(study_id)
    alfa = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='alfa').all()]
    beta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='beta').all()]
    gamma = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='gamma').all()]
    delta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='delta').all()]
    theta = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id, type='theta').all()]

    preproccesed = get_preprocessed_data(alfa, beta, delta, gamma, theta)

    study = Study.query.filter_by(id=study_id).first()

    keys = ['executiveFunction', 'sensoryProcessing', 'repetitiveBehaviours', 'motorSkills', 'perseverativeThinking', 'socialAwareness', 'verbalNoVerbalCommunication', 'informationProcessing']
    for i in range(len(keys)):
        # Get a random decimal between 0 and 100
        random_decimal = random.uniform(0, 100)
        # Set the value of the key to the random decimal
        study.__setattr__(keys[i], random_decimal)
    
    # Save the changes of the study
    db.session.commit()


    return jsonify({
        'executive_function': study.executiveFunction,
        'sensory_processing': study.sensoryProcessing,
        'repetitive_behaviors': study.repetitiveBehaviours,
        'motor_skills': study.motorSkills,
        'perseverative_thinking': study.perseverativeThinking,
        'social_awareness': study.socialAwareness,
        'verbal_no_verbal_communication': study.verbalNoVerbalCommunication,
        'information_processing': study.informationProcessing,
    }), 200