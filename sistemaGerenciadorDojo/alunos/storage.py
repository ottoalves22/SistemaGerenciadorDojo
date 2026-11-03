
import os

import oci
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

@deconstructible
class OracleStorage(Storage):

    def __init__(self):
        self.bucket_name = "docs-ornellas"
        self.namespace = "grcdvqigfkdr"
        self.region = "sa-saopaulo-1"   
        self.auth_mode = os.environ.get("OCI_AUTH", "config_file")

        if self.auth_mode == "instance_principal":
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

            self.client = oci.object_storage.ObjectStorageClient(
                config={"region": self.region},
                signer=signer,
            )

        elif self.auth_mode == "config_file":
            config = oci.config.from_file(
                file_location=os.environ.get(
                    "OCI_CONFIG_FILE",
                    "~/.oci/config",
                ),
                profile_name=os.environ.get(
                    "OCI_CONFIG_PROFILE",
                    "DEFAULT",
                ),
            )

            self.client = oci.object_storage.ObjectStorageClient(config)

        else:
            raise ValueError(f"Unsupported OCI_AUTH: {self.auth_mode}")

    def _save(self, name, content):
        content.seek(0)

        self.client.put_object(
            namespace_name=self.namespace,
            bucket_name=self.bucket_name,
            object_name=name,
            put_object_body=content,
            content_length=content.size,
        )

        return name

    def exists(self, name):
        try:
            self.client.head_object(
                namespace_name=self.namespace,
                bucket_name=self.bucket_name,
                object_name=name,
            )
            return True

        except oci.exceptions.ServiceError as exc:
            if exc.status == 404:
                return False
            raise

    def _open(self, name, mode="rb"):
        raise NotImplementedError("File download is not implemented.")

