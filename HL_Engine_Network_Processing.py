"""HL_Engine_Network_Processing.py"""
import nmap
from HL_Engine_2.HL_CommonDependency import *


class NetworkProcessEngine:
    """Network Process Engine"""

    def scan_wifi(self, base_ip):
        """Scan wifi network"""
        try:
            print()
            display_message(WLAN_NETWORK_SCANNER)
            nm = nmap.PortScanner()
            count = 1
            while count < 10:
                ip = base_ip + str(count)
                print(ip + " Scanning ...")
                count = count + 1
                nm.scan(hosts=ip, arguments="-n -sP -PE -PA21,23,80,3389")
                hosts_list = [(x, nm[x]["status"]["state"]) for x in nm.all_hosts()]
                for host, status in hosts_list:
                    print(host, status)
                    if status == "up":
                        report = open(ACTIVE_DEVICES_LOG, "a")
                        report.writelines(host + "\n")
                        report.close()
        except:
            return(False)
