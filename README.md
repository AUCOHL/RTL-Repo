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

Example Output

``` bash
Statistics for the predictions are as follows:

Total count: 1174
Edit_similarity: 61.37819
Exact_match: 33.816
```


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
