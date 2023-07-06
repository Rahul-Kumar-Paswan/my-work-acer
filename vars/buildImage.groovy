#!/usr/bin/env groovy

def buildImage() {
    echo "building the docker image..."
    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
        sh 'docker build -t rahulkumarpaswan/python-demo:1.1 .'
        sh "echo $PASS | docker login -u $USER --password-stdin"
        sh 'docker push rahulkumarpaswan/python-demo:1.1'
    }
} 