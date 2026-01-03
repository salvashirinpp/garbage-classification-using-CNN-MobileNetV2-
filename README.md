# ♻️ Garbage Classification Using CNN (MobileNetV2)

An end-to-end **Deep Learning project** that classifies garbage images into multiple waste categories using a **Convolutional Neural Network (CNN)** based on **MobileNetV2**.  
The project demonstrates the complete workflow from **model training** to **web-based prediction using Flask**.

---

## 📌 Project Summary

Waste management is a major environmental challenge. Manual waste segregation is inefficient and error-prone.  
This project aims to **automatically classify garbage images** into predefined categories using deep learning, enabling smarter recycling and waste management systems.

The solution leverages **transfer learning** with MobileNetV2 to achieve accurate image classification while keeping the model lightweight and efficient.

---

## 🎯 Objectives

- Automate garbage classification using image data  
- Apply CNN and transfer learning concepts in a real-world problem  
- Build a deployment-ready ML application  
- Provide confidence-based predictions for uploaded images  

---

## 🧠 Model Overview

- Model Type: Convolutional Neural Network (CNN)
- Base Architecture: MobileNetV2 (Transfer Learning)
- Framework: TensorFlow / Keras
- Input Image Size: 224 × 224 RGB
- Output: Multi-class classification with confidence score

---

## 🗂️ Garbage Categories

The model classifies images into the following categories:

- Battery  
- Biological waste  
- Brown glass  
- Cardboard  
- Clothes  
- Green glass  
- Metal  
- Paper  
- Plastic  
- Shoes  
- Trash  
- White glass  

---

## 📁 Project Structure (High-Level)

- Model training notebook  
- Trained CNN model file  
- Flask backend application  
- Frontend HTML interface  
- Project documentation  

---

## ⚙️ System Workflow

1. User uploads a garbage image through the web interface  
2. Image is resized and normalized  
3. CNN model processes the image  
4. Model predicts the waste category  
5. Prediction and confidence score are returned to the user  

---

## 📊 Model Training Summary

- Dataset sourced from Kaggle  
- Images preprocessed and augmented  
- MobileNetV2 used as a frozen base model  
- Custom classification layers added  
- Model trained and validated  
- Best-performing model saved for inference  

---

## 🌐 Application Overview

- Web-based interface built using Flask  
- Supports image upload  
- Returns prediction results in real time  
- Displays confidence score for transparency  

---

## 🚀 Key Highlights

- Uses transfer learning for better performance  
- Lightweight and efficient model  
- Real-world environmental use case  
- Clean separation of training and inference  
- Suitable for academic and portfolio projects  

---

## 🔮 Future Enhancements

- Improve accuracy with more training data  
- Add Grad-CAM visual explanations  
- Deploy on cloud platforms  
- Add mobile-friendly UI  
- Support batch image predictions  

---

## 🎯 Use Cases

- Smart waste segregation systems  
- Recycling automation  
- Smart city initiatives  
- Environmental monitoring solutions  
- Educational deep learning projects  

---

## 👤 Author

**Salva**  
Diploma in Data Science with Artificial Intelligence  
Focus Areas: Deep Learning, Computer Vision, Applied AI  

---

## 📜 License

This project is intended for **educational and learning purposes** only.
