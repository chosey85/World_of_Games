pipeline {
    agent any

    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/chosey85/World_of_Games.git'
            }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t World_of_Games .'
            }
        stage('Run Docker Image') {
            steps {
                sh 'docker run -d -p 5000:8777 World_of_Games'
            }
        stage('Test Application') {
            steps {
                sh 'python e2e.py'
            }
        stage('Finalize') {
            steps {
                sh 'docker kill World_of_Games'
                sh 'docker tag World_of_Games: chosey85/worldofgames
            }
        }
    }
}
