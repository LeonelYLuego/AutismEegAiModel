from . import ai_blueprint
from ..models.wave import Wave
from ...scripts.source import get_result
from flask import jsonify, request

@ai_blueprint.route('/waves', methods=['POST'])
def get_waves():
    data = request.get_json()
    study_id = data['study_id']
    waves = [wave.to_json() for wave in Wave.query.filter_by(studyId=study_id).all()]
    
    result = get_result(waves)

    print(result)

    return jsonify({
        'result': result
    }), 200