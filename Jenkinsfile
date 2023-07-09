pipeline {
  agent any
  
  stages{

    stage('Increment Version') {
      steps {
        script {
          echo " hello dear"
          def currentVersion = sh(
            script: "python3 -c \"import re; match = re.search(r'version=\\\\'(.*?)\\\\'', open('setup.py').read()); print(match.group(1) if match else '143')\"",
              returnStdout: true
              ).trim()
          echo "Previous Version: ${currentVersion}"
          // Split the version into major, minor, and patch parts
                    def versionParts = currentVersion.split('\\.')

                    // Access the version parts using index
                    def major = versionParts[0]
                    def minor = versionParts[1]
                    def patch = versionParts[2]

                    echo "Current Version: ${currentVersion}"
                    echo "Major: ${major}"
                    echo "Minor: ${minor}"
                    echo "Patch: ${patch}"
                    echo "versionParts 1 Version: ${versionParts}"
                    
                    // Increment the patch part
                    versionParts[-1] = String.valueOf(versionParts[-1].toInteger() + 1)
                    echo "versionParts 2 Version: ${versionParts}"
                    
                    // Join the version parts back together
                    def newVersion = versionParts.join('.')
                    echo "newVersion Version: ${newVersion}"
                    
                    // Update the setup.py file with the new version
                    sh "sed -i \"s/version='${currentVersion}'/version='${newVersion}'/\" setup.py"
          echo "Current Version: ${newVersion}"
          env.IMAGE_NAME = "$currentVersion-$BUILD_NUMBER"
          echo "Current IMAGE_NAME: ${IMAGE_NAME}"
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
        sh "docker build -t my-python-project:${IMAGE_NAME} ."
        sh "docker tag my-python-project:${IMAGE_NAME} rahulkumarpaswan/my-python-project:${IMAGE_NAME}"
        sh "docker push rahulkumarpaswan/my-python-project:${IMAGE_NAME}"
      }
    }

  }
}



