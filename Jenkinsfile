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
        script {
            def dockerCmd = 'docker run -d --name rahul-project -p 3000:3000 rahulkumarpaswan/my-python-project:1.2'
            sshagent(['ec2-user-Rahul']) {
                // some block
                sh "ssh -o StrictHostKeyChecking=no ec2-user@13.232.90.226 ${dockerCmd}"
            }
        }
      }
    }
  }
}
