#!/usr/bin/env groovy

def call(){
    echo "building the docker image... from groovy "
    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
        sh 'docker build -t rahulkumarpaswan/python-demo:1.0 .'
        sh "echo $PASS | docker login -u $USER --password-stdin"
        sh 'docker push rahulkumarpaswan/python-demo:1.0'
    }
}