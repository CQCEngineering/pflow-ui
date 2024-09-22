param location string

param suffix string

 @description('Branch of the repository for deployment.')
 param repositoryBranch string = 'main'

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: 'streamlit-app-service-plan'
  location: location
  properties: {
    reserved: true
  }
  sku: {
    name: 'B1'
  }
  kind: 'app,linux'
}

resource appService 'Microsoft.Web/sites@2020-06-01' = {
  name: 'streamlit-chat-app-${suffix}'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'WEBSITES_PORT'
          value: '8501'
        }
        {
          name: 'TEXT_TO_REPLACE_TITLE'
          value: 'text to replace title'
        }
        {
          name: 'PROMPT_FLOW_ENDPOINT'
          value: 'endpoint'
        }
        {
          name: 'SCM_DO_BUILD_DURING_DEPLOYMENT' // Build the application during deployment
          value: 'true'
        }
        {
          name: 'WEBSITE_NODE_DEFAULT_VERSION' // Set the default node version
          value: '~20'
        }
      ]
      linuxFxVersion: 'PYTHON|3.12'
    }
  }
}

resource srcControls 'Microsoft.Web/sites/sourcecontrols@2021-01-01' = {
  parent: appService
  name: 'web'
  properties: {
    repoUrl: 'https://github.com/FarzamMohammadi/hello-world'
    branch: repositoryBranch
    isManualIntegration: true
  }
}

output appServiceName string = appService.name
