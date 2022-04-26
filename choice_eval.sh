export CUDA_VISIBLE_DEVICES=1

python3 run_swag.py \
    --model_name_or_path bert-base-chinese \
    --do_eval \
    --context_file /data/ADL/hw2/context.json \
    --train_file /data/ADL/hw2/my_train.json \
    --validation_file /data/ADL/hw2/my_valid.json \
    --max_seq_length 384 \
    --learning_rate 3e-5 \
    --num_train_epochs 3 \
    --output_dir bert_base_chinese \
    --per_device_eval_batch_size 2 \
    --seed 1116