pipeline {
    agent any

    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/chosey85/World_of_Games.git'
                  }
                }
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
                  }
                }
        stage('Run Docker Image') {
            steps {
                sh 'docker-compose up'
                  }
                }
        stage('Test Application') {
            steps {
                sh 'python3 e2e.py'
                def exitcode = sh script: 'echo $?', returnStatus: true
                    if (exitCode != 0) {
                        sh 'docker-compose down'
                        error('The e2e application failed with exit code: ' + exitCode)
                    }
                  }
                }   
        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker login -u chosey85 -p XXXXXX'
                    sh 'docker-compose push'
                           }
                        }
                    }
            }
        }