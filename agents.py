import openai
import re
from bs4 import BeautifulSoup
import streamlit as st


class ContentGenerationAgent:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_content(self, topic):
        content = []
        # SEO keywords
        keywords = ["HR", "Human Resources", "Employee Engagement", "HR Trends", "Workplace Diversity", "Employee Wellness"]

     
        prompt = f"Write a comprehensive blog post on the topic: {topic}. Include relevant SEO keywords such as: {', '.join(keywords)}. The content should be detailed, informative, and structured with headings, subheadings, and a clear introduction and conclusion. The tone should be professional and suitable for a corporate audience."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful SEO content writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000  
        )

        content_text = response['choices'][0]['message']['content'].strip()
        return content_text

# SEO Optimization Agent: 
class SEOOptimizationAgent:
    def optimize_content(self, content):
        # Define target SEO keywords
        keywords = ["HR", "Human Resources", "Employee Engagement", "HR Trends", "Workplace Diversity", "Employee Wellness"]
        
        optimized_content = self._optimize_keywords(content, keywords)
        optimized_content = self._add_seo_headings(optimized_content)
        optimized_content = self._highlight_key_points(optimized_content)
        optimized_content = self._format_for_seo(optimized_content)

        return optimized_content

    def _optimize_keywords(self, text, keywords):
        for keyword in keywords:
           
            text = re.sub(rf"\b({keyword})\b", r"\1 (key HR term)", text, flags=re.IGNORECASE)
        return text

    def _add_seo_headings(self, text):
        # Add headings
        text = re.sub(r'(##\s*[^<]+)', r'<h2>\1</h2>', text)
        return text

    def _highlight_key_points(self, text):
        
        keywords = ["Employee Engagement", "HR Trends", "Employee Wellness", "Diversity and Inclusion"]
        for keyword in keywords:
            text = re.sub(rf"\b({keyword})\b", r"<strong>\1</strong>", text)
        return text

    def _format_for_seo(self, text):
        
        soup = BeautifulSoup(text, "html.parser")
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            paragraph.insert_before("<p>")
            paragraph.insert_after("</p>")
        return str(soup)


def main():
    st.set_page_config(page_title="SEO Blog Generator", page_icon="📚", layout="wide")
    
    st.title("SEO Blog Generator")
    st.write("Enter a topic to generate a comprehensive, SEO-optimized blog post.")


    topic = st.text_input("Enter the blog topic:")

    if topic:
        openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
        
        if openai_api_key:
            generation_agent = ContentGenerationAgent(openai_api_key)
            seo_agent = SEOOptimizationAgent()

            content = generation_agent.generate_content(topic)

            seo_content = seo_agent.optimize_content(content)

            st.subheader("Generated SEO-Optimized Blog Content:")
            st.markdown(seo_content, unsafe_allow_html=True)  

            st.download_button(
                label="Download Blog Content as .txt file",
                data=seo_content,
                file_name=f"{topic.replace(' ', '_')}_blog.txt",
                mime="text/plain"
            )


if __name__ == "__main__":
    main()
