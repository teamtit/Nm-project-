{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNbW1/VU6fFOqjTCk9SkboT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/teamtit/Nm-project-/blob/main/Untitled5.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "yMYRaJykM4ME"
      },
      "outputs": [],
      "source": [
        "# Step 1: Create demo fake news dataset\n",
        "import pandas as pd\n",
        "\n",
        "data = {\n",
        "    'text': [\n",
        "        'The government passed a new health care law.',\n",
        "        'Aliens have landed in New York City!',\n",
        "        'Scientists discovered a new planet in the solar system.',\n",
        "        'Celebrity caught in a fake scandal for publicity.',\n",
        "        'NASA confirms water on the moon.',\n",
        "        'You can win $1 million by clicking this link.',\n",
        "    ],\n",
        "    'label': ['REAL', 'FAKE', 'REAL', 'FAKE', 'REAL', 'FAKE']\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "df.to_csv('fake_or_real_news.csv', index=False)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Step 2: Import required libraries\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "# Step 3: Load the dataset\n",
        "df = pd.read_csv(\"fake_or_real_news.csv\")\n",
        "\n",
        "# Step 4: Preprocess (basic clean)\n",
        "df['text'] = df['text'].astype(str).str.lower().str.replace(r'[^\\w\\s]', '', regex=True)\n",
        "\n",
        "# Step 5: Split dataset\n",
        "X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)\n",
        "\n",
        "# Step 6: TF-IDF Conversion\n",
        "vectorizer = TfidfVectorizer(stop_words='english')\n",
        "X_train_vec = vectorizer.fit_transform(X_train)\n",
        "X_test_vec = vectorizer.transform(X_test)\n",
        "\n",
        "# Step 7: Train the model\n",
        "model = LogisticRegression()\n",
        "model.fit(X_train_vec, y_train)\n",
        "\n",
        "# Step 8: Prediction function\n",
        "def predict_news(news):\n",
        "    news = news.lower()\n",
        "    news_vec = vectorizer.transform([news])\n",
        "    return model.predict(news_vec)[0]\n",
        "\n",
        "\n",
        "sample_news = \"Scientists find a new cure for cancer.\"\n",
        "result = predict_news(sample_news)\n",
        "print(\"Prediction:\", result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6dcbv3zJNJNR",
        "outputId": "80dcfa99-3f1f-42e1-cd35-2cf3ff847d9e"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Prediction: REAL\n"
          ]
        }
      ]
    }
  ]
}
