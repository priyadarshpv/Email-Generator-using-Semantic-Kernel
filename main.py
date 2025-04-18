import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.hugging_face import HuggingFaceTextCompletion
from semantic_kernel.functions import KernelFunction, KernelArguments

# Replace with your Hugging Face API key
api_key = "hf_YOUR_API_KEY"
model_id = "google/flan-t5-large"
service_id = "huggingface_textgen"

# Initialize Kernel
kernel = sk.Kernel()
ai_service = HuggingFaceTextCompletion(
    service_id=service_id,
    ai_model_id=model_id,
    task="text2text-generation"
)
kernel.add_service(ai_service)

# Prompt Template
prompt_template = """
Objective: Write a professional email draft based on the provided details.

Details:
- Recipient Style/Tone: {{$recipient_style}}
- Email Topic: {{$topic}}
- Key Point: {{$main_point}}

Instructions:
1. Generate a clear Subject line.
2. Write a concise email body.
3. Use the specified tone and include the key point.
4. End with a standard closing (e.g., "Best regards").

--- EMAIL DRAFT ---
Subject:
"""

# Define Function
email_generator = KernelFunction.from_prompt(
    function_name="EmailGenerator",
    plugin_name="EmailPlugin",
    prompt=prompt_template
)
kernel.add_function(email_generator)

# Input Parameters
recipient_style = "formal and friendly"
topic = "Project Update & Deadline Reminder"
main_point = "Please remember the report submission deadline is this Friday, April 11th, 2025."

arguments = KernelArguments(
    recipient_style=recipient_style,
    topic=topic,
    main_point=main_point
)

# Asynchronous Email Generation
async def generate_email():
    result = await kernel.invoke(email_generator, arguments=arguments)
    print("Generated Email:")
    print("------------------")
    print(str(result).strip())

# Run Script
if __name__ == "__main__":
    asyncio.run(generate_email())
