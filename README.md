# Ship Detection

Welcome! This is the github repository of the Ship Detection project that lives at https://jaygala223-ship-detection--homepage-bjv4aj.streamlit.app/

The aim of this application is to create awareness about the dangers of illegal fishing and also to present a solution for this problem. 

There are 2 main sections to this project:
1. Detecting of ships from satellite imagery using Deep Learning techniques and
2. Identifying whether a ship was located inside a Marine Protected Area (MPA) using GeoSpatial data

**Note to future self and other developers:**

Sklearn is known to cause errors like: no such 'module' found.

Solution: `pip3 install sklearn` in your dev environment

For errors related to `protobuf` refer the following links:
https://stackoverflow.com/questions/71759248/importerror-cannot-import-name-builder-from-google-protobuf-internal

https://stackoverflow.com/questions/71906577/python-gprc-attributeerror-nonetype-object-has-no-attribute-message-types-by

Remove tensorflow-intel from the requirements.txt if the deployment on streamlit cloud fails due to `couldn't install requirements`.