import gradio as gr

def run_project():
    return "Smart Toll Plaza Project is running successfully!"

demo = gr.Interface(
    fn=run_project,
    inputs=None,
    outputs="text",
    title="Smart Toll Plaza System"
)

demo.launch()