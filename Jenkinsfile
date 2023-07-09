pipeline {
  agent any
  
  stages{

    stage('Increment Version') {
      steps {
        script {
          echo " hello dear"
          def currentVersion = sh(
                        script: "python3 -c \"import re; match = re.search(r'version=(\\\\'.*\\\\')', open('setup.py').read()); print(match.group(1)[1:-1] if match else '143')\"",
                        returnStdout: true
                    ).trim()

                    echo "Current Version: ${currentVersion}"
        }
      }
    }

    stage('checking') {
      steps {
        echo " hello dear welcome to  my world !!!!"
      }
    }
    
    stage('build') {
      steps {
        echo "hello"
        sh 'docker build -t my-python-project:1.2 .'
        sh 'docker tag my-python-project:1.2 rahulkumarpaswan/my-python-project:1.2'
        sh 'docker push rahulkumarpaswan/my-python-project:1.2'
      }
    }

  }
}



