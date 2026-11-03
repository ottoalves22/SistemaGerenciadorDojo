
import os
from urllib.parse import quote

import oci
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class OracleStorage(Storage):

    def __init__(self):
        self.bucket_name = os.environ.get(
            "OCI_BUCKET_NAME",
            os.environ.get("ORACLE_BUCKET_NAME", "docs-ornellas"),
        )
        self.namespace = os.environ.get(
            "OCI_NAMESPACE",
            os.environ.get("ORACLE_NAMESPACE", ""),
        )
        self.region = os.environ.get(
            "OCI_REGION",
            os.environ.get("ORACLE_REGION", "sa-saopaulo-1"),
        )
        self.auth_mode = os.environ.get("OCI_AUTH", "config_file")
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._build_client()
        return self._client

    def _build_client(self):
        if self.auth_mode == "instance_principal":
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            return oci.object_storage.ObjectStorageClient(
                config={"region": self.region},
                signer=signer,
            )

        if self.auth_mode == "config_file":
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
            return oci.object_storage.ObjectStorageClient(config)

        raise ValueError(f"Unsupported OCI_AUTH: {self.auth_mode}")

    def _save(self, name, content):
        if hasattr(content, "seek"):
            content.seek(0)

        put_kwargs = {
            "namespace_name": self.namespace,
            "bucket_name": self.bucket_name,
            "object_name": name,
            "put_object_body": content,
        }
        content_length = getattr(content, "size", None)
        if content_length is not None:
            put_kwargs["content_length"] = content_length

        self.client.put_object(**put_kwargs)
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

    def url(self, name):
        object_name = quote(name, safe="/")
        return (
            f"https://objectstorage.{self.region}.oraclecloud.com/"
            f"n/{self.namespace}/b/{self.bucket_name}/o/{object_name}"
        )

    def _open(self, name, mode="rb"):
        raise NotImplementedError("File download is not implemented.")
