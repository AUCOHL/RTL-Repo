import re

from fuzzywuzzy import fuzz

def construct_prompt(data, tokenizer=None, max_token_nums=15800):
    cross_file_prompt = f"// Repo Name: {data['repo_name']}\n"

    for snippet in data['context']:
        cross_file_prompt += f"// Path: {snippet['path']}\n{snippet['snippet']}" + "\n\n"

    in_file_prompt = f"// Path: {data['file_path']}\n{data['cropped_code']}\n"

    if tokenizer is not None and max_token_nums is not None:
        cross_file_prompt_token_nums = len(tokenizer.encode(cross_file_prompt))
        in_file_prompt_token_nums = len(tokenizer.encode(in_file_prompt))

        exceed_token_nums = cross_file_prompt_token_nums + in_file_prompt_token_nums - max_token_nums

        if exceed_token_nums > 0:
            cross_file_prompt_lines = cross_file_prompt.split("\n")
            for i in range(len(cross_file_prompt_lines)-1, -1, -1):
                exceed_token_nums -= len(tokenizer.encode(cross_file_prompt_lines[i]))

                if exceed_token_nums < 0:
                    break

            cross_file_prompt = "\n".join(cross_file_prompt_lines[:i]) + "\n\n"

    prompt = cross_file_prompt + in_file_prompt

    prompt = re.sub(r'\n{4,}', '\n\n', prompt)

    return prompt


def post_process(prediction):
    # Take the first non-empty, non-comment line
    # If all lines are comments, take the last comment line
    lines = prediction.split("\n")
    last_comment_line = ""

    for line in lines:
        if line.strip():
            if not line.strip().startswith("//"):
                return line
            last_comment_line = line

    return last_comment_line


def exact_match_score(predictions, ground_truths):
    if len(predictions) != len(ground_truths):
        raise ValueError("The length of the predicted codes and the ground truth codes should be equal.")

    exact_match = 0
    for pred, gt in zip(predictions, ground_truths):
        if pred.split() == gt.split():
            exact_match += 1

    return round(exact_match / len(predictions), 5)


def edit_similarity_score(predictions, ground_truths):
    if len(predictions) != len(ground_truths):
        raise ValueError("The length of the predicted codes and the ground truth codes should be equal.")

    edit_sim = 0.0
    for pred, gt in zip(predictions, ground_truths):
        edit_sim += fuzz.ratio(pred, gt)

    return round(edit_sim / len(predictions), 5)
