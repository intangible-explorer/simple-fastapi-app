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
                withCredentials([file(credentialsId: 'test-ssh', variable: 'fastpi')]) {
                    sh '''
                    cat $fastpi
                    ssh -i $fastpi ubuntu@13.232.233.78
                    cd simple-fastapi-app
                    git pull origin main 
                    source env/bin/activate
                    fastapi dev main.py --host 0.0.0.0
                    '''
                }
    // some block
            }
        }
    }
}
