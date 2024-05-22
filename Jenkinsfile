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
        stage("Deploy") {
            steps {
                sh '''
                git pull 
                fastapi dev main.py
                '''
            }
        }
    }
}
