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

// Variables
def blueOceanUrl
def slackMessage
def appName
def appImage
def appCommit
def appVersion
def appTag
def appImageTags = []


// Pipeline
pipeline {
    agent any
    
    stages {
/*
        stage('Checkout repository'){
            steps {
                checkout scm
            }
        }
*/
        stage('Configuration'){
            steps {
                script {
                    appName = "ping"
                    appCommit = resizeCommit(env.GIT_COMMIT)
                    
                    blueOceanUrl = generateBuildUrl(
                        env.HUDSON_URL,
                        env.JOB_NAME,
                        env.JOB_BASE_NAME,
                        env.BUILD_NUMBER,
                    )
                    
                    def possibleTag = checkTagExistence(env.GIT_BRANCH)
                    if(possibleTag) {
                        appVersion = possibleTag
                        appImageTags.add(possibleTag)
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
                    def testsFile = "/tmp/tests.xml"
                    appImage.inside {
                        sh "pip install -e .[dev]"
                        sh "pytest -s -p no:warnings /app/tests/ --junitxml=${testsFile}"
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
    }
    post {
        success {
            script {
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
