#!/bin/bash

# Update the packages
sudo apt-get update
sudo apt-get upgrade

# Check if an initial argument is passed for the target directory
if [ $# -eq 0 ]; then
    DATA_DIR="./src/"
else
    DATA_DIR="$1"
fi

# Install Python dependencies
python3 -m pip install pip --upgrade
python3 -m pip install -r requirements.txt

# Set the file path for the default TFLite model
FILE=${DATA_DIR}/efficientdet_lite0.tflite

# Check if the file already exists
if [ ! -f "$FILE" ]; then
# Download the TFLite model
  curl \
    -L 'https://storage.googleapis.com/download.tensorflow.org/models/tflite/task_library/object_detection/rpi/lite-model_efficientdet_lite0_detection_metadata_1.tflite' \
    -o ${FILE}
fi

# Set the file path for the Edge TPU TFLite model
FILE=${DATA_DIR}/efficientdet_lite0_edgetpu.tflite

# Check if the file already exists
if [ ! -f "$FILE" ]; then
# Download the TFLite model
  curl \
    -L 'https://storage.googleapis.com/download.tensorflow.org/models/tflite/task_library/object_detection/rpi/efficientdet_lite0_edgetpu_metadata.tflite' \
    -o ${FILE}
fi


echo -e "Downloaded files are in {$DATA_DIR}"
