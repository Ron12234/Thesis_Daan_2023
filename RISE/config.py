# some training parameters
EPOCHS = 40
BATCH_SIZE = 10
NUM_CLASSES = 3
image_height = 560
image_width = 560
channels = 1

save_model_dir = "path model here"
dataset_dir = "path datasets here"


train_dir = dataset_dir + "train/"
valid_dir = dataset_dir + "valid/"
test_dir = 'path to test set here'

# choose a network
# model = "resnet18"
model = "resnet34"
#model = "resnet50"
# model = "resnet101"
# model = "resnet152"
