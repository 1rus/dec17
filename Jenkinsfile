node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
        pythonImage = docker.build('dec17:build')
    }
    stage('test'){
        pythonImage.inside {
   		sh '''. /tmp/venv/bin/activate && python - m pytest /frame-test/test_assertions.py --junitxml=results.xml'''
		sh 'ls -la'
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}
