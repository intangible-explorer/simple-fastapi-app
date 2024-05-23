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
                echo 'Testing Completed'
            }
        }
        stage("Deploy DEV Environment") {
            steps {
                sshagent(['ssh-app-server']) {
                    sh '''
                        ssh -tt -o StrictHostKeyChecking=no ubuntu@13.232.233.78 << EOF
                            cd simple-fastapi-app
                            git pull origin main
                            source env/bin/activate
                            nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                        EOF
                    '''
                }
            }
        }
    }
}
