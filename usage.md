# Using SOWA

Welcome to the Advanced Textbook Q&A System! This guide will walk you through the process of using our system to upload textbooks, ask questions, and interpret the results.

## Table of Contents

1. [Starting the Application](#starting-the-application)
2. [Uploading Textbooks](#uploading-textbooks)
3. [Asking Questions](#asking-questions)
4. [Interpreting Results](#interpreting-results)
5. [Tips for Effective Querying](#tips-for-effective-querying)
6. [Troubleshooting](#troubleshooting)

## Starting the Application

1. Ensure you've completed all steps in the [SETUP.md](SETUP.md) file.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   ```bash
   cd /path/to/project
   ```
4. Start the application by running:
   ```bash
   
   streamlit run app.py
   ```
5. Open the system in your web browser at the URL provided in the terminal (e.g., http://localhost:5000).
6. **Uploading Textbooks**
   - Once the application is running, click the Upload button on the main dashboard.
   - Select your textbook file in PDF format from your computer.
   - Click Submit to upload the file.
   - Wait for the system to process the textbook. A confirmation message will appear once the upload is successful.

7. **Asking Questions**
   - Navigate to the Ask a Question tab.
   - Type your question in the input box. For example:
      1. "What is the definition of photosynthesis?"
      2. "Explain the differences between meiosis and mitosis."

8. Click the Submit button to process your question.

9. **Interpreting Results**
   The response will be displayed in the Results section.
   Each answer includes:
   - Direct Answer: A concise response to your question.
   - Relevant Text: Extracted sections from the textbook that support the answer.
   - References: Page numbers or sections where the information was found (if available).
   - If the answer is incomplete or unclear, refine your question and try again.

## Tips for Effective Querying
1. Use clear and specific language for your questions.
2. Instead of "Explain this concept," ask "What is the function of chloroplasts?"
3. Avoid overly broad or vague questions.
4. For example, "Tell me about biology" is less effective than "What are the main types of cells in biology?"
5. If you encounter unsatisfactory results, rephrase or break down your question into smaller parts.

## Troubleshooting
1. Issue: Unable to Start the Application
   - Ensure all dependencies are installed as per SETUP.md.
   - Verify that your Python version meets the requirements.
   - Check for errors in the terminal and resolve them accordingly.
2. Issue: Textbook Upload Fails
   - Ensure the file is in PDF format and below the maximum size limit specified in SETUP.md.
   - Check your internet connection if using a remote server.
3. Issue: Answers are Incorrect or Incomplete
   - Ensure the textbook contains information relevant to your question.
   - Try rephrasing your question for clarity.
   - Check the Relevant Text section for context and verify against your textbook.
4. Issue: System Crashes or Freezes
   - Restart the application and try again.
   - Check for errors in the terminal log.
 