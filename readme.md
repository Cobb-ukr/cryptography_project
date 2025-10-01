# Flask Encryption/Decryption App

## Description

This is a Flask web application that allows users to encrypt and decrypt text using a password. The app supports all types of characters, including letters, numbers, spaces, and special symbols. The project is containerized with Docker for easy deployment.

## Features

* Encrypt any text with a password
* Decrypt encrypted text using the same password
* Copy the output to clipboard
* Reset all fields for a clean interface

## Project Structure

```
flask-crypto-app/
├─ app.py
├─ converter.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ templates/
│   └─ index.html
├─ static/
│   └─ index.css
└─ .gitignore
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd flask-crypto-app
```

### 2. Build and run with Docker

```bash
docker build -t flask-crypto-app .
docker run -p 5000:5000 flask-crypto-app
```

Or using docker-compose:

```bash
docker-compose up --build
```

### 3. Access the app

Open a browser and go to:

```
http://localhost:5000
```

## Usage

1. Enter text to encrypt or decrypt.
2. Enter a password.
3. Click **Encrypt** or **Decrypt**.
4. Copy the result or reset the form as needed.

## Requirements

* Python 3.12+
* Flask
* cryptography
* Docker (optional, for containerized setup)
