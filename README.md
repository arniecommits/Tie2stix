# Tie2stix
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
**Allow conversion of McAfee Threat Intelligence Exchange File Reputation hashes as STIX XML File for Ingestion into SIEM/TIP**

**Install Instructions**

**Step 1**
Import the ePO query Import file in your ePO Under Queries and Report, hit edit and note the query id from the edit url or optionally you can run the web api query as described here https://docs.mcafee.com/bundle/epolicy-orchestrator-5.10.0-product-guide/page/GUID-86796CE0-477D-43EB-A9CF-6980401E0947.html

![Import Import ePO Query.xml](https://user-images.githubusercontent.com/60926235/82129308-91dac900-97b9-11ea-83eb-4955227bf96b.PNG)
Run the TIE Reputation Export Query , just to make sure your TIE DB Connectivity is OK

**Step 2**
Install Python Libraries 

    pip install -r requirements.txt

**Step 3**
Edit the variables in the script 

    epo_ip='epo IP' 
    query_id='id of imported query'
    user_pass='admin:<yourpass>' 
    stixfilename='STIXoutput.xml'
    

**Step 4**
Run the Python Script...happy STIXXING

    python tie2stix.py



