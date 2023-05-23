import sys
from zapv2 import ZAPv2
from pathlib import Path

#sys.path.append("./")
from utils.log_utils import LogUtils

#java -jar zap-2.12.0.jar -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config api.disablekey=true
class ZapController:

    def __init__(self) -> None:
        self.apikey: str = "83g73a2fl9cmdthejlqe7gd9vu"
        self.zap: ZAPv2 = ZAPv2(apikey=self.apikey)

    def start_scan(self):
        script_file: str = "scripts/MyScript.js"
        script_file2: str = "scripts/MyScript2.js"
        script_file = str(Path().cwd()   / script_file)
        script_file2 = str(Path().cwd() / script_file2)
        self.zap.script.remove("MyScript.js")
        self.zap.script.load('MyScript.js',"httpsender","Oracle Nashorn",script_file,"test" )
        self.zap.script.enable("MyScript.js",self.apikey)
        self.zap.script.remove("MyScript2.js")
        self.zap.script.load('MyScript2.js',"authentication","Oracle Nashorn",script_file2,"test2" )
        #self.zap.script.enable("MyScript2.js",self.apikey)

def main():
    zap_controller = ZapController()
    zap_controller.start_scan()

if __name__ == "__main__":
    main()