# RTL-Repo Benchmark

This repository contains the code and data for the RTL-Repo benchmark introduced in the paper [RTL-Repo: A Benchmark for Evaluating LLMs on Large-Scale RTL Design Projects](https://arxiv.org/abs/2405.17378).

## 📰 News

* **[May. 10, 2024]**: RTL-Repo has been accepted to [IEEE LAD'24](https://www.islad.org) - The First IEEE International Workshop on LLM-Aided Design!


## 👋 Overview

RTL-Repo is a benchmark for evaluating LLMs' effectiveness in generating Verilog code autocompletions within large, complex codebases. It assesses the model's ability to understand and remember the entire Verilog repository context and generate new code that is correct, relevant, logically consistent, and adherent to coding conventions and guidelines, while being aware of all components and modules in the project. This provides a realistic evaluation of a model's performance in real-world RTL design scenarios. RTL-Repo comprises over 4000 code samples from GitHub repositories, each containing the context of all Verilog code in the repository, offering a valuable resource for the hardware design community to assess and train LLMs for Verilog code generation in complex, multi-file RTL projects.

You can access our dataset on 🤗 HuggingFace Hub using this link [🤗 RTL-Repo](https://huggingface.co/datasets/ahmedallam/RTL-Repo), or you can run the following code:

```python
from datasets import load_dataset
rtl_repo = load_dataset('ahmedallam/RTL-Repo', split='test')
```

## 💽 Installation

Before proceeding with the installation, please ensure you have PyTorch installed. Refer to the [PyTorch installation page](https://pytorch.org/get-started/locally/#start-locally) for the specific installation command for your platform.

You can install and run our benchmark easily by following these commands:

```bash
git clone https://github.com/AUCOHL/RTL-Repo.git
cd RTL-Repo
pip install -r requirements.txt
```

## 🚀 Usage

### Generate model predictions

To run your model on our benchmark's full test dataset, simply execute this command:

```bash
python src/generate_model_predictions.py --model_name <model_name_or_path> --model_max_tokens <model_max_tokens> --temperature <temperature>
```

### Evaluate

After generating predictions from your model, execute this script to produce the evaluation statistics:

```bash
python src/evaluate.py --prediction_path <prediction_path>
```

Example Output (GPT-3.5):

```
Statistics for the predictions are as follows:

Total count: 1174
Edit similarity: 61.37819
Exact match: 33.816
```


## 🏆 Leaderboard


| Model Name                                                       | Publisher    | Number of Parameters | Open-Source? | Verilog-Specific? | Edit Similarity | Exact Match |
|------------------------------------------------------------------|--------------|----------------------|-------|-------------------|-----------------|-------------|
| [GPT-4](https://arxiv.org/abs/2303.08774v3)                      | OpenAI       | N/A                  | ❌    | ❌                | 71.87           | 48.5        |
| [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5-turbo) | OpenAI       | N/A                  | ❌    | ❌                | 61.4            | 33.8        |
| [RTLCoder-DeepSeek](https://huggingface.co/ishorn5/RTLCoder-Deepseek-v1.1) | Liu et al.    | 6.7B                 | ✅    | ✅                | 48.1            | 16.2        |
| [Starcoder2](https://huggingface.co/bigcode/starcoder2-15b)      | BigCode      | 15B                  | ✅    | ❌                | 48.0            | 17.0        |
| [VeriGen](https://huggingface.co/shailja/fine-tuned-codegen-16B-Verilog)  | Thakur et al. | 16B                  | ✅    | ✅                | 43.9            | 9.5         |
| [RTLCoder-Mistral](https://huggingface.co/ishorn5/RTLCoder-v1.1) | Liu et al.   | 7B                   | ✅    | ✅                | 37.9            | 8.3         |


## ✍️ Citation

If you find our work helpful, please use the following citation.
    
```bibtex
@misc{allam2024rtlrepo,
      title={RTL-Repo: A Benchmark for Evaluating LLMs on Large-Scale RTL Design Projects}, 
      author={Ahmed Allam and Mohamed Shalan},
      year={2024},
      eprint={2405.17378},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

## 🪪 License

All rights reserved ©2024 The American University in Cairo and other contributors. RTL-Repo is available under the Apache 2.0 License: See `LICENSE`.
