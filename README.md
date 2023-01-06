# Ship Detection

Welcome! This is the github repository of the Ship Detection project that lives at https://jaygala223-ship-detection--homepage-bjv4aj.streamlit.app/

The aim of this application is to create awareness about the dangers of illegal fishing and also to present a solution for this problem. 

There are 2 main sections to this project:
1. Detecting of ships from satellite imagery using Deep Learning techniques: Users can upload satellite images and a CNN that is specially trained for this task will return a probability of that image containing a ship.

2. Identifying whether a ship was located inside a Marine Protected Area (MPA) using GeoSpatial data: Users can enter coordinates of their satellite images. A map marked with MPA boundaries using GEOJSON is then used to determine whether the given point lies within an MPA.

Here are some of the screenshots of the app in action:
![upload an image](https://user-images.githubusercontent.com/57001778/210954323-af81e105-b1d6-4e25-87be-2aff181d6d1f.JPG)
![inside mpa](https://user-images.githubusercontent.com/57001778/210954328-1929794d-9086-471e-99e4-f056b98b1370.JPG)
![no ship](https://user-images.githubusercontent.com/57001778/210954334-556b68a9-aa7d-425e-8ae8-c9179e7eae6f.JPG)
![outside mpa](https://user-images.githubusercontent.com/57001778/210954337-399b0d91-4dd0-4bf9-92cf-a8904a9f430f.JPG)
![ship detected](https://user-images.githubusercontent.com/57001778/210954339-ad3fcc4b-4f66-43f7-a1b3-8f83e5647cf2.JPG)



**Notes for future self and other developers:**

1. Sklearn is known to cause errors like: no such 'module' found.
Solution: `pip3 install sklearn` in your dev environment

2. For errors related to `protobuf` refer the following links:
https://stackoverflow.com/questions/71759248/importerror-cannot-import-name-builder-from-google-protobuf-internal
https://stackoverflow.com/questions/71906577/python-gprc-attributeerror-nonetype-object-has-no-attribute-message-types-by

3. Remove tensorflow-intel from the requirements.txt if the deployment on streamlit cloud fails due to `couldn't install requirements`.
