# Object detection model on Raspberry Pi 4
> A real-time object detection model on Raspberry Pi 4 using TensorFlow module on Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Static Badge](https://img.shields.io/badge/Raspberry_OS-Bullseye-brown)](https://www.raspberrypi.com/software/operating-systems/)
[![Static Badge](https://img.shields.io/badge/Python-3.9.2-blue)](https://www.python.org/downloads/release/python-392/)

<div align="center">
    <img src="https://github.com/CheesyFrappe/object-detection-on-raspberry-pi/assets/80858788/e56bea78-be0f-43f3-9e1e-aa2f4efd61f0"/>
</div><be>

---

### Table of contents:
- [Introduction](#introduction)
- [Prerequisities](#prerequisities)
- [Usage](#usage)

# Introduction
This project uses [TensorFlow Lite](https://www.tensorflow.org/lite) with Python on a Raspberry Pi to perform real-time object detection using images streamed from the Pi Camera. It draws a bounding box around each detected object in the camera preview (when the object score is above a given threshold).<br>

In this project, transfer learning is used which allows you to use pre-trained models. [TensorFlow](https://www.tensorflow.org/lite/models/trained) provides pre-trained models for common use cases.
[EfficientDet-Lite0](https://www.tensorflow.org/lite/models/modify/model_maker/object_detection) is the model that was used in the project. Check out the [Prerequisities](#prerequisities) for the installation of the needed models.

Coral USB Accelerator was not used in the project however, the source code supports the Coral Accelerator. Check out the [Usage](#usage).

# Prerequisities
> [!IMPORTANT]
> The project was written/tested on Raspberry OS 32-bit Bullseye. The `tflite-support` library only supports Python `3.7` - `3.9` at this moment.
> Bullseye comes with `Python 3.9` as default. If you're using Bookworm or other OS releases, I recommend you check your Python version and be sure `tflite-support` supports the needed sub-modules for this project.

<div align="center">
    <img src="https://github.com/CheesyFrappe/object-detection-on-raspberry-pi/assets/80858788/e0154ee7-f796-4a9b-adaf-208610b52e97"/>
</div>

> [!IMPORTANT]
> Using a Python virtual environment is highly recommended for the usage. Installing packages with `sudo pip` will install packages globally, which may break some system tools. On the other hand, `virtualenv` avoids the need to install Python packages globally.

To install the requirements, first create a Python virtual environment:
```shell
$ python3 -m venv ENV_DIR
```
`ENV_DIR` should be a non-existent directory. The directory can have any name, but to keep these instructions simple, I will assume you have created your virtualenv in a directory called venv (e.g. with `python3 -m venv tflite`).

To work in your virtualenv, you activate it:
```shell
$ source ./tflite/bin/activate
```
Also, you can get out of the virtualenv by deactivating it:
```shell
(tflite)$ deactivate
$ 
```

In the virtual environment you just created, clone the repository and type in the directory:
```shell
(tflite)$ sh setup.sh
```
This will upgrade your packages and pip then, install the required Python modules along with the pre-trained models.

# Usage
> [!IMPORTANT]
> CSI camera module is used as default in the source code. If you're using a WebCam, modify the subprogram call in the `main.py` on `detect.py`.

If you're using a WebCam, change the subprogram call in `main.py` to:
```python
# detect(True, DISPLAY_WIDTH, DISPLAY_HEIGHT, THREAD_NUM, False)
detect(False, DISPLAY_WIDTH, DISPLAY_HEIGHT, THREAD_NUM, False)
```
To run the project, change the directory to `./src` and type:
```shell
(tflite)$ python3 detect.py
```
<br>

> [!NOTE]
> If you are getting an error like:

>ImportError: /lib/aarch64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by ~/.local/lib/python3.9/site-packages/tensorflow_lite_support/metadata/cc/python/_pywrap_metadata_version.so)

Downgrade your `tflite-support` from version `0.4.4` (current) to `0.4.3` using the following command:
```shell
(tflite)$ python -m pip install --upgrade tflite-support==0.4.3
```

---
<br>
<div align="center">
    <img src="https://github.com/CheesyFrappe/object-detection-on-raspberry-pi/assets/80858788/7278d35e-cce8-45b7-aab0-5c840ccd3dc0"/>
    <i>taken on this project</i>
</div><br>

You should see the camera feed appear on the monitor attached to your Raspberry Pi. Put some objects in front of the camera, like a coffee mug or keyboard, and you'll see boxes drawn around those that the model recognizes, including the label and score for each. It also prints the number of frames per second (FPS) at the top-left corner of the screen. As the pipeline contains some processes other than model inference, including visualizing the detection results, you can expect a higher FPS if your inference pipeline runs in headless mode without visualization.

## Speed up model inference (with Coral USB Accelerator)
If you want to significantly speed up the inference time, you can attach an
[Coral USB Accelerator](https://coral.withgoogle.com/products/accelerator)—a USB
accessory that adds the
[Edge TPU ML accelerator](https://coral.withgoogle.com/docs/edgetpu/faq/) to any
Linux-based system.

If you have a Coral USB Accelerator, you can run the sample with it enabled:

1.  First, be sure you have completed the
    [USB Accelerator setup instructions](https://coral.withgoogle.com/docs/accelerator/get-started/).

2.  Run the object detection script using the EdgeTPU TFLite model and enable
    the EdgeTPU option. Be noted that the EdgeTPU requires a specific TFLite
    model that is different from the one used above.
    Change the subprogram call in `main.py` to:

```python
# detect(False, DISPLAY_WIDTH, DISPLAY_HEIGHT, THREAD_NUM, False)
detect(False, DISPLAY_WIDTH, DISPLAY_HEIGHT, THREAD_NUM, True)
```
Then run:
```shell
(tflite)$ python3 detect.py
```

You should see significantly faster inference speeds.





