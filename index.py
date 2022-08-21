# 21 August 2022 - Added the ability to create a CLI package from a single file.
# Build to convert the Google Evaluation Sheet to json to use that in comparing 2 json files.
import typer
import pandas as pd
import json
app = typer.Typer()


def fileExists(file):
    if file is None:
        return False
    else:
        return True


@app.command()
def json2csv(
    json_file: str = typer.Argument(..., help="JSON file to convert"),
    csv_file: str = typer.Option(None, help="CSV file to save"),
):
    """Convert JSON file to CSV file"""
    if not fileExists(json_file):
        typer.secho(f"{json_file} does not exist", fg="red")
        return
    if not fileExists(csv_file):
        csv_file = json_file.replace(".json", ".csv")
    df = pd.read_json(json_file)
    df.to_csv(csv_file)
    typer.secho(f"{json_file} converted to {csv_file}", fg="green")

    print("Creating CLI package")


@app.command()
def csv2json(
    csv_file: str = typer.Argument(..., help="CSV file to convert"),
    json_file: str = typer.Option(None, help="JSON file to save"),
):
    """Convert CSV file to JSON file"""
    # check if file exists and is a csv file
    try:
        if csv_file.endswith(".csv") and fileExists(csv_file):
            df = pd.read_csv(csv_file)
            df.to_json(f'{csv_file}.json', orient='records')
            print("File converted to json")
    except Exception as e:
        print("\nError: ", e, "\n\n",
              "Please check if file exists and is a csv file")


if __name__ == "__main__":
    app()
