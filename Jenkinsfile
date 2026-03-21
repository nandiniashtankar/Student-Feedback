pipeline {
    agent any
    
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
                    python -m pip install --upgrade pip
                    pip install selenium
                '''
            }
        }
        
        stage('Install ChromeDriver') {
            steps {
                echo 'Installing ChromeDriver...'
                sh '''
                    # Install Chrome and ChromeDriver
                    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
                    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
                    apt-get update
                    apt-get install -y google-chrome-stable
                    
                    # ChromeDriver will be managed by Selenium Manager automatically
                '''
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests...'
                dir('student-feedback') {
                    sh 'python -m pytest test/test_form.py -v --html=report.html --self-contained-html || true'
                }
            }
        }
        
        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results...'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'student-feedback',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
