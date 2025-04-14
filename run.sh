torch-model-archiver \
    --model-name skin_tone_model \
    --version 1.0 \
    --serialized-file output/skin_tone_model.pth \
    --handler models/skinton_handler.py \
    --extra-files models/model.py \
    --export-path model_store \
    --force