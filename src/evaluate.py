import json
import argparse

from utils import exact_match_score, edit_similarity_score

def main():
    args = argparse.ArgumentParser()

    args.add_argument("--prediction_path", type=str)

    args = args.parse_args()

    predictions_list = []

    with open(args.prediction_path, "r") as f:
        for line in f:
            predictions_list.append(json.loads(line.strip()))

    mean_es = edit_similarity_score([x["generated"] for x in predictions_list],
                                    [x["label"] for x in predictions_list])

    mean_em = exact_match_score([x["generated"] for x in predictions_list],
                                [x["label"] for x in predictions_list])

    total_count = len(predictions_list)

    print("Statistics for the predictions are as follows:\n")
    print(f"Total count: {total_count}")
    print(f"Edit similarity: {mean_es}")
    print(f"Exact match: {mean_em*100}")

if __name__ == "__main__":
    main()
