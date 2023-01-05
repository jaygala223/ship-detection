# ship-detection
Personal project to make a deep learning application to detect ships from satellite imagery

Note to future self and other developers:

Sklearn is known to cause errors like: no such 'module' found.

Solution: `pip3 install sklearn` in your dev environment

For errors related to `protobuf` refer the following links:
https://stackoverflow.com/questions/71759248/importerror-cannot-import-name-builder-from-google-protobuf-internal

https://stackoverflow.com/questions/71906577/python-gprc-attributeerror-nonetype-object-has-no-attribute-message-types-by

Remove tensorflow-intel from the requirements.txt if the deployment on streamlit cloud fails due to `couldn't install requirements`.

image.png