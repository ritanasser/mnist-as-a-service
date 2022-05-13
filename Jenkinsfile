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
    stage ('fanstic ascii -connect'){
        when {branch "master"}
        step{
        sh '''
        [distutils]
        index-servers = local
        [local]
        repository: https://ritan710.jfrog.io/artifactory/api/pypi/finalproject-pypi-local
        username: ritanas00@gmail.com
        password: AKCp8mYUvBJwzxKZHMfPMW1hQqViZtnFbs6xXPZHYkZEDA8KcefKRKfeAQEyh3dPCHmYXk2iM
        '''
        }}

    stage('Fantastic ascii  - build'){
        when { branch "master" }
        steps {
            sh '''
            cd package_demo
            python setup.py wheel
            python setup.py twine
            python setup.py sdist upload -r local
            python setup.py bdist_wheel upload -r local

            '''
        }
    }

  }
}


