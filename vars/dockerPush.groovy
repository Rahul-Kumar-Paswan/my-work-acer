#!/usr/bin/env groovy

import com.example.Docker

def call(String imageName){
    echo "pushing the docker image... from groovy from call"
    return new Docker(this).dockerPush(imageName)
}