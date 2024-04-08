import os

def get_ssh_details():
    return {
        'hostname': os.getenv("VM_HOST"),
        'username': os.getenv("VM_USERNAME"),
        'password': os.getenv("VM_PASSWORD")
    }