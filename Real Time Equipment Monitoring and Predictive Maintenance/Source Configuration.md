**Source Configuration**

- Create an Azure DB for postgresql
- Set the server parameters as below to enable CDC
     - wal_level to logical

        ![wal_level](images/wal_level.png)
     - max_replication_slot to a higher number 

         ![max_replication_slot](images/max_rep_slot.png)
    - maximum write ahead log senders and size to a greater value

        ![max_wal_senders](images/max_wal_senders.png)
    - set track commit timestamp to On

        ![track_commit_timestamp](images/track_commit_timestamp.png)
- Create publication and replication slot for the tables in the server

    SELECT * FROM pg_create_logical_replication_slot('my_replication_slot', 'pgoutput');

        ![replication_slot](images\replication_slot.png)
- Grant the user role with replication permission

    ALTER ROLE <user_name> WITH REPLICATION;

        ![role_replication](images\role_replication.png)
- To setup sample dataset,
    - run the  EquipmentSensorsDataGenerator.py
    - run the insert_transaction_data.py   
