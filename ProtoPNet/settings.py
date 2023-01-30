base_architecture = 'vgg19'
img_size = 560
prototype_shape = (210, 128, 1, 1) #(num_protype, ...)
num_classes = 3
prototype_activation_function = 'log'  # prototype_activation_function could be 'log', 'linear',
add_on_layers_type = 'regular'

experiment_run = 'exeriment_name_here'

data_path = 'here'
train_dir = data_path + 'path to augmented train set here'
test_dir = data_path + 'path to validation set here'
train_push_dir = data_path + 'path to unaugmented set here'
train_batch_size = 10
test_batch_size = 12
train_push_batch_size = 10

joint_optimizer_lrs = {'features': 1e-4,
                       'add_on_layers': 3e-3,
                       'prototype_vectors': 3e-3}
joint_lr_step_size = 5

warm_optimizer_lrs = {'add_on_layers': 3e-3,
                      'prototype_vectors': 3e-3}

last_layer_optimizer_lr = 1e-4

coefs = {
    'crs_ent': 1,
    'clst': 0.8,
    'sep': -0.08,
    'l1': 1e-4,
}

num_train_epochs = 31
num_warm_epochs = 3

push_start = 5

push_epochs = [i for i in range(num_train_epochs) if i % 5 == 0]
