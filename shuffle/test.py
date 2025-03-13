import json
from pathlib import Path
import requests


def fetch_vector() :
    test_dir = Path(__file__).parent
    # Load test vectors
    with open(test_dir / "shuffle_tests.json", "r") as f:
        vectors_json = json.load(f)

    return vectors_json


if __name__ == "__main__":
    vectors = fetch_vector()
    for vector in vectors:
        input_array = []
        for i in range(vector["input"]):
            input_array.append(i)

        response = requests.post("http://localhost:8000/api/v1/shuffle/validtae", json={"input" : {"input" : input_array, "entropy": vector["entropy"]}, "output" : { "output" : vector["output"]}})
        result = response.json()
        if result.status != "ok":
            print(f"Failed: {vector}")