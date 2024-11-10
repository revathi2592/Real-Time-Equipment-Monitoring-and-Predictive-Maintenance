**Real Time Equipment Monitoring and Predictive Maintenance**

Welcome to the Real-Time Equipment Monitoring and Predictive Maintenance project, created by Revathi Mani as an individual participant. This project demonstrates a robust solution for monitoring equipment health and anticipating maintenance needs using the advanced capabilities of Microsoft Fabric.

The solution is designed to handle real-time streaming data, leveraging Change Data Capture (CDC) from Azure Database for PostgreSQL as the source of live equipment data. This streaming data flows into an EventStream within Microsoft Fabric, where it’s directed to a KQL database hosted on Event House. OneLake availability is then enabled, creating a Lakehouse shortcut to this dataset and establishing the Bronze layer in a medallion architecture.

The Bronze layer serves as a raw data repository, ready for transformation and refinement. Data is subsequently processed into the Silver layer, where a PySpark notebook cleanses and renames columns for a structured dataset. This Silver table is then utilized to create snapshot tables at hourly, daily, and monthly intervals, enabling different levels of data aggregation.

Finally, the Bronze layer and aggregated tables power detailed reporting that provides a device status summary, trends in status changes, and monitors key metrics like vibration levels and temperature. This real-time insight helps identify potential issues, predict equipment faults, and proactively plan maintenance.

**Prerequisites**

To setup project you need
- Azure subscription
- Fabric Account
- Visual Studio Code (optional) to generate and insert streaming data in Azure DB for postgresql

**Source Configuration**

[How to configure source to enable CDC](Source%20Configuration.md)


**Event Stream Configuration**

[How to setup event stream in microsoft fabric](Event%20Stream%20Configuration.md)

**Event House Configuration**

[How KQL table gets created](Event%20House%20Configuration.md)

**Lake House Configuration**

[How to create lakehouse shortcut](Lake%20House%20Configuration.md)

**Notebooks to Create Silver and Gold Layers**

[Gold Layer via Pyspark Notebooks](Notebooks%20to%20Create%20Silver%20and%20Gold%20Layers.md)

**Reporting**

[What to visualize](Reporting.md)

Thank you for taking the time to review this project! I hope the demo on Real-Time Equipment Monitoring and Predictive Maintenance using Microsoft Fabric was insightful. If you have any questions, feedback, or suggestions, feel free to reach out at revathi2592@gmail.com.

Happy learning and coding! 

