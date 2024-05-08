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
                script {
                    try {
                        docker.withTool('docker') {
                            sh 'docker build -f API3/Dockerfile -t uvera12/api-image:vsha256-1 .'
                        }
                    } catch (err) {
                        currentBuild.result = 'FAILURE'
                        error "Error al construir la imagen Docker: ${err}"
                    }
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    try {
                        docker.withRegistry('https://registry.example.com', 'dockerCredentials') {
                            sh 'docker push uvera12/api-image:vsha256-1'
                        }
                    } catch (err) {
                        currentBuild.result = 'FAILURE'
                        error "Error al empujar la imagen Docker: ${err}"
                    }
                }
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
