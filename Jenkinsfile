pipeline {
    agent any

    environment {
        VENV = '.venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh 'python -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '. .venv/bin/activate && flake8 app'
            }
        }

        stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest'
            }
        }

        stage('Code Quality') {
            steps {
                sh 'sonar-scanner'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo_service .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8000:8000 --name todo_service todo_service'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}