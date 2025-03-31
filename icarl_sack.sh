#!/bin/bash


python main.py \
    --dataset=seq-cifar100 \
    --model=icarl \
    --buffer_size=2000 \
    --model_config=best \
    --cog_cl 1 \
    --wandb_entity=shiva-umbc \
    --wandb_project=Final-icarl-cifar100-cogcl-mammoth \
    --wandb_name=cogcl-run-seed-weightedloss_scores \
    --enable_other_metrics=True \
    --savecheck=task \
    --permute_classes=True \
    --ckpt_name=icarl-cifar100-cogcl-run-seed
