#Installing Kivy for Python.

#Ensure you are on a supported version of Python before you begin.
#Ensure you only have one version of Python installed and only the current installed version has a directory in: "C:\Users\USERNAME\AppData\Local\Programs\Python"

#Install Prerequisites.
python -m pip install --upgrade pip wheel setuptools
python -m pip install pygame
python -m pip install cython
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2 kivy_deps.glew
python -m pip install kivy_deps.gstreamer
python -m pip install kivy_deps.angle #(Install if Python 3.5+)

#Install Kivy.
python -m pip install kivy
python -m pip install kivy_examples



#Start here if encountering issues...

#Location:
#Control Panel\System and Security\System\Advanced system settings\Environment Variables...\System variables

#To:
#Add to: "Path", "PYTHONPATH" (Create variable if needed...)

#What:
C:\Users\Justin\AppData\Local\Programs\Python\Python37
C:\Users\Justin\AppData\Local\Programs\Python\Python37\DLLs
C:\Users\Justin\AppData\Local\Programs\Python\Python37\Lib
C:\Users\Justin\AppData\Local\Programs\Python\Python37\Scripts
C:\Users\Justin\AppData\Local\Programs\Python\Python37\Lib\site-packages
