# SEO Blog Generator

This project is a **SEO Blog Generator** built with **Streamlit** and **OpenAI's GPT-3.5**. The application generates SEO-optimized blog posts on a topic provided by the user. The generated blog includes key sections like **headings**, **subheadings**, and **SEO keywords**. Additionally, it highlights important keywords in the content to ensure SEO optimization.

## Features
- **Model Selection**: The user can choose between **GPT-3.5** (free) and **GPT-4** (paid) models to generate content.
- **SEO Optimization**: The generated content is optimized with relevant keywords such as **HR**, **Human Resources**, **Employee Engagement**, etc.
- **Highlighting Key Points**: Important concepts such as **Employee Engagement** and **HR Trends** are bolded in the generated content for better readability.
- **Formatted Content**: The content is well-structured with **headings** (`<h2>`), **bolded** key points, and SEO-friendly formatting.
- **Downloadable Content**: The user can download the SEO-optimized content as a `.txt` file.

## Installation and Setup

### Prerequisites
- Python 3.7 or later.
- **OpenAI API Key** for generating content with GPT-3.5 and GPT-4. You can generate the API key by signing up on [OpenAI's website](https://beta.openai.com/signup/).

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Suriyaprakash2023/abex.git
cd abex
```

### Step 2: Install Dependencies
``` bash
pip install -r requirements.txt
```
### Step 3: Run the App

Once you've installed the dependencies and set up your OpenAI API key, run the app using Streamlit:

```bash
streamlit run agents.py
```
The app should be available at http://localhost:8501 in your web browser.


## How to Use the App:
 ### 1. Enter a Blog Topic

- In the input field labeled "Enter the blog topic:", type the topic for which you want to generate the SEO-optimized blog post. For example, you can type:
"The Role of AI in Transforming Human Resources"

### 2. Enter Your OpenAI API Key
- If you select GPT-4 (a paid model), you will be prompted to enter your OpenAI API key.
- If you select GPT-3.5 (free), the app will generate content without needing the API key.

### 3. Generate Content
- Once you’ve provided the topic and API key (if required), click on "Generate Blog Content".
- The app will use OpenAI to generate a detailed, SEO-optimized blog post on the selected topic.

### 4. View the Generated Content
- After generating the content, the blog post will be displayed in the app, formatted with headings and important keywords bolded.

### 5. Download the Blog Content
- You can download the generated content as a .txt file by clicking the "Download Blog Content as .txt file" button.


## Code Explanation

- ContentGenerationAgent: This class is responsible for generating content using OpenAI's GPT-3.5 or GPT-4 model based on the user-provided topic.
- SEOOptimizationAgent: This class optimizes the generated content for SEO by integrating relevant keywords, adding headings, and formatting the content to be SEO-friendly.

- Streamlit UI: The user interface allows users to input a topic, select the model, and see the generated SEO-optimized content in real-time. Users can also download the content as a .txt file.