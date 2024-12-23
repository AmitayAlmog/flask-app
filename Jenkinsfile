pipeline{
    agent any
    stages{
        stage("checkout scm"){
            steps{
                checkout scm
            }
        }

        stage("build docker image"){
            steps{
                echo "building docker image"
                sh "docker build -t amitay/flask-app ."
                 
            }
        }

        stage("push docker image"){
            when {
                branch "main"
            }
            steps{
                echo "pushing docker image"
            }
        }
    }
}