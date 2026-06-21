import re


METHODS = [
    "CNN",
    "RNN",
    "LSTM",
    "GRU",
    "Transformer",
    "BERT",
    "Autoencoder",
    "GAN",
    "Neural Network",
    "Random Forest",
    "SVM",
    "KNN",
    "Decision Tree",
    "Attention"
]

DATASETS = [
    "MNIST",
    "CIFAR",
    "ImageNet",
    "Caltech",
    "TIMIT",
    "COCO",
    "Corel"
]

METRICS = [
    "accuracy",
    "precision",
    "recall",
    "f1",
    "f1-score",
    "auc",
    "error rate",
    "bleu",
    "rouge"
]


def extract_research_info(text):

    text_lower = text.lower()

    methods = set()
    datasets = set()
    metrics = set()

    for item in METHODS:
        if item.lower() in text_lower:
            methods.add(item)

    for item in DATASETS:
        if item.lower() in text_lower:
            datasets.add(item)

    for item in METRICS:
        if item.lower() in text_lower:
            metrics.add(item)

    return {
        "Methods": sorted(list(methods)),
        "Datasets": sorted(list(datasets)),
        "Metrics": sorted(list(metrics))
    }