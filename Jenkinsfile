pipeline {
  agent any
  
  stages{

    stage('Increment Version') {
      steps {
          script {
            echo "Hello Dear"
            // Read the current version from setup.py
            def currentVersion = sh(script: "grep -oP \"(?<=version=')([^\']*)\"", returnStdout: true).trim()

            // Split the version into major, minor, and patch parts
            def versionParts = currentVersion.split('.')
                    
            // Increment the patch part
            versionParts[-1] = String.valueOf(versionParts[-1].toInteger() + 1)
                    
            // Join the version parts back together
            def newVersion = versionParts.join('.')
                    
            // Update the setup.py file with the new version
            sh "sed -i \"s/version='${currentVersion}'/version='${newVersion}'/\" setup.py"
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



