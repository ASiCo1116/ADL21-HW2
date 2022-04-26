python curves.py \
  --model_name_or_path macbert_qa_2/checkpoint-20000 \
  --context_file /data/ADL/hw2/context.json \
  --context_id_file prediction.choice.csv \
  --validation_file /data/ADL/hw2/my_valid.json \
  --do_eval \
  --output_dir macbert_qa_2 \
  --dataloader_pin_memory=False \
  --dataloader_num_workers 4