@Library('my-shared-lib') _

pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
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
                startMockServer()
            }
        }

        stage('Run API Tests') {
            steps {
                runApiTests(env: 'dev', parallel: true, withCoverage: true)
            }
        }
    }

    post {
        always {
            stopMockServer()

            archiveArtifacts artifacts: 'project/allure-results/**', allowEmptyArchive: true

            allure includeProperties: false, jdk: '',
                   results: [[path: 'project/allure-results']]

            step([
                $class: 'CoberturaPublisher',
                coberturaReportFile: 'project/coverage.xml',
                onlyStable: false,
                failUnhealthy: false,
                failUnstable: false,
                failNoReports: false
            ])

            sendNotification(currentBuild.currentResult)
        }
    }
}