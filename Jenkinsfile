pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo '从 GitHub 拉取代码'
                sh '''
                    rm -rf project
                    git clone https://github.com/L-royse/shoppingweb-test.git project
                    cd project
                    ls -la
                '''
            }
        }

        stage('Start Mock Server') {
            steps {
                sh '''
                    cd project
                    nohup python3 mock_server.py > mock.log 2>&1 &
                    echo $! > mock.pid
                    sleep 3
                    cat mock.log
                    curl -s http://127.0.0.1:5000/posts | head -c 200
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    cd project
                    pytest tests_api/ -v --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            sh '''
                if [ -f project/mock.pid ]; then
                    kill $(cat project/mock.pid) || true
                    rm -f project/mock.pid
                fi
            '''
            archiveArtifacts artifacts: 'project/allure-results/**', allowEmptyArchive: true
        }
    }
}