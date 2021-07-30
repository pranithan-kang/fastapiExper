
# Flatten the user_role list of dict to be set of string
def extract_user_roles(user_role):
  return { x["role"] for x in user_role }

def to_test_method():
  return 3