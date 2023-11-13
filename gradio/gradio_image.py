import gradio as gr

def predict_glaucoma(image):
    # Perform necessary preprocessing on the input image
    # Make predictions using the trained model
    # Return the prediction result
    # Let's assume predict_glaucoma returns a dictionary of class probabilities
    return {"Normal": 0.3, "Glaucoma": 0.7}

# Create a Gradio interface with example images
iface = gr.Interface(
    fn=predict_glaucoma,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=2),
    examples=["normal_eye.png", "glaucoma_eye.png"]
)

# Launch the interface -> will make it available at http://127.0.0.1:7860
iface.launch()