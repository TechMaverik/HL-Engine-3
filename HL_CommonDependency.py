"""
HL_Message_Bank.py
Author:Akhil P Jacob
HLDynamic-Integrations
"""
ENCRYPTION_PATH = "HL_Crypto/key.txt"
PAYLOAD_XML_PATH = "payload_setup.xml"
PAYLOAD = "payload"
LOG_REPORT = "error_report.txt"
INSTALLATION_FAILED = "HLEngine: Installation failed...."
COMMENCING_INSTALLATION = "HLEngine : Commencing installation......"
COULD_NOT_UNDERSTAND = "HLEngine:Google Speech Recognition could not understand audio"
COULD_NOT_CREATE_REQUEST = "HLEngine:Could not request results from Google Speech Recognition service; {0}"
SAY_SOMETHING = "Say something!"
RATE_OF_SPEECH = 125
BAUD_RATE = 9600
WELCOME_MSG = "\n\n[        HL_ENGINE 2.0 SETUP         ] \n "
INSTALLATION_COMPLETED = "\n\n[        HL_ENGINE 2.0 INSTALLATION COMPLETED         ] \n "
WLAN_NETWORK_SCANNER = "WLAN_Network_Scanner"
ACTIVE_DEVICES_LOG = "active_devices.txt"


def display_message(MSG):
    """Display message"""
    print(MSG)
