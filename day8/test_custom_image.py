import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from PIL import Image

# 1. Model Train Pandrom (Standard MNIST)
print("Model Train Aagudhu... ⏳")
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train, X_test = X_train / 255.0, X_test / 255.0

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=3, verbose=1)
print("\nModel Training Complete! 🎉")


# 2. Custom Image Preprocessing Function
def predict_my_image(image_path):
    # Image-a open pandrom
    img = Image.open(image_path)
    
    # Image-a Black & White (Grayscale) format-ku maathuroam
    img = img.convert('L')
    
    # Model-ku thevaiyana 28x28 size-ku resize pandrom
    img = img.resize((28, 28))
    
    # Image array-a maathuroam
    img_array = np.array(img)
    
    # Mukkiyam: Paint-la White background-la Black text-la ezhudhina, 
    # Invert pannanum (MNIST-la Black Background-la White Text irukkum)
    # Background white (255)-a irundha invert pannurom:
    if np.mean(img_array) > 127:
        img_array = 255 - img_array
        
    # Scale pixels (0.0 to 1.0)
    img_array = img_array / 255.0
    
    # Model (1, 28, 28) shape-a input-a edukkum (Batch dimension add pandrom)
    img_array = img_array.reshape(1, 28, 28)
    
    # Prediction
    prediction = model.predict(img_array)
    predicted_number = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    
    print("\n---------------------------------")
    print(f"📷 Image Path: {image_path}")
    print(f"🎯 Neural Network Prediction: NUMBER {predicted_number}")
    print(f"🔥 Confidence: {confidence:.2f}%")
    print("---------------------------------")

predict_my_image('digit.png')
# 3. Unga Image-a Test Pannunga!
# Unga folder-la 'my_digit.png' nu file vechu check pannunga
# Example: predict_my_image('my_digit.png')