import oci

config = oci.config.from_file(
    "/root/.oci/config",
    "DEFAULT"
)

oci.config.validate_config(config)

identity = oci.identity.IdentityClient(config)

user = identity.get_user(config["user"]).data

print("Autenticação OK!")
print(f"Usuário: {user.name}")
print(f"Estado: {user.lifecycle_state}")