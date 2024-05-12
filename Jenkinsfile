pipeline {
    agent any
    stages {
        stage('Setup and Activate Virtual Environment and Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Download data') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 src/download_data.py
                '''
            }
        }
         stage('Test dataset') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 tests/test_dataset.py
                '''
            }
        }
        stage('Preprocessing') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 src/preprocessing.py
                '''
            }
        }
        stage('Train model') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 src/train_model.py
                    '''
            }
        }       
    }
    post {
        always {
            sh 'echo "Pipeline completed"'
        }
    }
}
