import gradio as gr

def reset_env():
    return {"status": "ok"}

demo = gr.Interface(
    fn=reset_env,
    inputs=[],
    outputs="json",
    allow_flagging="never"
)

demo.launch()