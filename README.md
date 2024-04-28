# RTL-Repo Benchmark

This repository contains the code for the RTL-Repo benchmark introduced in the paper [RTL-Repo: A Benchmark for Evaluating LLMs on Large-Scale RTL Design Projects](https://arxiv.org/abs/). RTLRepo comprises a dataset of over 4000 code samples extracted from public GitHub repositories, each containing the context of all Verilog code in the repository. This benchmark provides a valuable resource for the hardware design community to assess and compare LLMs' performance in real-world RTL design scenarios and train LLMs specifically for Verilog code generation in complex, multi-file RTL projects.

You can access our dataset on 🤗 HuggingFace Hub using this link [🤗 RTL-Repo](https://huggingface.co/datasets/ahmedallam/RTL-Repo).

# Installation

```bash
git clone https://github.com/ahmed-alllam/RTLRepo.git
cd RTLRepo
pip install -r requirements.txt
```

# How to run

## Generate model predictions

```bash
python src/generate_model_predictions.py --model_name <model_name_or_path> --model_max_tokens <model_max_tokens> --temperature <temperature>
```

## Evaluate

```bash
python src/evaluate.py --prediction_path predictions/gpt-3.5-turbo.jsonl
```

Output

``` bash
Statistics for the predictions are as follows:

Total count: 1174
Edit_similarity: 61.37819
Exact_match: 33.816
```


# Citation
    
```bibtex
@article{,
    title={},
    author={},
    journal={},
    year={}
}
```
