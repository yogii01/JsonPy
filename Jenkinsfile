pipeline {
    agent any
        tools {
            maven "3.8.4"
                }
        stages {
            stage('Git Checkout'){
                steps {
                    git branch: 'main', credentialsId: 'JsonPy', url: 'https://github.com/yogii01/JsonPy.git'
                }
            }
        stage ('Python') {
            steps {
                bat 'Demo.py'
            }
        }

        stage ('Server'){
            steps {
                rtServer (
                    id: "Artifactory",
                    url: 'http://127.0.0.1:8082/artifactory',
                    username: 'admin',
                    password: 'Yogesh@123',
                    bypassProxy: true,
                    timeout: 300
                        )

            }
        }
        stage ('Upload'){
            steps{
                rtUplode (
                 serverId:"Artifactory",
                  spec: '''{
                   "files": [
                      {
                      "pattern": ".war",
                      "target": "logic-ops-lab-libs-snapshot-local"
                      }
                            ]
                           }''',
                        )
            }
        }
        stage ('Publish build info') {
            steps {
                rtPublishBuildInfo (
                    serverId: "Artifactory"
                )
            }
        }
    }
}       
