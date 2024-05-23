pipeline {
    agent any

    environment {
        DEV_SERVER = ''
        GIT_BRANCH = ''
    }

    stages {
        stage('Set Environment') {
            steps {
                script {
                    echo "Branch Name: ${env.BRANCH_NAME}"  // Debugging line

                    def devServer = ''
                    def gitBranch = ''

                    if (env.BRANCH_NAME == 'int') {
                        devServer = 'ubuntu@43.205.206.174'
                        gitBranch = 'int'
                    } else if (env.BRANCH_NAME == 'uat') {
                        devServer = 'ubuntu@65.0.86.51'
                        gitBranch = 'uat'
                    } else if (env.BRANCH_NAME == 'main') {
                        devServer = 'ubuntu@3.110.159.100'
                        gitBranch = 'main'
                    } else {
                        error("Unsupported branch: ${env.BRANCH_NAME}")
                    }

                    echo "DEV_SERVER: ${devServer}"  // Debugging line
                    echo "GIT_BRANCH: ${gitBranch}"  // Debugging line

                    env.DEV_SERVER = devServer
                    env.GIT_BRANCH = gitBranch

                    echo "env.DEV_SERVER: ${env.DEV_SERVER}"  // Debugging line
                    echo "env.GIT_BRANCH: ${env.GIT_BRANCH}"  // Debugging line
                }
            }
        }

        stage('Checkout') {
            steps {
                echo 'Checkout'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'venv/bin/pip install -r requirements.txt'
                echo 'Testing Completed'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def deployScript = """
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
                    sh deployScript
                }
            }
        }
    }
}
