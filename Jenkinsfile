node('master'){

  tags = sh(script: "git tag", returnStdout: true).trim()
  properties(
    [
        parameters(
            [
                choice(choices: tags, description: 'Escolha Tag',name: 'DESIRED_TAG')
            ]
        )
    ]
)
  
  stage('Echo'){
    println(env.DESIRED_TAG)
  }
  
  stage('Checkout'){
    checkout scm
  }
}
