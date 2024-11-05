pipeline {
    agent any
 
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Yaswanth0402/demo_jenkins', branch: 'main'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                bat '''
                    python pip install pytest
                '''
            }
        }
 
        stage('Run Tests') {
            steps {
                bat 'pytest test_main.py'
            }
        }
    }
 
    post {
        always {
            echo 'Build finished'
        }
    }
}
