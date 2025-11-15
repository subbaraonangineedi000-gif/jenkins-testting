pipeline {
    agent {
        docker { image 'python:3.14.0-alpine3.22' }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building in Python container...'
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Python script...'
                sh 'python hello.py'
            }
        }
    }
}
