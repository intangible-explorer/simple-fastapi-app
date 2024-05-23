pipeline {
    agent any

    environment {
        DEV_SERVER = ""
        GIT_BRANCH = ""
    }

    stages {
        stage("Set Environment") {
            steps {
                script {
                    if (env.BRANCH_NAME == 'int') {
                        env.DEV_SERVER = 'ubuntu@43.205.206.174'
                        env.GIT_BRANCH = 'int'
                    } else if (env.BRANCH_NAME == 'uat') {
                        env.DEV_SERVER = 'ubuntu@65.0.86.51'
                        env.GIT_BRANCH = 'uat'
                    } else if (env.BRANCH_NAME == 'main') {
                        env.DEV_SERVER = 'ubuntu@3.110.159.100'
                        env.GIT_BRANCH = 'main'
                    } else {
                        error("Unsupported branch: ${env.BRANCH_NAME}")
                    }
                }
            }
        }
        
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
        
        stage("Deploy") {
            steps {
                sh '''
                echo "$env.DEV_SERVER"
                echo "$env.GIT_BRANCH"
                '''
                sshagent(['ssh-app-server']) {
                    sh """
                        ssh -tt -o StrictHostKeyChecking=no ${env.DEV_SERVER} << EOF
                            # Kill any process running on port 8000
                            fuser -k 8000/tcp
                            
                            # Navigate to the app directory
                            cd simple-fastapi-app
                            
                            # Pull the latest code from the respective branch
                            git pull origin ${env.GIT_BRANCH}
                            
                            # Activate the virtual environment
                            source venv/bin/activate
                            
                            # Start the FastAPI server in the background
                            nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                            exit
                        EOF
                    """
                }
            }
        }
    }
}
