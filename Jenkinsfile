#!/usr/bin/env groovy

@Library('jenkins-shared-library-1.2')

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
                    buildImage()
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
