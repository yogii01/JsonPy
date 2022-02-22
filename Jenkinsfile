pipeline {
    agent any
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
                              "pattern": "G:\\py\\*.zip",
                              "target": "Demo_file"
                            }
                         ]      
                    }'''
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

        
