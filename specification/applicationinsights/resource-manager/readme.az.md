## AZ

These settings apply only when `--az` is specified on the command line.

``` yaml $(az)
az:
    extensions: app-insights
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
            op: "*"
          hidden: true
        - where:
            group: ExportConfigurations
          set:
            group: continuous-export
          hidden: false
```