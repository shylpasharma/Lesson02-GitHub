pipeline {
  environment {
    registry = "shilpa1606/ubuntu"
    registryCredential = 'dockerhub'
  }
  agent any
  stages {
        stage("Cloning git") {
            steps {
                git "https://github.com/shylpasharma/Lesson02-GitHub.git"
            }
        }
        stage("Building Image") {
            steps{
            script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
            }
        }
    }
        stage("Deploy Image") {
        steps{
            script {
                docker.withRegistry( "", registryCredential ) {
                    dockerImage.push()
            }
        }
      }
    }
  }
}
