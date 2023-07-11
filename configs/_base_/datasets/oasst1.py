from datasets import load_dataset
from mmchat.datasets import process_hf_dataset
from mmengine.dataset import DefaultSampler

"""
------------ Dataset Meta Info (after `load_dataset`) ------------

DatasetDict({
    train: Dataset({
        features: ['text'],
        num_rows: 9846
    })
    test: Dataset({
        features: ['text'],
        num_rows: 518
    })
})

------------ Dataset Meta Info (after `process_hf_dataset`) ------------

DatasetDict({
    train: Dataset({
        features: ['text', 'input', 'output'],
        num_rows: 9846
    })
    test: Dataset({
        features: ['text', 'input', 'output'],
        num_rows: 518
    })
})

"""


oasst1 = dict(
    type = process_hf_dataset,
    dataset = dict(
        type = load_dataset,
        path = 'timdettmers/openassistant-guanaco',
    ),
    map_fn = "lambda x: {'input': '', 'output': x['text']}",
)

train_dataloader = dict(
    batch_size=16,
    num_workers=2,
    dataset = oasst1,
    sampler=dict(type=DefaultSampler, shuffle=True)
)