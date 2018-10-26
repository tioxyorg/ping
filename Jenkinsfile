node('master'){
  def tags = "RELOAD\n"
  tags += sh(script: "git tag", returnStdout: true).trim()
  properties(
    [
        parameters(
            [
                choice(
                  choices: tags,
                  description: 'Escolha Tag',
                  name: 'DESIRED_TAG'
                )
            ]
        )
    ]
  )

  if (!env.DESIRED_TAG.contains("RELOAD")){
      stage('Echo'){
        println(env.DESIRED_TAG)
      }
    
      stage('Checkout'){
        checkout scm
      }
  }
}
