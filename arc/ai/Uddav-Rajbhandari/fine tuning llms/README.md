 # Topics
1. PEFT
# Objectives
1. To train and evaluate LLMs using custom datasets

1. Learn all the concepts clearly rather than implementation.
# Tasks
1. Follow [this](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb#scrollTo=LjY75GoYUCB8) unsloth notebook step by step to finetune llama3.2-3B. Learn the purpose of every line of code by printing the intermediate outputs and surfing the internet. Use kaggle with accelerator(gpu) or google colab.

2. Create your own custom data for finetuning. Assume you want to train the llama3.2-3B model to think step by step i.e. to give it CoT capability. You want to use it to teach simple mathematics to grade 5 students. Create synthetic data [like](https://huggingface.co/datasets/isaiahbjork/chain-of-thought/viewer?views%5B%5D=train) this using chatGPT or likewises.

3. Using the same unsloth notebook from 1 and dataset created from 2, finetune the llama3.2-3B model and notice its response before and after finetuning. Refer to this [blog](https://medium.com/@chuciche/fast-llm-fine-tuning-with-unsloth-train-on-your-own-data-a0f109ba21a3) if needed.
