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
                            # Kill any process running on port 8000
                            fuser -k 8000/tcp || true
                            
                            # Navigate to the app directory
                            cd simple-fastapi-app
                            
                            # Pull the latest code
                            git pull origin main
                            
                            # Activate the virtual environment
                            source venv/bin/activate
                            
                            # Start the FastAPI server in the background
                            nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                            exit
                        EOF
                    '''
                }
            }
        }
    }
}
