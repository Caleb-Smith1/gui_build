OpenAI Prompt GUI App

This application allows a user to type a prompt into a text box, submit it, and receive a response from OpenAI’s GPT-3.5 model. The output is displayed in a scrollable box below the prompt.

---

🔧 How to Set Up

1. Install the required Python packages:

   pip install openai python-dotenv

2. Create a file named `.env` in the same folder as `app.py`.

3. Paste your OpenAI API key into the `.env` file like this:

   OPENAI_API_KEY=your-api-key-here

   Replace `your-api-key-here` with your actual key from:
   https://platform.openai.com/account/api-keys

4. Make sure `.env` is saved with no quotes, no spaces, and no extra lines.

---

▶️ How to Run

1. Open your terminal in the project folder.
2. Run the application:

   python app.py

3. Type a prompt in the input box and click "Submit".
4. The AI's response will appear in the output box.

---

🔐 Note

The `.env` file is listed in `.gitignore` to keep your API key private and safe from being uploaded to GitHub.
