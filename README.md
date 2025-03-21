ATOM AI Assistant (AiTOMM)

Overview

AiTOMM (AI Technology for Operational and Multimedia Management) is an advanced AI assistant designed to enhance user interactions with computing devices. It features natural language processing, voice recognition, face recognition, multimedia controls, and various automation capabilities.

Features

Natural Language Processing (NLP) – Understands and processes user commands efficiently.

Voice & Audio Interaction – Allows users to interact via voice commands.

Conversational Memory – Retains past conversations for a personalized experience.

Face Recognition – Securely identifies users.

Multimedia Control – Plays YouTube videos, adjusts volume, and manages applications.

System & Web Integration – Controls PC applications, performs Google searches, and sends WhatsApp messages.

Location & Date/Time Awareness – Provides location-based and time-sensitive responses.

Object Detection – Identifies objects using YOLOv4.

Weather & Temperature Updates – Fetches real-time weather data.

Technology Stack

Backend: Python (Flask, SpeechRecognition, Pyttsx3, OpenCV, PyWhatKit)

Frontend: HTML, CSS, JavaScript

AI/ML: NLP Models (Llama 3, Groq)

Databases: JSON for memory storage, CSV for command mapping

Installation

Prerequisites

Ensure you have the following installed:

Python 3.8+

Required Python libraries:

pip install groq pyaudio numpy keyboard SpeechrRcognition pygame pyautogui pywhatkit pynput playsound pyttsx3 numpy beautifulsoup4 requests pywhatkit opencv-python face_recognition

Additional Dependencies:

CMake for Face Recognition module

Groq & Llama 3 API access for NLP

yolov4.cfg for Object Detection

Steps to Run

Clone the repository:

git clone https://github.com/yourusername/AiTOMM.git

Navigate to the project folder:

cd AiTOMM

Run the main script:

python main.py

Use voice commands or text input to interact with the AI assistant.

Usage

Example Commands

"Play a video on YouTube"

"Send a WhatsApp message to [contact]"

"What's the weather today?"

"Close all apps and shut down the system"

"Recognize my face"

Roadmap & Future Enhancements

Improved Speech-to-Text Accuracy – Integrate OpenAI Whisper model.

Enhanced UI – Develop a web-based interactive dashboard.

Expanded Automation – Add support for smart home devices.

Better Memory Handling – Implement user profiles and selective memory retention.

Contributors

Shounak Das (Team Leader, Backend Development)

Sarbojit Ghosh (Backend & Frontend Development)

Sirin Bhattacharya & Srijani Ghosh (UI/UX Design & Implementation)

Krishnayan Bhadra (Documentation & Testing)

Mentor: Prof. Kushol Roy

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Special thanks to our mentor and Future Institute of Engineering and Management for their support.
