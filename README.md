# streamlit_chat

Lightweight Streamlit Chat with data app to connect to api

## To deploy

Create a resource group for the app to land in.

Login to the Azure cli with:

```console
az login
```

```console
az group create --n rg-streamlittest --location uksouth
```



Deploy with:

```console
az deployment group create --resource-group rg-streamlittest --parameter infra/test.bicepparam 
```

To preview changes

```console
az deployment group what-if 
```


### Connect to prompftflow

1. Create a promptflow
2. Deploy managed endpoint
3. Add XXXXX to .env