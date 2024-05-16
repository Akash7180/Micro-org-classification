# Microorganism Classification Project README

## Introduction
Welcome to our Microorganism Classification project repository! This project focuses on classifying microorganisms using deep learning techniques. We employ Convolutional Neural Networks (CNNs) to classify microorganism images into eight different categories. The project utilizes Anaconda Navigator and Jupyter Notebook for model development, saving the trained models in H5 file format. Additionally, we utilize Django for deploying the model with user login and signup functionalities.

## Project Components
1. **Data Collection and Preprocessing**: Microorganism images are collected and preprocessed before feeding into the models. The data is classified into the following eight categories:
   - Euglena
   - Amoeba
   - Paramecium
   - Hydra
   - Yeast
   - Rod Bacteria
   - Spiral Bacteria
   - Spherical Bacteria

2. **Model Development**:
   - Manual CNN: A CNN model is manually constructed for classification.
   - VGG Model: Utilization of the VGG architecture for classification.
   - LeNet Model: Deployment of the LeNet architecture for classification.

3. **Model Deployment**:
   - Django Framework: The trained models are deployed using Django, allowing users to interact with the classification system.
   - User Login and Signup: Authentication functionalities are implemented using Django for secure access to the classification system.

## Usage
To utilize the microorganism classification system:
1. Ensure you have Anaconda Navigator installed for managing dependencies.
2. Open Jupyter Notebook to access the model building scripts.
3. Train the models using the provided datasets and save them in H5 format.
4. Install Django and set up the project for deployment.
5. Deploy the models using Django, providing user login and signup functionalities.
6. Users can upload microorganism images for classification through the deployed Django application.
7. The system will classify the images into one of the eight predefined categories. If the image does not belong to any of these categories, it will display an "Unknown Image Detected" message.

## Contributors
- [List contributors here]

## License
[Include license information here]

## Contact
For any inquiries or support regarding the project, feel free to contact [include contact information].

## Acknowledgments
We would like to acknowledge the following resources and individuals for their contribution to this project:
- [List acknowledgments here]

