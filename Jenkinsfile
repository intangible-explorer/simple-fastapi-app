pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh '''
                    apt-get update
                    apt install -y python3-venv
                    cd app/simple-fastapi-app
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage("Unit Testing") {
            steps {
                echo "Running Unit Tests"
                // Add your unit testing commands here
            }
        }

        stage('Deploy to Dev Environment') {
            steps {
                sh '''
                    cd app/simple-fastapi-app
                    source venv/bin/activate && uvicorn --host 0.0.0.0 main:app --port 8001 &
                    '''
                echo "Access your Dev environment application at: http://localhost:8001"
            }
        }

        // Add stages for other environments if needed
    }
}
