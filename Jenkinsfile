pipeline {
  agent any
  parameters {
    string(name: 'userName',defaultValue: 'Anthony', description: 'please give a name')
    choice(name: 'version',choices: ['1.1','1.2','1.3'], description: 'select the version to test')
    booleanParam(name: 'is_boy',defaultValue: true, description: 'you is boy or not')
  }
  stages {
    stage('build') {
      steps {
        sh 'echo "Hello World"'
        sh '''
          echo "Multiline shell steps works too"
          ls -lah
        '''
      }
    }
    stage('test'){
      steps{
        script {
          sh "java -version"
        }
      }
    }
  }
}

