import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

print("TensorFlow Version:", tf.__version__)

# 1. Dataset Load & Preprocessing
# MNIST Dataset-a TensorFlow-la irundhe direct-a load pannalam
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Pixels 0-255 range-la irukkum. Adhai 0.0 - 1.0-ku Normalize pandrom
X_train, X_test = X_train / 255.0, X_test / 255.0

# 2. Building the Neural Network Architecture
model = models.Sequential([
    # 2D $28 \times 28$ Image-a 1D array-a ($784$ numbers) maathudhu
    layers.Flatten(input_shape=(28, 28)),
    
    # Hidden Layer 1: 128 Neurons with ReLU activation
    layers.Dense(128, activation='relu'),
    
    # Hidden Layer 2: 64 Neurons with ReLU activation
    layers.Dense(64, activation='relu'),
    
    # Output Layer: 10 Neurons (0 to 9 numbers) with Softmax (Probabilities)
    layers.Dense(10, activation='softmax')
])

# 3. Compile the Model (Optimizer, Loss, Metrics)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 4. Train the Model (Epochs = Number of full passes)
print("\nTraining Model Start Aagudhu... ⏳")
model.fit(X_train, y_train, epochs=5, batch_size=32)

# 5. Evaluate Performance on Unseen Test Data
print("\nTesting Model Performance... 📊")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nFinal Test Accuracy: {test_acc * 100:.2f}%")

# 6. Live Test / Prediction on 1st Test Image
sample_img = X_test[0]
prediction = model.predict(sample_img.reshape(1, 28, 28))
predicted_label = tf.argmax(prediction[0]).numpy()

print(f"\nTrue Label: {y_test[0]}")
print(f"Neural Network Predicted Label: {predicted_label}")