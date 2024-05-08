pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/FVer12/CI-CDAPI.git'
            } 
        }
        stage('Build') {
            steps {
                sh 'docker build -f Dockerfile -t uvera12/api-image:sha256-1 .'
            }
        }
        stage('Push') {
            steps {
                echo 'El construyo la imagen perfectamente'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'El pipeline se ejecutó correctamente'
        }
        failure {
            echo 'El pipeline falló. Revisar los logs para más detalles.'
        }
    }
}
