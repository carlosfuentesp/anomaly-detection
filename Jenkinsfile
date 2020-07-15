pipeline {
    agent any
    triggers {
        // Poll SCM every minute for new changes
        pollSCM('* * * * *')
    }
    options {
       // add timestamps to output
       timestamps()
    }
    stages {
        stage('Install dependencies') {
            steps {
                echo 'Starting Build'
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Run tests') {
            steps {
                sh "bash ./run_tests.sh"
            }
        }
        stage('Run ML pipeline') {
            steps {
                sh "python3 /source/main.py"
            }
        }
/*         stage('Acceptance test') {
            steps {
                sh 'python3 run_python_script.py acceptance'
            }
        } */
    }
}
