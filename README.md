# Tie2stix
Allow conversion from McAfee Threat Intelligence Exchange File hashes as STIX XML File for Ingestion into SIEM/TIP

Install Instructions

Step 1
Import the ePO query Import file in your ePO Under Queries and Report, hit edit and note the query id from the edit url or optionally you can run the web api query as described here https://docs.mcafee.com/bundle/epolicy-orchestrator-5.10.0-product-guide/page/GUID-86796CE0-477D-43EB-A9CF-6980401E0947.html

Step 2
Install Python Libraries pip install -r requirements.txt

Step 3
Edit the variables in the script epo_ip='172.16.1.4' query_id='983' user_pass='admin:' stixfilename='tiestix.xml'

Step 4
Run the Python Script...happy STIXXING


