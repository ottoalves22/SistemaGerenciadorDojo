import os

import boto3
from botocore.config import Config
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


OCI_ACCESS_KEY_ID = os.getenv("OCI_ACCESS_KEY_ID")
OCI_SECRET_ACCESS_KEY = os.getenv("OCI_SECRET_KEY")
OCI_BUCKET_NAME = "ornellas-dojo-docs"
OCI_REGION = "sa-saopaulo-1"
OCI_NAMESPACE = "grcdvqigfkdr"

ORACLE_BUCKET_ENDPOINT_URL = (
    f"https://{OCI_NAMESPACE}.compat.objectstorage.{OCI_REGION}.oraclecloud.com"
)

client = boto3.client(
    "s3",
    endpoint_url=ORACLE_BUCKET_ENDPOINT_URL,
    aws_access_key_id=OCI_ACCESS_KEY_ID,
    aws_secret_access_key=OCI_SECRET_ACCESS_KEY,
    region_name=OCI_REGION,
    config=Config(signature_version="s3v4"),
)


@deconstructible
class OracleStorage(Storage):

    def _save(self, name, content):
        client.upload_fileobj(
            content,
            OCI_BUCKET_NAME,
            name,
        )
        return name

    def exists(self, name):
        from botocore.exceptions import ClientError

        try:
            client.head_object(
                Bucket=OCI_BUCKET_NAME,
                Key=name,
            )
            return True
        except ClientError as exc:
            if exc.response["ResponseMetadata"]["HTTPStatusCode"] == 404:
                return False
            raise

    def url(self, name):
        return client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": OCI_BUCKET_NAME,
                "Key": name,
            },
            ExpiresIn=300,
        )

    def _open(self, name, mode="rb"):
        raise NotImplementedError(
            "A abertura de arquivos pelo Django ainda não foi implementada."
        )