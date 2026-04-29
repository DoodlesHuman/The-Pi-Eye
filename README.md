# The Pi-Eye – Text Reader and Picture Analyzer for Visually Impaired

## Abstract

This project, "The Pi-Eye," addresses the challenges faced by visually impaired students by implementing a low-cost, handy text reader. It utilizes optical character recognition (OCR) and integrates it with a text-to-speech engine. The system is designed to improve accessibility through the application of hard keys and runs on a Raspberry Pi, leveraging the features of the Internet of Things (IoT). The project also includes functionality for object labeling.

## Overview

Visually impaired individuals often struggle with conventional texts and have limited access to specialized materials like Braille books. Existing text readers in the market are typically very expensive. The Pi-Eye project aims to provide an affordable and portable alternative, enabling visually impaired students to access written information by converting it into spoken words. The integration with IoT principles allows for potential future enhancements and connectivity.

## Key Features

* **Optical Character Recognition (OCR):** Converts printed or written text from images into machine-encoded text.
* **Text-to-Speech (TTS) Engine:** Transforms extracted text into audible speech, making it accessible to visually impaired users.
* **Hard Key Accessibility:** Implemented physical buttons for easy and intuitive control of the device.
* **Raspberry Pi Based:** Utilizes a low-cost, credit-card sized computer, making the solution economical and portable.
* **IoT Integration:** Leverages IoT concepts for potential connectivity and data exchange.
* **Object Labeling:** Identifies and labels objects in the environment, providing additional contextual information to the user.

## Technologies Used

* **Hardware:**
    * Raspberry Pi (Primary computing unit)
    * Camera Module (for capturing images for OCR)
    * Input Switches (Hard keys for user interaction)
    * Speaker (for audio output)
    * Power Supply
* **Operating System:**
    * Raspbian (Debian-based OS optimized for Raspberry Pi)
* **Programming Language:**
    * Python
* **Key Libraries and APIs:**
    * **OpenCV (`cv2`):** For various image processing tasks (e.g., image capture, preprocessing).
    * **OCR-Space API:** Cloud-based OCR service for text extraction.
    * **gTTS (Google Text to Speech):** Python library and utility to access Google Text-to-Speech API.
    * **Picamera:** Python library for controlling the Raspberry Pi camera module.
    * **imutils:** A series of convenience functions to make basic image processing functions with OpenCV easier.
    * **NumPy:** Fundamental package for scientific computing with Python, especially for image data manipulation.
    * **Microsoft Azure Computer Vision API:** Used for object detection and labeling.
    * **simplejson:** For efficient JSON encoding/decoding.
    * **RPi.GPIO:** Python module to control the GPIO on a Raspberry Pi.

## Setup Instructions

### Hardware Setup

1.  Connect the Raspberry Pi camera module to the CSI port.
2.  Connect input switches to the appropriate GPIO pins on the Raspberry Pi.
3.  Connect a speaker in the 3.5mm jack for audio output .
4.  Ensure proper power supply to the Raspberry Pi (originally used a power bank (5V, 2A)).

### Software Setup

1.  **Operating System:** Install Raspbian OS on your Raspberry Pi.
2.  **Python Environment:** Ensure Python 3 is installed.
3.  **Install Dependencies:**
     
     * Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
        ```bash
        sudo apt-get install mpg321
        ```
4.  **API Keys:** Include API keys in the code for OCR-Space and Microsoft Azure Computer Vision API.

## Future Scope


* Designing a purpose-oriented computer board for increased power, reduced size, and lower cost.
* Further integration with other IoT devices for a more interconnected system.
* Exploring advanced OCR models for improved accuracy and language support.
* Enhancing object labeling capabilities for wider recognition.

**Amos Ram Rehum**

Submitted to St. Albert's College, Ernakulam, Kerala, (Mahatma Gandhi University, Kottayam) for the partial fulfilment of the awarding of degree of **Master of Science in Physics**

April 2018
