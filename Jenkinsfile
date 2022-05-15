pipeline {
  agent any
  stages {

    stage('Fantastic ascii  - build'){
        when { branch "master" }
        steps {
            sh '''
            cp .pypirc ~
            cd package_demo
            pip3 install wheel
            pip3 install twine
            python3 setup.py sdist upload -r local
            python3 setup.py bdist_wheel upload -r local

            '''
        }
    }

  }
}


