pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'calpy'
        GITHUB_REPO_URL = 'https://github.com/deepanshpandey/SPE_MiniProject.git'
	OPTION = 1
	NUMBER = 2
	EXP = 3
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('Run Main Application') {
            steps {
                script {
                    sh "echo '${OPTION}\n${NUMBER}\n${EXP}' | python3 calculator.py"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 caltest.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                    sh 'docker tag calpy deepanshpandey/calpy:latest'
                    sh 'docker push deepanshpandey/calpy'
                    }
                }
            }
        }

    stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }

    }
}
