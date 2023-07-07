#!/usr/bin/env groovy

import com.example.Docker

def call(String imageName) {
    echo "building the docker image..."
    return new Docker(this).buildDockerImage(imageName)
} 