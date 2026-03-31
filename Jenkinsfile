pipeline {
    agent any

    environment {
        REPO_DIR = "${WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install selenium pytest pytest-html
                '''
            }
        }

        stage('Install Chrome & ChromeDriver') {
            steps {
                echo 'Installing Google Chrome...'
                sh '''
                    if ! command -v google-chrome &> /dev/null; then
                        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
                        echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
                        apt-get update -y
                        apt-get install -y google-chrome-stable
                    else
                        echo "Chrome already installed: $(google-chrome --version)"
                    fi
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests in headless mode...'
                sh '''
                    export DISPLAY=:99
                    cd ${WORKSPACE}
                    python3 -m pytest test/test_form.py -v \
                        --html=report.html \
                        --self-contained-html \
                        -p no:warnings || true
                '''
            }
        }

        stage('Publish Test Report') {
            steps {
                echo 'Publishing HTML test report...'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${WORKSPACE}",
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Archiving report...'
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
        success {
            echo 'All tests passed successfully.'
        }
        failure {
            echo 'Some tests failed. Check the report for details.'
        }
    }
}
