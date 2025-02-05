{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWEesqFEffWtydU6ywULo1",
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
        "<a href=\"https://colab.research.google.com/github/Udithreddy4/Codtech12/blob/main/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4gjKApDyeiIy",
        "outputId": "6b068c47-6fd6-4657-991f-4bafc243e927"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Summary:\n",
            "\n",
            "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Colloquially, the term \"artificial intelligence\" is often used to describe machines \n",
            "(or computers) that mimic \"cognitive\" functions that humans associate with the human mind, such as \"learning\" and \"problem solving\". Leading AI textbooks define the field as the study of \"intelligent agents\": any device that perceives its environment and takes actions that \n",
            "maximize its chance of successfully achieving its goals.\n",
            "\n",
            "Summary of empty article:\n",
            "\n"
          ]
        }
      ],
      "source": [
        "import nltk\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import word_tokenize, sent_tokenize\n",
        "from heapq import nlargest\n",
        "\n",
        "def summarize_article(article_text, num_sentences=5):\n",
        "    try:\n",
        "        # 1. Text Preprocessing\n",
        "        stop_words = set(stopwords.words('english'))\n",
        "        words = word_tokenize(article_text.lower())  # Tokenize and lowercase\n",
        "        sentences = sent_tokenize(article_text)  # Sentence tokenization\n",
        "\n",
        "        word_frequencies = {}\n",
        "        for word in words:\n",
        "            if word.isalnum() and word not in stop_words:  # Remove punctuation and stopwords\n",
        "                if word in word_frequencies:\n",
        "                    word_frequencies[word] += 1\n",
        "                else:\n",
        "                    word_frequencies[word] = 1\n",
        "\n",
        "        # 2. Sentence Scoring\n",
        "        sentence_scores = {}\n",
        "        for sentence in sentences:\n",
        "            for word in word_tokenize(sentence.lower()):\n",
        "                if word in word_frequencies:\n",
        "                    if sentence in sentence_scores:\n",
        "                        sentence_scores[sentence] += word_frequencies[word]\n",
        "                    else:\n",
        "                        sentence_scores[sentence] = word_frequencies[word]\n",
        "\n",
        "        # 3. Summary Generation\n",
        "        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)\n",
        "        summary = \" \".join(summary_sentences)\n",
        "        return summary\n",
        "\n",
        "    except LookupError as e:\n",
        "        required_resource = str(e).split(\"'\")[1]  # Extract missing resource name\n",
        "        return f\"Error: Required NLTK resource '{required_resource}' is missing.\\nPlease download it using: nltk.download('{required_resource}')\"\n",
        "    except Exception as e:  # Handle other potential errors\n",
        "        return f\"An error occurred: {e}\"\n",
        "\n",
        "# Insert article text\n",
        "article = \"\"\"\n",
        "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.\n",
        "Leading AI textbooks define the field as the study of \"intelligent agents\": any device that perceives its environment and takes actions that\n",
        "maximize its chance of successfully achieving its goals. Colloquially, the term \"artificial intelligence\" is often used to describe machines\n",
        "(or computers) that mimic \"cognitive\" functions that humans associate with the human mind, such as \"learning\" and \"problem solving\".\n",
        "There are different approaches to AI, such as rule-based systems, neural networks, and machine learning algorithms. AI is used in various\n",
        "fields including healthcare, automotive, finance, and entertainment. As technology advances, AI is expected to play an even greater role in\n",
        "shaping the future of various industries and our daily lives.\n",
        "\"\"\"\n",
        "\n",
        "# Get the summary of the article\n",
        "summary = summarize_article(article, 3)  # Get a 3-sentence summary\n",
        "print(\"Summary:\")\n",
        "print(summary)\n",
        "\n",
        "# Example of handling NLTK resource issue:\n",
        "# (Simulate a missing resource for testing)\n",
        "# nltk.download = lambda x: (_ for _ in ()).throw(LookupError(\"Resource 'punkt' not found.\"))  # Mock missing 'punkt'\n",
        "# summary = summarize_article(article)\n",
        "# print(summary)\n",
        "\n",
        "# Example of an empty article\n",
        "article_empty = \"\"\n",
        "summary_empty = summarize_article(article_empty)\n",
        "print(\"\\nSummary of empty article:\")\n",
        "print(summary_empty)\n"
      ]
    }
  ]
}