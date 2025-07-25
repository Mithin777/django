pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-static-site'
        EC2_USER = 'ubuntu' // Change to 'ec2-user' if using Amazon Linux
        EC2_HOST = '172.31.10.90' // Your EC2 instance IP
        SSH_KEY = '~/.ssh/jdjango.pem' // ✅ Updated key name
        DOCKER_CONTAINER = 'static-site'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Mithin777/django.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Save & Transfer Docker Image to EC2') {
            steps {
                sh '''
                    docker save $DOCKER_IMAGE | gzip > image.tar.gz
                    scp -i $SSH_KEY -o StrictHostKeyChecking=no image.tar.gz $EC2_USER@$EC2_HOST:/home/$EC2_USER/
                '''
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                    ssh -i $SSH_KEY -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST << 'EOF'
                        cd /home/$EC2_USER
                        docker load < image.tar.gz
                        docker stop $DOCKER_CONTAINER || true
                        docker rm $DOCKER_CONTAINER || true
                        docker run -d --name $DOCKER_CONTAINER -p 80:80 $DOCKER_IMAGE
                    EOF
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed.'
        }
    }
}
