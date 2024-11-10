**Event Stream Configuration**

- Create an eventstream in the workspace.
- Choose the Azure DB for posgresql in the external sources option. 
        (Azure DB for postgresql will appear in the place of loading)
    ![choose_source](images\choose_source.png)
- Configure the source connection details

    ![source_server](images\source_server.png)

- Once the configuration is set correctly, the test preview in the source will display the schema and payload containing the source data

    ![source_preview](images\source_preview.png)

- The postgresql server can also be queried to know the details of the event stream like ip address, status of the streaming ,etc

    ![replication_state](images\replication_state.png)

- Manage field transformation can be used to rename the columns, change the datatypes, fetch the transaction timestamp, CRUD operation types, etc.

    ![manage_field](images\manage_field.png)

- configure the destination as Eventhouse and create a KQL database and table newly

    ![kql_destination](images\kql_destination.png)