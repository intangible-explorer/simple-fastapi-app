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
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage("Deploy") {
            steps {
                echo "deploy"
            }
        }
    }
}
