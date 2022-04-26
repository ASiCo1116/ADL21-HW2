# Homework 2 ADL NTU 110-2 Spring

## Environment

```shell
# If you have pipenv, you can build the environemt from pipfile
pipenv install --skip-lock
```

## Preprocessing

```shell
# To preprocess intent detectiona and slot tagging datasets
bash preprocess.sh
```

## Context selection

#### Training

```shell
# choice_train.sh

python3 run_swag.py \
    --model_name_or_path bert-base-chinese \
    --train_file PATH_TO_TRAIN_FILE \
    --validation_file PATH_TO_TRAIN_VALID_FIEL \
    --do_train \
    --do_eval \
    --context_file PATH_TO_CONTEXT_FILE \
    --max_seq_length 384 \
    --learning_rate 3e-5 \
    --num_train_epochs 3 \
    --output_dir PATH_TO_SAVE_CHECKPOINT \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --seed SEED
```

#### Testing

```python
# choice_predict.sh

python3 swag_predict.py \
    --model_name_or_path PATH_TO_SAVE_CHECKPOINT \
    --do_predict \
    --context_file PATH_TO_CONTEXT_FILE \
    --prediction_file PATH_TO_TEST_FILE \
    --max_seq_length 384 \
    --learning_rate 3e-5 \
    --num_train_epochs 3 \
    --dataloader_pin_memory=False \
    --dataloader_num_workers 4 \
    --output_dir bert_base_chinese_choice \
    --per_device_eval_batch_size 2 \
    --seed SEED
```

## Question answering

#### Training

```shell
# qa_train.sh

python run_qa.py \
  --model_name_or_path hfl/chinese-macbert-base \
  --context_file PATH_TO_CONTEXT_FILE \
  --train_file PATH_TO_TRAIN_FILE \
  --validation_file PATH_TO_TRAIN_VALID_FIEL \
  --do_train \
  --do_eval \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 2 \
  --num_train_epochs 2 \
  --max_steps 20000 \
  --output_dir PATH_TO_SAVE_CHECKPOINT
```

#### Testing

```python
# qa_predict.sh

python run_qa.py \
  --model_name_or_path PATH_TO_SAVE_CHECKPOINT \
  --context_file /data/ADL/hw2/context.json \
  --context_id_file prediction.choice.csv \ # from context selection prediction
  --test_file PATH_TO_TEST_FILE \
  --do_predict \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 2 \
  --output_dir PATH_TO_SAVE_CHECKPOINT \
  --dataloader_pin_memory=False \
  --dataloader_num_workers 4
```