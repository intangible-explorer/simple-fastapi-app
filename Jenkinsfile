pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                echo "checkout"
            }
        }
        stage("Test") {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage("Deploy DEV Environment") {
            steps {
                sh '''
                git pull origin main
                fastapi dev main.py
                '''
            }
        }
    }
}
