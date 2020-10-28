pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'This is the best hello world program ever written'
            }
        }
        stage('CheckoutGitrepo') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/shylpasharma/Lesson02-GitHub.git']]])
            }
        }
        stage('Deploy') {
            steps {
                sh '''cd /root
                ./test.py'''
            }
        }
    }
}
