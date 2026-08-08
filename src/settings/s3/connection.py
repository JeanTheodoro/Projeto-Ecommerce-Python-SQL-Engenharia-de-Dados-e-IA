import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[3]

load_dotenv(BASE_DIR / ".env")


class SupabaseS3Service:

    def __init__(self):
        self.endpoint = os.getenv("SUPABASE_DATALAKE_ENDPOINT")
        self.region = os.getenv("SUPABASE_REGION")
        self.bucket_name = os.getenv("SUPABASE_BUCKET_NAME")
        self.access_key_id = os.getenv("SUPABASE_ACCESS_KEY_ID")
        self.secret_access_key = os.getenv("SUPABASE_ACCESSS_KEY")

        print("ACCESS:", repr(self.access_key_id))
        print("SECRET:", repr(self.secret_access_key))
        print("ENDPOINT:", repr(self.endpoint))
        print("BUCKET:", repr(self.bucket_name))

        self.client = boto3.client(
            "s3",
            endpoint_url=self.endpoint,
            region_name=self.region,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
        )

    def list_files(self, prefix: str = "") -> list[str]:

        files = []

        paginator = self.client.get_paginator(
            "list_objects_v2"
        )

        pages = paginator.paginate(
            Bucket=self.bucket_name,
            Prefix=prefix,
        )

        for page in pages:
            for obj in page.get("Contents", []):
                files.append(obj["Key"])

        return files

    def upload_bytes(
        self,
        file_bytes: bytes,
        s3_key: str,
        content_type: str | None = None,
    ) -> None:

        extra_args = {}

        if content_type:
            extra_args["ContentType"] = content_type

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=s3_key,
            Body=file_bytes,
            **extra_args,
        )
