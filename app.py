from tempfile import NamedTemporaryFile

import os
import whisper
from flask import Flask, abort, request

# Load the Whisper model:
model = whisper.load_model('tiny')

app = Flask(__name__)

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

# @app.route('/', methods=['POST'])
# def handler():
#     if not request.files:
#         # If the user didn't submit any files, return a 400 (Bad Request) error.
#         abort(400)
#
#     # For each file, let's store the results in a list of dictionaries.
#     results = []
#
#     # Loop over every file that the user submitted.
#     for filename, handle in request.files.items():
#         # Create a temporary file.
#         # The location of the temporary file is available in `temp.name`.
#         temp = NamedTemporaryFile()
#         # Write the user's uploaded file to the temporary file.
#         # The file will get deleted when it drops out of scope.
#         handle.save(temp)
#         # Now we can store the result object for this file.
#         results.append({
#             'filename': filename,
#             'transcript': 'Coming soon!',
#         })
#
#     # This will be automatically converted to JSON.
#     return {'results': results}

@app.route('/', methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        # temp = NamedTemporaryFile(dir=r'D:\flaskProject')
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(r'D:\flaskProject\test.mp3')
        # Let's get the transcript of the temporary file.
        result = model.transcribe(r'D:\flaskProject\test.mp3')
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}


if __name__ == '__main__':
    app.run()
