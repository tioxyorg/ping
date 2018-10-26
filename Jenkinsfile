node('master'){
  
  def tags = ['1', '2', '3']
  
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
}
