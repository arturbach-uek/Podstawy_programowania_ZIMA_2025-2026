required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}
print(required_permissions.issubset(user_permissions))
