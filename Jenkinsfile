#!/usr/bin/env groovy

library identifier : 'jenkins-shared-library-1.2@main',retriever:modernSCM([
    $class:'GitSCMSource',
    remote:'https://github.com/Rahul-Kumar-Paswan/jenkins-shared-library-1.2.git',
    credentialsId:'git-credentials'
])

def gv

pipeline {
    agent any
    stages {
        stage("init") {
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }
        stage("checking") {
            steps {
                script {
                    echo "checking"
                    buildJar()
                }
            }
        }
        stage("build image") {
            steps {
                script {
                    echo "building image"
                    buildImage 'rahulkumarpaswan/python-demo:1.7'
                    dockerLogin()
                    dockerPush 'rahulkumarpaswan/python-demo:1.7'
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    echo "deploying"
                    gv.deployApp()
                }
            }
        }
    }   
}
