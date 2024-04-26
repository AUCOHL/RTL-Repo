import json
import tqdm
import os
import argparse
import torch

from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.utils.data import DataLoader

from utils import construct_prompt, post_process

def save_predictions(predictions_list, prediction_path):
    with open(prediction_path, "a") as f:
        for item in predictions_list:
            f.write(json.dumps(item) + "\n")

def main():
    args = argparse.ArgumentParser()

    args.add_argument("--model_name", type=str, default="shailja/fine-tuned-codegen-16B-Verilog")
    args.add_argument("--model_max_tokens", type=int, default=2048)
    args.add_argument("--temperature", type=float, default=0.2)

    args = args.parse_args()

    if not os.path.exists("predictions"):
        os.makedirs("predictions")

    prediction_path = f"predictions/{args.model_name.split('/')[-1]}.jsonl"
    predictions_list = []

    dataset = load_dataset("ahmedallam/RTL-Repo", split="test")
    print(dataset)

    dataset = dataset.shuffle(seed=2003)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForCausalLM.from_pretrained(args.model_name, torch_dtype=torch.float16, device_map='auto')

    for data_item in tqdm.tqdm(dataset):
        prompt = construct_prompt(data_item, tokenizer, max_token_nums=args.model_max_tokens - 80)
        inputs = tokenizer(prompt, return_tensors="pt", max_length=args.model_max_tokens - 80, truncation=True).to('cuda')
        input_ids_length = inputs["input_ids"].shape[1]

        outputs = model.generate(**inputs, max_new_tokens=50, do_sample=True, temperature=args.temperature, pad_token_id=tokenizer.eos_token_id)
        outputs = outputs[0, input_ids_length:]
        prediction = tokenizer.decode(outputs, skip_special_tokens=True)
        prediction = post_process(prediction)

        print(f"Generated: {prediction}")
        print(f"Label: {data_item['next_line']}")
        predictions_list.append({
            'generated': prediction,
            'label': data_item['next_line']
        })

    save_predictions(predictions_list, prediction_path)

if __name__ == "__main__":
    main()
