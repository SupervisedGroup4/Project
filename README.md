{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "name": "CNN_full_model.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "machine_shape": "hm",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/elisabethnetland/Labeling-Images-as-Edited-Using-CNN/blob/main/CNN_full_model.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kUbJKJNFASXp",
        "outputId": "f9fa38b4-0504-42c0-e8a8-88fd9e3429a5"
      },
      "source": [
        "from google.colab import drive\n",
        "\n",
        "drive.mount('/content/drive', force_remount=True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3ptg62pWCvZn"
      },
      # TDT4173 - Assignment 3
The repository contains a **Convolutional Neural Network (CNN)-model buildt to classify images of real and artificial human faces**. The code is a part of the third assignment in the course TDT4173 Machine Learning at NTNU, and is created by the group Supervised learning Group 4. The purpose of this project is the academic learning of adressing a machine learning task.

### Running the application 
The model can be run with a Virtual Machine, the following setup is with Google Colab: 

1. First you have to upload the dataset from kaggle on Google Drive: https://www.kaggle.com/ciplab/real-and-fake-face-detection

2. Then you have to open the CNN model in your virtual machine (here Google Colab), by pressing this button --> 

3. You need to fetch the dataset from Google Drive to Google Colab. This procedure is presented below. 

**Fetch the dataset from Google Colab**

1. Executing the below code which will provide you with an authentication link

```
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```

2. Open the link

3. Choose the Google account whose Drive you want to mount

4. Allow Google Drive Stream access to your Google Account

5. Copy the code displayed, paste it in the text box as shown below, and press Enter colab import drive

Once the Drive is mounted, you’ll get the message **“Mounted at /content/drive”**, and you’ll be able to browse through the contents of your Drive from the file-explorer pane. 

Now you can interact with your Google Drive as if it was a folder.
Exampel from the model:
\
`fake = "/content/drive/My Drive/archive/real_and_fake_face/training_fake"`

**The setup is complete and you can run the code**
