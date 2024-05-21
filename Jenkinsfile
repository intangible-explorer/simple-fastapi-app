pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                script {
                    setupBackend()
                }
            }
        }

        stage("Unit Testing") {
            steps {
                echo "Running Unit Tests"
            }
        }

        stage('Deploy to Dev Environment') {
            steps {
                script {
                    deployToLocal('dev', 8001)
                }
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                script {
                    deployToLocal('test', 8002)
                }
            }
        }

        stage('Deploy to Prod Environment') {
            steps {
                script {
                    deployToLocal('prod', 8003)
                }
            }
        }
    }
}

def setupBackend() {
    def appPath = 'app/'
    sh "apt install -y python3-venv"
    sh "cd ${appPath} && python3 -m venv venv && source venv/bin/activate"
    sh "pip install -r /simple-fastapi-app/requirements.txt"
}

def deployToLocal(environment, port) {
    def appPath = 'app/'
    def appPort = port
    
    sh "cd ${appPath}/simple-fastapi-app/"
    sh "uvicorn --host 0.0.0.0 main:app --port ${appPort}"
    
    echo "Access your ${environment} environment application at: http://localhost:${appPort}"
}
