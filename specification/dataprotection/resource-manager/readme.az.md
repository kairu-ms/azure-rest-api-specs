## AZ

These settings apply only when `--az` is specified on the command line.

``` yaml $(az)
az:
  extensions: dataprotection
  namespace: azure.mgmt.dataprotection
  package-name: azure-mgmt-dataprotection
az-output-folder: $(azure-cli-extension-folder)/src/dataprotection
python-sdk-output-folder: "$(az-output-folder)/azext_dataprotection/vendored_sdks/dataprotection"
randomize-names: true
directive:
  - where:
      command: dataprotection backup-instance trigger-restore
    set:
      command: dataprotection backup-instance restore trigger
  - where:
      command: dataprotection backup-vault show-in-resource-group
    set:
      command: dataprotection backup-vault list-in-resource-group
  - where:
      command: dataprotection backup-vault show-in-subscription
    set:
      command: dataprotection backup-vault list-in-subscription

cli:
  cli-directive:
    - where:
       group: OperationResult
       op: Get
      hidden: true
    - where:
       group: DataProtection
      hidden: true
    - where:
       group: DataProtectionOperations
      hidden: true
    - where:
       group: OperationStatus
      hidden: true
    - where:
       group: ExportJobs
      hidden: true
    - where:
       group: ExportJobsOperationResult
      hidden: true
    - where:
       group: BackupVaultOperationResults
      hidden: true
    - where:
       group: BackupInstances
       op: CreateOrUpdate#update
      hidden: true
    - where:
       group: BackupInstances
       op: TriggerRehydrate
      hidden: true
    - where:
       group: BackupPolicies
       op: CreateOrUpdate#update
      hidden: true
    - where:
       group: BackupVaults
       op: GetInSubscription
      hidden: true
    - where:
       group: BackupVaults
       op: GetInResourceGroup
      hidden: true
```
