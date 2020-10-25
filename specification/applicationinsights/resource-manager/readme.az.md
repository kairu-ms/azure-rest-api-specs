## AZ
 
These settings apply only when `--az` is specified on the command line.
 
``` yaml $(az)
az:
    extensions: applicationinsights
    namespace: azure.mgmt.applicationinsights
    package-name: azure-mgmt-applicationinsights
az-output-folder: $(azure-cli-extension-folder)/src/application-insights
python-sdk-output-folder: "$(az-output-folder)/azext_applicationinsights/vendored_sdks/applicationinsights"
# add additinal configuration here specific for Azure CLI
# refer to the faq.md for more details
cli:
    cli-directive:
        - where:
            group: "*"
          hidden: true
        - where:
            group: ExportConfigurations
          name: continues_export
          hidden: false
```