import gradio as gr
from transformers import pipeline

# Load translation model
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-ROMANCE"
)

def translate_text(text):
    if not text.strip():
        return ""

    try:
        result = translator(text)
        return result[0]["translation_text"]
    except Exception as e:
        return f"Error: {str(e)}"

custom_css = """
body {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
"""

with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:

    gr.Markdown("""
    <div class="main-title">
        ISHOWSHAUN
    </div>

    <div class="sub-title">
        🌍 AI Language Translator
    </div>
    """)

    input_text = gr.Textbox(
        label="Enter Text",
        lines=6,
        placeholder="Type something..."
    )

    translate_btn = gr.Button("🚀 Translate")

    output_text = gr.Textbox(
        label="Translated Text",
        lines=6
    )

    translate_btn.click(
        fn=translate_text,
        inputs=input_text,
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
