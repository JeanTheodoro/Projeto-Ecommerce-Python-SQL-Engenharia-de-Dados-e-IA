from pathlib import Path

from data.converter_csv_to_parquet import converter_csv_to_parquet
from settings.s3.connection import SupabaseS3Service


BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"

PROCESSED_DIR = BASE_DIR / "data" / "parquet"


def main():

    parquet_files = converter_csv_to_parquet(
        input_dir=RAW_DIR,
        output_dir=PROCESSED_DIR,
    )

    s3 = SupabaseS3Service()

    for parquet_file in parquet_files:

        with open(parquet_file, "rb") as file:
            parquet_bytes = file.read()

        s3_key = f"parquet/{parquet_file.name}"

        print("########")
        print(f"parquet: {s3_key}")
        print("########")
        s3.upload_bytes(
            file_bytes=parquet_bytes,
            s3_key=s3_key,
            content_type="application/octet-stream",
        )

        print(
            f"Upload realizado: {s3_key}"
        )


if __name__ == "__main__":
    main()