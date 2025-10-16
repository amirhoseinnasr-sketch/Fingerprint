import os  
import numpy as np  
import pandas as pd  
import cv2  
import tensorflow as tf  
from sklearn.model_selection import train_test_split  
from tensorflow.keras.preprocessing.image import ImageDataGenerator  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  

category_path = r'C:\Users\Farzin\Desktop\finger\archive(1)\SOCOFing\Altered\f'

if os.path.exists(category_path):
    for img in os.listdir(category_path):
        print(img)
else:
    print("The specified path does not exist.")


# تنظیم مسیر به دیتاست  
dataset_path = r'C:\Users\Farzin\Desktop\finger\archive(1)\SOCOFing\Altered\f'  # مسیر به پوشه دیتاست  
categories = ['male', 'female']  # برچسب‌های دسته‌ها  

data = []  
labels = []  

# بارگذاری داده‌ها 
for category in categories:  
    category_path = os.path.join(dataset_path, category)  
    for img in os.listdir(category_path):  
        img_path = os.path.join(category_path, img)  
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # بارگذاری تصویر به صورت سیاه و سفید  
        image = cv2.resize(image, (128, 128))  # تغییر اندازه تصویر  
        data.append(image)  
        labels.append(categories.index(category))  

# تبدیل داده‌ها به آرایه numpy  
data = np.array(data) / 255.0  # نرمال‌سازی داده‌ها  
data = np.reshape(data, (-1, 128, 128, 1))  # اضافه کردن بعد کانال  

labels = np.array(labels)  

# تقسیم داده‌ها به مجموعه آموزشی و آزمایشی  
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)  

# استفاده از Augmentation برای افزایش تنوع داده  
datagen = ImageDataGenerator(horizontal_flip=True, rotation_range=20)



# طراحی مدل CNN  
model = Sequential([  
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),  
    MaxPooling2D(pool_size=(2, 2)),  
    Conv2D(64, (3, 3), activation='relu'),  
    MaxPooling2D(pool_size=(2, 2)),  
    Conv2D(128, (3, 3), activation='relu'),  
    MaxPooling2D(pool_size=(2, 2)),  
    Flatten(),  
    Dense(128, activation='relu'),  
    Dropout(0.5),  
    Dense(2, activation='softmax')  # دو دسته: مرد و زن  
])  

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# آموزش مدل  
history = model.fit(datagen.flow(X_train, y_train, batch_size=32),   
                    validation_data=(X_test, y_test),   
                    epochs=20)

# ارزیابی مدل  
loss, accuracy = model.evaluate(X_test, y_test)  
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")

def predict_gender(image_path):  
    # بارگذاری و پیش‌پردازش تصویر  
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  
    img = cv2.resize(img, (128, 128))  
    img = img / 255.0  
    img = np.reshape(img, (1, 128, 128, 1))  

    # پیش‌بینی جنسیت  
    prediction = model.predict(img)  
    return categories[np.argmax(prediction)]  

# تست با یک تصویر جدید  
result = predict_gender(r'لوکیشن یه اثر انگشت جدید')  
print(f'The predicted gender is: {result}')