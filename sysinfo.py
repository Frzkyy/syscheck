import platform
import getpass

def get_info():
     print(f"""========== System Info ==========
OS: {platform.system()}
Kernel: {platform.release()}
Architecture: {platform.machine()}
Processor: {platform.processor()}
Hostname: {getpass.getuser()}
Device Name: {platform.node()}

=================================""")