from pathlib import Path

import pandas as pd


def converter_csv_to_parquet(
    input_dir: str | Path,
    output_dir: str | Path,
) -> list[Path]:

    input_path = Path(input_dir)
    output_path = Path(output_dir)

    output_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    parquet_files = []

    for csv_file in input_path.glob("*.csv"):

        print(f"Convertendo: {csv_file.name}")

        df = pd.read_csv(csv_file)

        parquet_file = (
            output_path / f"{csv_file.stem}.parquet"
        )

        df.to_parquet(
            parquet_file,
            engine="pyarrow",
            index=False,
        )

        parquet_files.append(parquet_file)

        print(
            f"Parquet criado: {parquet_file.name}"
        )

    return parquet_files
