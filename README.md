# Microorganism Classification Project

## Introduction
This project focuses on microorganism classification using deep learning techniques. We employ Anaconda Navigator and Jupyter Notebook for model development, saving the trained models in H5 file format. Additionally, Django is utilized for deploying the model with user login and signup functionalities. The project includes three models: Manual CNN, VGG, and LeNet, trained to classify microorganism images into eight categories.

By [Your Name]

- [Data Collection and Preprocessing](#data-collection-and-preprocessing)
- [Model Development](#model-development)
- [Model Deployment](#model-deployment)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Contact](#contact)

## Data Collection and Preprocessing
Microorganism images are collected and preprocessed before feeding into the models. The data is classified into the following eight categories:
- Euglena
- Amoeba
- Paramecium
- Hydra
- Yeast
- Rod Bacteria
- Spiral Bacteria
- Spherical Bacteria

## Model Development
Three models are developed:
- Manual CNN: A manually constructed CNN model.
- VGG Model: Utilizes the VGG architecture for classification.
- LeNet Model: Deploys the LeNet architecture for classification.

## Model Deployment
The trained models are deployed using Django, allowing users to interact with the classification system. User login and signup functionalities are implemented for secure access.

## Usage
To execute the microorganism classification project after downloading:

1. **Install Anaconda Navigator**: Download and install Anaconda Navigator from [here](https://www.anaconda.com/products/distribution).
2. **Open Jupyter Notebook**: Launch Jupyter Notebook from Anaconda Navigator.
3. **Access Model Building Scripts**: Navigate to the directory where you downloaded the project and open Jupyter Notebook. Open the provided scripts for model building.
4. **Train Models**: Run the scripts in Jupyter Notebook to train the three models: manual CNN, VGG, and LeNet, using the provided datasets. Save the trained models in H5 file format.
5. **Install Django**: Install Django framework by running `pip install django` in your terminal.
6. **Update Model Paths**: Open the `view.py` file located in the `coding/APP` directory of the downloaded code in VS Code. Change the path of the models to the path on your computer (`/MODELFILE/keras_model.h5`) and the path of the image directory (`coding/deploy/project/media`).
7. **Run Django Server**: Open the terminal and navigate to the project directory. Run `python manage.py runserver` to start the Django server.
8. **Access the Application**: Open a web browser and navigate to the local server address provided by Django (usually `http://127.0.0.1:8000/`). You can now interact with the microorganism classification system, upload images for classification, and receive results.




