# Portal Turret Lamp

This repository contains both the Python project required to run the portal turret code in addition to the CAD files required to construct the project. Some important notes are highlighted below:

* The YOLO object detection system was implemented in order for the software to detect faces. This project uses a pretrained model available in the `yoloface` respository on GitHub available [here](https://github.com/sthanhng/yoloface).
* The `yoloface` weights file can be downloaded using the script `yoloface/download-model.sh`. This script was adapted from the script installer in the `yoloface` respository. The `yolov3-face.cfg` file has already been copied into this directory for convenience.
* The image specified in `detect_in_image.py` can be changed to any image file and it is used for testing out `yoloface`. Both test images in `assets/` are random images from online.

## Setup

To allow for the proper installation of the Python module `simpleaudio` the package `libasound2-dev` must be installed on the host system. On Ubuntu-derived systems, the command is the following:

```bash
sudo apt install libasound2-dev
```

Install the dependencies onto either the system or a Python virtual environment with the following:

```bash
pip install -r requirements.txt
```

## Running

Navigate to the `src/` directory and run the following command. Note that the escape button is used to quit.

```bash
python turret.py
```

Ensure your webcam is uncovered and move your head in and out of view. The turret will start in a "undeployed" state but will change if it sees a face and a voice line will be played. Note that when there all faces leave the field of view, the turret will begin "searching" and if a face is not reintroduced in 5 seconds after searching audio line begins, the turret will "deactivate". This is the original state of the turret at the start of running the application.