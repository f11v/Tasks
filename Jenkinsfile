pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Tu lógica de compilación
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Aquí irían tus pruebas
            }
        }
    }

    post {
        always {
            echo 'Pipeline has completed.'
        }
        success {
            echo 'Pipeline was successful!'
            sh '''
            curl -X POST -H "Authorization: token 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" \
                 -H "Content-Type: application/json" \
                 -d '{"state": "success", "description": "Pipeline passed successfully!", "context": "CI/CD Jenkins Pipeline"}' \
                 https://api.github.com/repos/f11v/Tasks/statuses/${GIT_COMMIT}
            '''
        }
        failure {
            echo 'Pipeline failed.'
            sh '''
            curl -X POST -H "Authorization: token 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" \
                 -H "Content-Type: application/json" \
                 -d '{"state": "failure", "description": "Pipeline encountered an error.", "context": "CI/CD Jenkins Pipeline"}' \
                 https://api.github.com/repos/f11v/Tasks/statuses/${GIT_COMMIT}
            '''
        }
    }
}