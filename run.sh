unzip choice.zip
unzip qa.zip

python3.8 test_to_oneline_json.py "${2}"

python3.8 swag_predict.py \
    --model_name_or_path choice \
    --do_predict \
    --context_file "${1}" \
    --prediction_file oneline_test.json \
    --output_dir swag

python3.8 run_qa.py \
    --model_name_or_path qa \
    --context_file "${1}"\
    --context_id_file prediction.choice.csv \
    --test_file oneline_test.json \
    --do_predict \
    --output_file "${3}" \
    --output_dir qa