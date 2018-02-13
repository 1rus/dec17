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
    		sh '''. /tmp/venv/bin/activate && pytest --pyargs /frame-test/test_assertions.py --junitxml=results.xml'''
		sh 'ls -la'
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}
