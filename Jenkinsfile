pipeline {
    agent any
    environment {
        PATH = "C:\\Users\\sanikommu.yaswanth.TL592\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\sanikommu.yaswanth.TL592\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Yaswanth0402/demo_jenkins', branch: 'main'
            }
        }

        stage('Verify Python Installation') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install pytest'
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
