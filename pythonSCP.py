__build__ = 1.0
from os import system as __system__
def download(User, IP_or_Domain, Password, Path_to_File, Path_to_save_file): __system__(f"sshpass -p '{Password}' scp {User}@{IP_or_Domain}:{Path_to_File} {Path_to_save_file}")
def upload(User, IP_or_Domain, Password, Path_to_file, Path_to_upload): __system__(f"sshpass -p '{Password}' scp {Path_to_file} {User}@{IP_or_Domain}:{Path_to_upload}")
