###### Query McAfee ePO TIE Database via ePO queries and Output to STIX ###########################
###### Author: Arnab Roy , Email: arnab_roy@mcafee.com ############################################

import pycurl
import pprint
from io import BytesIO
from xml.etree import ElementTree
import warnings
warnings.filterwarnings("ignore")
####STIX Libs####
from cybox.objects.file_object import File
import stix.utils as utils
from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator
####################################################################################################################################

epo_ip='172.16.1.4'
query_id='983'
user_pass='admin:<yourpass>'
stixfilename='tiestix.xml'

###################################################################################################################################
## Do not change bellow this ######################################################################################################
dataquery='https://'+epo_ip+':8443/remote/core.executeQuery?queryId='+query_id+'&:output=xml'
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, dataquery)
c.setopt(c.HTTPHEADER, ['Accept: application/xml'])
c.setopt(c.VERBOSE, 0)
c.setopt(pycurl.SSL_VERIFYPEER, 0)   
c.setopt(pycurl.SSL_VERIFYHOST, 0)
c.setopt(c.USERPWD, user_pass)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
response = buffer.getvalue().decode("utf-8")
response = response.strip('OK:')
response = response.strip('\r\n')
stxf = File()
stix_package = STIXPackage()
stix_header = STIXHeader()
stix_header.description = "Malicious File Hash Indicator"
stix_package.stix_header = stix_header
indicator = Indicator()
indicator.title = "File Observable"
indicator.description = (
        "An indicator containing a File observable with an associated hash"
)

root = ElementTree.fromstring(response)
for child in root:
    for child2 in child:
        for child3 in child2:
            for filenames in child3.iter('fileJoined.filename'):
                indicator.add_short_description(filenames.text)
            for hashes in child3.iter('fileJoined.md5'):
                stxf.add_hash(hashes.text)    

indicator.set_producer_identity("McAfee LLC.")
indicator.set_produced_time(utils.dates.now())
indicator.add_object(stxf)
stix_package.add(indicator)
stxout = open(stixfilename, "wb")
stxout.write(stix_package.to_xml())
stxout.close()
                