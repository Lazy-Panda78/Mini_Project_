#!/bin/bash
# EC2 instance bootstrap script (Ubuntu 22.04)
# Run once after launching your EC2 instance

sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose git

# Pull and run the app
git clone https://github.com/YOUR_USERNAME/freshness-classifier.git
cd freshness-classifier
docker-compose up -d

echo "Setup complete. API running at port 8000."
