# Text To Image Generator App 🖼️

This application allows you to generate images from text prompts using cutting-edge AI models. Simply enter a text prompt, and the app will create a beautiful image based on your input!

## How it works

1. **Input Prompt**: Enter a text prompt describing the image you want to generate.
2. **Generate Image**: Click the "Generate Image" button to initiate the image generation process.
3. **Image Generation**: The app sends your text prompt to a powerful AI model hosted by Hugging Face's Inference API. The model generates an image based on your prompt.
4. **Display Image**: Once the image is generated, it is displayed on the screen along with your original prompt.
5. **Image Saving**: The generated image is saved locally and can be downloaded or shared as needed.

## How to use

### Running the app locally

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install dependencies by running: `pip install -r requirements.txt`.
4. Run the Streamlit app using the command: `streamlit run main.py`.
5. Access the app in your web browser at `http://localhost:8501`.

### Docker containerization

1. Build the Docker image by running: `docker build -t text-to-image-app:latest .`
2. Run the Docker container with the command: `docker run -p 8501:8501 text-to-image-app:latest`

## Example

Suppose you enter the text prompt: "A serene sunset over the ocean with palm trees swaying gently in the breeze."

The app will generate an image that captures this scene, complete with vibrant colors and realistic details. You can then download or share the generated image to bring your imagination to life!

Enjoy creating stunning images from your text prompts with the Text To Image Generator App! ✨
