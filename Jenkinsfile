pipeline {
  agent any

  environment {
    REGISTRY_URL = '352708296901.dkr.ecr.us-east-1.amazonaws.com'
    ECR_REGION = 'us-east-1'
    K8S_NAMESPACE = 'rita-namespace'
    K8S_CLUSTER_NAME = 'devops-alfnar-k8s'
    K8S_CLUSTER_REGION = 'eu-north-1'


  }
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


