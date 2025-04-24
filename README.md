# AWS Flask Demo Project

This is a basic Flask web app intended to be hosted on AWS EC2. It's configured to work with Gunicorn and optionally Nginx.

## Features
- Flask backend served via Gunicorn
- AWS EC2 deployment-ready
- Includes wsgi.py entry point

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run locally:
```bash
python wsgi.py
```

3. For production (on EC2):
```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

![Flask App Screenshot](https://raw.githubusercontent.com/supernova117/aws-flask-ec2-s3-demo/main/flask-demo-screenshot.png)

## Author
Armend Daci | AWS Certified Solutions Architect


