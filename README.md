💼 HR Salary Prediction App

This project predicts a candidate’s salary based on their experience, test score, and interview performance using a machine learning model. It’s fully containerized with Docker and deployed using Kubernetes on Google Cloud Platform (GCP).

🔍 Features

ML-powered salary prediction

Clean frontend UI

REST API using Flask

Docker containerized

Kubernetes deployment (GKE)

Public Docker image available on Docker Hub

📦 Try it with Docker

Pull the image directly from Docker Hub:

docker pull bharath0011/hiring_api:latest
docker run -p 5000:5000 bharath0011/hiring_api

Then open frontend.html in your browser and enter values to get a salary prediction.

🧠 Tech Stack

Python, Flask

Scikit-learn, Pandas

HTML + JS for frontend

Docker

Google Kubernetes Engine (GKE)

📁 Project Files

main.py: Flask backend

frontend.html: Web UI

hr_analytics.pkl: ML model

Dockerfile: For containerization

requirements.txt: Dependencies

hr_analytics.ipynb: Model training

gcp_commands.txt: GCP + Kubernetes setup steps

🌐 Live Deployment (GCP)

This project is deployed on Google Cloud Kubernetes Engine (GKE). A LoadBalancer exposes the service to the internet.

🙋‍♂️ Author

Bharath Kumar📦 Docker Hub: https://hub.docker.com/repositories/bharath0011,
🔗 LinkedIn: https://www.linkedin.com/in/bharath-kumar-reddy-4a5675289 
📧 Email: bharath0124r@gmail.com

📄 License

MIT License – feel free to fork and build on it!

