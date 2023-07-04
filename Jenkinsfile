pipeline {
  agent any
  
  stages{
    stage('version') {
      steps {
        echo "Hello Darling"
      }
    }
    stage('checking') {
      steps {
        echo "Welcome to My World !!!!"
      }
    }
    
    stage('build') {
      steps {
        sshagent(['ec2-user-Rahul']) {
            // some block
        }
      }
    }
  }
}
