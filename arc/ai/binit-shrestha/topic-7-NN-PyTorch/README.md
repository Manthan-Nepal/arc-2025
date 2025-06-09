## Neural Networks - PyTorch

### AND XOR Gates
- Neural network implementation using PyTorch

- Single Layer, Single Neuron

- Works alright for AND gate, but doesn't give 100% accuracy for XOR gate
    - Because XOR isn't linearly seprabale
    - Using 2 layers with multiple neurons successfully captures XOR's data

### Iris Dataset
- Directly loaded data, changed to Tensors

- 2 types of networks
    - Simple 1 layer, 100 epochs - Suboptimal results
    - 2 layers ReLU activation between, same no. of epochs, decent results

### QuickStart Optimization
- Mostly copied the code from the QuickStart resource

- For optimization, during data transformation, standardize and ToTensor() + More epochs

- Got over 80% accuracy, compared to 50% in the initial QuickStart resource

- Since data was FashionMNIST - Images, so using CNNs would do better for less epochs