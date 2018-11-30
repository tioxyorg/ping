// Functions
def generateSlackMessage(EMOJI, STATUS, APP_NAME, IMAGE_VERSION, BLUE_OCEAN_BUILD) {
    return """
    ${EMOJI} *${STATUS}*: APP > `${APP_NAME}`

    IMAGE: `${IMAGE_VERSION}`
    PIPELINE: ${BLUE_OCEAN_BUILD}
    """
}

def generateBuildUrl(HUDSON_URL, JOB_NAME, JOB_BASE_NAME, BUILD_NUMBER) {
    JOB_NAME = JOB_NAME.minus("/${JOB_BASE_NAME}")
    return "${HUDSON_URL}blue/organizations/jenkins/${JOB_NAME}/detail/${JOB_BASE_NAME}/${BUILD_NUMBER}/pipeline"
}

def resizeCommit(commit, desiredLength = 7) {
    return commit.take(desiredLength)
}

def checkTagExistence(branch) {
    def tag
    def semVerRegex = "^v\\d+\\.\\d+\\.\\d+"

    if (branch ==~ semVerRegex) {
        tag = branch
    }
    else {
        tag = ""
    }
    return tag
}

def pushImage(repository, credentialId, image, imageTags) {
    docker.withRegistry(repository, credentialId) {
        for(tag in imageTags){
            image.push(tag)
        }
    }
}

def generatePropertiesFile(fileName, fileContent, indentation) {
    def serializedContent = readJSON(
        text: groovy.json.JsonOutput.toJson(fileContent)
    )
    writeJSON(
        file: fileName,
        json: serializedContent,
        pretty: indentation,
    )
}


// Variables
def blueOceanUrl
def slackMessage
def appName = "ping"
def appImage
def appCommit
def appVersion
def appTag
def appImageTags = []
def propertiesFile = "buildProperties.json"
def propertiesContent = [:]

// Pipeline
pipeline {
    agent any
    
    stages {
        stage('Configuration'){
            steps {
                script {
                    appCommit = resizeCommit(env.GIT_COMMIT)
                    
                    blueOceanUrl = generateBuildUrl(
                        env.HUDSON_URL,
                        env.JOB_NAME,
                        env.JOB_BASE_NAME,
                        env.BUILD_NUMBER,
                    )
                    
                    appTag = checkTagExistence(env.GIT_BRANCH)
                    if(appTag) {
                        appVersion = appTag
                        appImageTags.add(appTag)
                        appImageTags.add("latest")
                    }
                    else {
                        appVersion = appCommit
                    }
                    
                    appImageTags.add(appCommit)
                }
            }
        }
        stage('Build'){
            steps {
                script {
                    appImage = docker.build("tioxyorg/${appName}:${appCommit}")
                }
            }
        }
        stage('Test'){
            steps {
                script {
                    def testsFile = "test-${appVersion}.xml"
                    appImage.inside {
                        sh "pip install -e .[dev]"
                        sh "pytest -s -p no:warnings tests/ --junitxml=${testsFile}"
                        junit(
                            testResults: testsFile,
                        )
                    }
                }
            }
        }
        stage('Push Image'){
            steps {
                script {
                    pushImage(
                        "https://index.docker.io/v1/",
                        "dockerhub-credentials",
                        appImage,
                        appImageTags,
                    )
                }
            }
        }
        stage('Create properties file'){
            steps {
                script {
                    propertiesContent = [
                        "app": [
                            "version": appVersion,
                            "image": "tioxyorg/${appName}:${appVersion}",  
                        ],
                        "jenkins": [
                            "buildNumber": env.BUILD_NUMBER,
                            "jobBaseName": env.JOB_BASE_NAME,
                            "jobName": env.JOB_NAME,
                        ],
                    ]

                    def desiredIndentation = 4
                    generatePropertiesFile(
                        propertiesFile,
                        propertiesContent,
                        desiredIndentation,
                    )
                }
            }
        }
    }
    post {
        success {
            script {
                archiveArtifacts(
                    artifacts: propertiesFile,
                    onlyIfSuccessful: true,
                )
                slackMessage = generateSlackMessage(
                    ":heavy_check_mark:",
                    "SUCCESS",
                    appName,
                    appVersion,
                    blueOceanUrl,
                )
                slackSend(
                    message: slackMessage,
                    color: "#76FF03",
                )
            }
        }
        unstable {
            script {
                slackMessage = generateSlackMessage(
                    ":warning:",
                    "UNSTABLE",
                    appName,
                    appVersion,
                    blueOceanUrl,
                )
                slackSend(
                    message: slackMessage,
                    color: "#FFFF00",
                )
            }
        }
        failure {
            script{
                slackMessage = generateSlackMessage(
                    ":x:",
                    "FAILURE",
                    appName,
                    appVersion,
                    blueOceanUrl,
                )
                slackSend(
                    message: slackMessage,
                    color: "#D50000",
                )
            }
        }
    }
}
