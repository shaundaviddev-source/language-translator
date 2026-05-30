import os
import gradio as gr
from deep_translator import GoogleTranslator

LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

def translate_text(text, source_lang, target_lang):
    if not text.strip():
        return ""

    try:
        translated = GoogleTranslator(
            source=LANGUAGES[source_lang],
            target=LANGUAGES[target_lang]
        ).translate(text)

        return translated

    except Exception as e:
        return f"Translation Error: {e}"

def swap_languages(src, tgt):
    return tgt, src

custom_css = """
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    font-size: 20px;
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

    with gr.Row():
        source_lang = gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="English",
            label="Source Language"
        )

        target_lang = gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="Tamil",
            label="Target Language"
        )

    swap_btn = gr.Button("🔄 Swap Languages")

    input_text = gr.Textbox(
        label="Input Text",
        lines=6,
        placeholder="Enter text..."
    )

    translate_btn = gr.Button("🚀 Translate")

    output_text = gr.Textbox(
        label="Translated Text",
        lines=6
    )

    translate_btn.click(
        translate_text,
        inputs=[input_text, source_lang, target_lang],
        outputs=output_text
    )

    swap_btn.click(
        swap_languages,
        inputs=[source_lang, target_lang],
        outputs=[source_lang, target_lang]
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )
