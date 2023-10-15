import os

from app.main import create_app
from app.main.models import wave, study, patient

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

if __name__ == '__main__':
    app.run(port=3002)