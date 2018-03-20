node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
        pythonImage = docker.build('dec17:test')
    }
    stage('test'){
        pythonImage.inside {
		sh 'ls -la'
    		sh '''python3 -m pytest frame-test/test_assertions.py --junitxml=results.xml'''
		sh 'ls -la'
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}
