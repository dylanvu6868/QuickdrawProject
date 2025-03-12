
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np

# Giả lập dữ liệu (Cần thay bằng dữ liệu thực tế)
X, y = np.random.rand(1000, 28, 28, 1), np.random.randint(0, 5, 1000)
y = tf.keras.utils.to_categorical(y, num_classes=5)

# Xây dựng mô hình CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(5, activation='softmax')
])

# Compile và train model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=5, batch_size=32, validation_split=0.2)

# Lưu model
model.save("quickdraw_model")
print("Model đã lưu thành công!")
