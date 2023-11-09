## About the connector
Rapid7 Velociraptor is a unique, advanced open-source endpoint monitoring, digital forensic and cyber response platform. It provides you with the ability to more effectively respond to a wide range of digital forensic and cyber incident response investigations and data breaches.
<p>This document provides information about the Rapid7 Velociraptor Connector, which facilitates automated interactions, with a Rapid7 Velociraptor server using FortiSOAR&trade; playbooks. Add the Rapid7 Velociraptor Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Rapid7 Velociraptor.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-rapid7-velociraptor</pre>

## Prerequisites to configuring the connector
- You must have the client API certificate issued by the Rapid7 Velociraptor CA to authenticate and establish a TLS connection with the API server. For more information check: https://docs.velociraptor.app/docs/server_automation/server_api/
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Rapid7 Velociraptor server.

## Minimum Permissions Required
- Required permissions for check health: MACHINE_STATE.

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Rapid7 Velociraptor</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Upload Client API Certificate</td><td>Provide the client API certificate issued by the Rapid7 Velociraptor CA to authenticate and establish a TLS connection with the API server. Required permissions for check health: MACHINE_STATE. For more information check: https://docs.velociraptor.app/docs/server_automation/server_api/
</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Clients List</td><td>Retrieves a list of clients from Rapid7 Velociraptor based on the input parameters you have specified. Required Permissions: READ_RESULTS</td><td>list_clients <br/>Investigation</td></tr>
<tr><td>Run Artifacts Collection</td><td>Launches an artifact collection against a client based on the client ID specified. If the client_id is “server” then the collection occurs on the server itself. In that case the caller needs the SERVER_ADMIN permission. Required Permissions: COLLECT_CLIENT, COLLECT_SERVER</td><td>run_artifacts_collection <br/>Investigation</td></tr>
<tr><td>Get Flow Results</td><td>Retrieves the results of a flow from Rapid7 Velociraptor based on the Flow ID and other input parameters you have specified. Required Permissions: READ_RESULTS</td><td>get_flow_results <br/>Investigation</td></tr>
<tr><td>Get Flows List</td><td>Retrieves a list of flows launched on each client from Rapid7 Velociraptor based on the input parameters you have specified. Required Permissions: READ_RESULTS</td><td>list_flows <br/>Investigation</td></tr>
<tr><td>Create Flow Download</td><td>Creates a download pack for the flow. This function initiates the download creation process for a flow. It is equivalent to the GUI functionality allowing to “Download Results” from the Flows Overview page. Required Permissions: PREPARE_RESULTS</td><td>create_flow_download <br/>Investigation</td></tr>
<tr><td>Dump Artifact Definitions</td><td>Dumps artifact definitions from the internal repository. Required Permissions: READ_RESULTS</td><td>dump_artifact_definitions <br/>Investigation</td></tr>
<tr><td>Create Hunt</td><td>Creates and launches a hunt to collect the specified artifacts. Required Permissions: ORG_ADMIN, START_HUNT</td><td>create_hunt <br/>Investigation</td></tr>
<tr><td>Get Hunts List</td><td>Retrieves a list of hunts from Rapid7 Velociraptor based on the input parameters you have specified. Required Permissions: READ_RESULTS</td><td>list_hunts <br/>Investigation</td></tr>
<tr><td>Get Hunt Results</td><td>Retrieves the results of a hunt from Rapid7 Velociraptor based on the Hunt ID and other input parameters you have specified. Required Permissions: READ_RESULTS</td><td>get_hunt_results <br/>Investigation</td></tr>
<tr><td>Create Hunt Download</td><td>Creates a download pack for a hunt. This function initiates the download creation process for a hunt. It is equivalent to the GUI functionality allowing to “Download Results” from the Hunts Overview page. Required Permissions: PREPARE_RESULTS</td><td>create_hunt_download <br/>Investigation</td></tr>
<tr><td>Run VQL Query</td><td>Runs a user-defined VQL query on Rapid7 Velociraptor. Make sure you have all the permissions required to run the query.</td><td>run_vql_query <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Clients List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search String</td><td>Specify the client search string to retrieve clients from Rapid7 Velociraptor. Can have the following prefixes: ’label:’, ‘host:’.
</td></tr><tr><td>Client ID</td><td>Specify the client ID to retrieve client from Rapid7 Velociraptor.
</td></tr><tr><td>Count</td><td>Specify the maximum number of results, per page, that this operation should return from Rapid7 Velociraptor. By default, this is set as 1000. 
</td></tr><tr><td>Offset</td><td>Specify the index of the first item to be returned by this operation from Rapid7 Velociraptor. By default, this is set as 0. 
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "client_id": "",
    "agent_information": {
        "version": "",
        "name": ""
    },
    "os_info": {
        "system": "",
        "release": "",
        "machine": "",
        "fqdn": "",
        "install_date": ""
    },
    "first_seen_at": "",
    "last_seen_at": "",
    "last_ip": "",
    "last_interrogate_flow_id": "",
    "labels": []
}</pre>
### operation: Run Artifacts Collection
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Client ID</td><td>Specify the client ID to schedule a collection on Rapid7 Velociraptor.
</td></tr><tr><td>Artifacts</td><td>Specify a comma-separated list of artifacts to collect from Rapid7 Velociraptor.
</td></tr><tr><td>Env</td><td>Specify parameters to apply to the artifact (an alternative to a full spec). (e.g., dict(Device ='C:', VSSAnalysis='Y', KapeTriage='Y'))
</td></tr><tr><td>Spec</td><td>Specify parameters to apply to the artifacts. (e.g., dict(`Windows.KapeFiles.Targets`=dict(Device ='C:', VSSAnalysis='Y', KapeTriage='Y')))
</td></tr><tr><td>Timeout</td><td>Specify query timeout. (default 10 min)
</td></tr><tr><td>Ops Per Sec</td><td>Specify query Ops Per Sec value.
</td></tr><tr><td>CPU Limit</td><td>Specify query CPU limit value.
</td></tr><tr><td>Iops Limit</td><td>Specify query Iops Limit value.
</td></tr><tr><td>Max Rows</td><td>Specify max number of rows to fetch.
</td></tr><tr><td>Max Bytes</td><td>Specify max number of bytes to upload.
</td></tr><tr><td>Urgent</td><td>Select the checkbox to set the collection as urgent. When this is set as true it skips other queues collections on the client.
</td></tr><tr><td>Org ID</td><td>Specify the org ID in which the collection will be started in Rapid7 Velociraptor.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Flow Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Flow ID</td><td>Specify the hunt ID to read from Rapid7 Velociraptor.
</td></tr><tr><td>Client ID</td><td>Specify the client ID to extract from Rapid7 Velociraptor.
</td></tr><tr><td>Artifact</td><td>Specify artifact to retrieve in this operation from Rapid7 Velociraptor.
</td></tr><tr><td>Source</td><td>Specify an optional source within the artifact.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Flows List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Client ID</td><td>Specify the client ID to retrieve flows from Rapid7 Velociraptor.
</td></tr><tr><td>Flow ID</td><td>Specify the flow ID to retrieve from Rapid7 Velociraptor.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Flow Download
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Client ID</td><td>Specify the client ID to export flow from Rapid7 Velociraptor.
</td></tr><tr><td>Flow ID</td><td>Specify the flow ID to export from Rapid7 Velociraptor.
</td></tr><tr><td>Wait</td><td>Select the checkbox to wait for the download to complete before returning.
</td></tr><tr><td>Password</td><td>Specify an optional password to encrypt the collection zip.
</td></tr><tr><td>Format</td><td>Specify the format to export (csv,json,csv_only) defaults to both.
</td></tr><tr><td>Name</td><td>Specify the name of the file. By default filename is generated based on flow id.
</td></tr><tr><td>Expand Sparse</td><td>Select the checkbox to expand sparse files in the archive.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Dump Artifact Definitions
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Artifact Name</td><td>Specify a comma-separated list of artifact definitions to dump
</td></tr><tr><td>Include Dependencies</td><td>Select the checkbox to include all dependencies as well.
</td></tr><tr><td>Sanitize</td><td>Select the checkbox to remove extra metadata.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Hunt
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Artifacts</td><td>Specify a comma-separated list of artifacts to collect from Rapid7 Velociraptor.
</td></tr><tr><td>Description</td><td>Specify a description of the hunt you want to create on Rapid7 Velociraptor.
</td></tr><tr><td>Expiry Time</td><td>Specify a time for expiry. If the expiry time is in the past, the hunt will not be created in the Rapid7 Velociraptor.
</td></tr><tr><td>Spec</td><td>Specify the parameters to apply to the artifacts. (e.g.: dict(`Windows.KapeFiles.Targets`=dict(Device ='C:', VSSAnalysis='Y', KapeTriage='Y')))
</td></tr><tr><td>Timeout</td><td>Specify query timeout. (default 10 min)
</td></tr><tr><td>Ops Per Sec</td><td>Specify query Ops Per Sec value.
</td></tr><tr><td>CPU Limit</td><td>Specify query CPU limit value.
</td></tr><tr><td>Iops Limit</td><td>Specify query Iops Limit value.
</td></tr><tr><td>Max Rows</td><td>Specify max number of rows to fetch.
</td></tr><tr><td>Max Bytes</td><td>Specify max number of bytes to upload.
</td></tr><tr><td>Pause</td><td>Select the checkbox to create the new hunt in the paused state.
</td></tr><tr><td>Include Labels</td><td>Specify comma-separated list of labels to only include those in the response.
</td></tr><tr><td>Exclude Labels</td><td>Specify comma-separated list of labels to exclude those in the response.
</td></tr><tr><td>OS</td><td>Specify to target this OS.
</td></tr><tr><td>Org ID</td><td>Specify the org ID in which the collection will be started in the Rapid7 Velociraptor.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Hunts List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Hunt ID</td><td>Specify the hunt ID to read from Rapid7 Velociraptor.
</td></tr><tr><td>Count</td><td>Specify the maximum number of results, per page, that this operation should return from Rapid7 Velociraptor.
</td></tr><tr><td>Offset</td><td>Specify the index of the first item to be returned by this operation from Rapid7 Velociraptor.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Hunt Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Hunt ID</td><td>Specify the hunt ID to read from Rapid7 Velociraptor.
</td></tr><tr><td>Artifact</td><td>Specify the artifact to retrieve from Rapid7 Velociraptor.
</td></tr><tr><td>Source</td><td>Specify an optional source within the artifact.
</td></tr><tr><td>Brief</td><td>Select the checkbox to return less columns from Rapid7 Velociraptor.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Hunt Download
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Hunt ID</td><td>Specify the hunt ID to export from Rapid7 Velociraptor.
</td></tr><tr><td>Only Combined</td><td>Select the checkbox to only export combined results from Rapid7 Velociraptor.
</td></tr><tr><td>Wait</td><td>Select the checkbox to wait for the download to complete before returning.
</td></tr><tr><td>Format</td><td>Specify the format to export (csv,json) defaults to both.
</td></tr><tr><td>Base</td><td>Specify the base filename to write to.
</td></tr><tr><td>Password</td><td>Specify an optional password to encrypt the collection zip.
</td></tr><tr><td>Expand Sparse</td><td>Select the checkbox to expand sparse files in the archive.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Run VQL Query
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>VQL Query</td><td>Specify the VQL query to run on Rapid7 Velociraptor. For more information check: https://docs.velociraptor.app/vql_reference/
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - rapid7-velociraptor - 1.0.0` playbook collection comes bundled with the Rapid7 Velociraptor connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Rapid7 Velociraptor connector.

- Create Flow Download
- Create Hunt
- Create Hunt Download
- Dump Artifact Definitions
- Get Clients List
- Get Flow Results
- Get Flows List
- Get Hunt Results
- Get Hunts List
- Run Artifacts Collection
- Run VQL Query

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
