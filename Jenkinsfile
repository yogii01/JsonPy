pipeline {
    agent any
        tools {
            maven "3.8.4"
                }
        stages {
            
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
                rtUpload (
                    serverId: 'Artifactory',
                    spec: '''{
                          "files": [
                            {
                              "pattern": ".zip",
                              "target": "logic-ops-lab-libs-snapshot-local"
                            }
                         ]      
                    }''',
                    buildName: 'holyFrog',
                    buildNumber: '42',
                    project: 'my-project-key'
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

        
