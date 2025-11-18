pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')   // your Jenkins Docker Hub creds ID
        IMAGE_NAME = 'subbu4540/hello-app:test'               // your Docker Hub image
    }

    stages {
        stage('Use Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        docker.image(IMAGE_NAME).inside {
                            sh 'python hello.py'          // run command inside container
                        }
                    }
                }
            }
        }
    }
}
