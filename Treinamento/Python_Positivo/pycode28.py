import os
import pytest
import re
import uuid

os.environ['GOOGLE_CLOUD_PROJECT'] = os.environ['FIRESTORE_PROJECT_ID']
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        'firestore-service-account.json'
    )
)

import main


@pytest.fixture
def client():
    """ Yields a test client, AND creates and later cleans up a
        dummy collection for sessions.
    """
    main.app.testing = True

    # Override the Firestore collection used for sessions in main
    main.sessions = main.db.collection(str(uuid.uuid4()))

    client = main.app.test_client()
    yield client

    # Clean up session objects created in test collection
    for doc_ref in main.sessions.list_documents():
        doc_ref.delete()


def test_session(client):
    r = client.get('/')
    assert r.status_code == 200
    data = r.data.decode('utf-8')
    assert '1 views' in data

    match = re.search('views for ([A-Za-z ]+)', data)
    assert match is not None
    greeting = match.group(1)

    r = client.get('/')
    assert r.status_code == 200
    data = r.data.decode('utf-8')
    assert '2 views' in data
    assert greeting in data