pipeline {
    agent any
    environment {
        REPO_PATH = "${env.WORKSPACE}" + '/mlops_final_proj/'
    }
    stages {
        stage('Clone repository from Github') {
            steps {
                sh '''
                    if [ -d mlops_final_proj ]; then
                        rm -r mlops_final_proj
                    fi
                    git clone 'https://github.com/sultanovemil/mlops_final_proj.git'
                '''
            }
        }
        stage('Setup and Activate Virtual Environment and Install Dependencies') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install dvc
                '''
            }
        }
        stage('Download data') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    python3 src/download_data.py
                '''
            }
        }
         stage('Test dataset') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    python3 tests/test_dataset.py
                '''
            }
        }
        stage('Preprocessing') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    python3 src/preprocessing.py
                '''
            }
        }
        stage('Train model') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    python3 src/train_model.py
                    dvc add models/rfc_model.pkl
                    git add models/rfc_model.pkl.dvc .dvc/config
                    git commit -m "Add model"
                    '''
            }
        }
        stage('Metrics') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    python3 src/metrics.py
                    '''
            }
        }
        stage('Test model') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    . venv/bin/activate
                    pytest tests/test_model.py
                    '''
            }
        }
        stage('Build docker container') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    docker build -t my_app .
                    '''
            }
        }
        stage('Run docker container') {
            steps {
                sh '''
                    cd ${REPO_PATH}
                    docker run -d -p 8501:8501 my_app
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
