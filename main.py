# File: CustomTokenCredential.py

from azure.core.credentials import TokenCredential, AccessToken
import time
import subprocess

class CustomTokenCredential(TokenCredential):
    def get_token(self, *scopes, **kwargs):
        # Set the expiration time appropriately. Adjust as needed.
        expires_on = int(time.time()) + 60
        return AccessToken(self.refreshed_token, expires_on)
    
    @property
    def refreshed_token(self):
        command = "some command to get token"
        result = subprocess.check_output(command, shell=True)
        return result.decode().strip()
