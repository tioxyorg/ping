node('master'){
  
  def tags = ['1', '2', '3']
  parameters: [
    choice(name: 'DESIRED_TAG', choices: ${tags}, description: 'Desired tag?')
  ]
  
  stage('Echo'){
    println(env.DESIRED_TAG)
  }
}
