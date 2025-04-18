# Email Generator using Semantic Kernel (Hugging Face + FLAN-T5)

This project uses [Microsoft's Semantic Kernel](https://github.com/microsoft/semantic-kernel) with the `google/flan-t5-large` model from Hugging Face to generate professional email drafts based on structured input.

### 🔧 Features

- Uses a custom prompt to structure the email.
- Allows control over tone, topic, and main point.
- Integrates with Hugging Face for text generation.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/email-generator-sk.git
cd email-generator-sk
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Program

Make sure to replace the Hugging Face token with your own in `main.py`.

```bash
python main.py
```

---

## 📄 Example Output

```txt
Generated Email:
------------------
Subject: Reminder: Project Report Due This Friday

Dear Team,

I hope you're doing well. Just a reminder that the project report submission deadline is this Friday, April 11th, 2025. Please ensure all updates are included.

Best regards,
```

---

## 📦 Dependencies

- `semantic-kernel`
- `huggingface_hub`

---

## 🔑 API Key

You must have a valid Hugging Face token to run this. Get it from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

Then, replace the value of `api_key` in `main.py`.

---

## 📝 License

This project is licensed under the MIT License.
```
