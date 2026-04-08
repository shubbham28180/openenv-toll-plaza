import gradio as gr

def reset_env():
    return {"status": "ok"}

demo = gr.Interface(
    fn=reset_env,
    inputs=None,
    outputs="json"
)

demo.launch(server_name="0.0.0.0", server_port=7860)