from fastapi import Header

def get_current_roles(roles:str = Header(...)):
    return set(roles.split(","))