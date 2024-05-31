from datasets import load_dataset, DatasetDict

# Load the dataset from Hugging Face
dataset = load_dataset("torchgeo/tropical_cyclone")

# Perform a train-test split
train_test_split = dataset['train'].train_test_split(test_size=0.2)

# Create a DatasetDict with train and test sets
dataset = DatasetDict({
    'train': train_test_split['train'],
    'test': train_test_split['test']
})

# Check the splits
print(dataset)
