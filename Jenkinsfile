pipeline {
    agent {
        docker {
            image 'python:3.14.0-alpine3.22'
            args '-u root:root' // Optional: run as root if needed
            registryCredentialsId 'dockerhub_id' // Add this line for Docker Hub credentials
        }
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
