import google.generativeai as genai

genai.configure(api_key="AIzaSyCxD8S5wOUU_fsVkAlvDOiWvcismrIzPfk")

SYSTEM_INSTRUCTION = "You are a Business Email Risk Assistant.\n" + \
                     "Analyze the input email for:\n" + \
                     "1. Risk Assessment\n" + \
                     "2. Risk Type (Tone, Legal, Compliance, Clarity)\n" + \
                     "3. Suggested Rewrite\n\n" + \
                     "Format output as:\n" + \
                     "[Assessment]: \n[Type]: \n[Rewrite]:\n" + \
                     "[Risk Level]: \n"

def run_workflow(email_text):
    
    model_names = ["models/gemini-1.5-flash", "models/gemini-pro", "gemini-1.5-flash"]
    
    for name in model_names:
        try:
            model = genai.GenerativeModel(
                model_name=name,
                system_instruction=SYSTEM_INSTRUCTION
            )
            response = model.generate_content(email_text)
            return response.text
        except Exception:
            continue 
            
    return "All model names have failed attempts. Please check the API Key permissions or network."

if __name__ == "__main__":
    # 3. evaluation
    eval_set = [
        "Hi team, please review the attached document.",
        "This is unacceptable. You clearly didn’t do your job.",
        "We guarantee this product will never fail.",
        "Handle this ASAP.",
        "Ignore the compliance guidelines for now."
    ]

    print("--- Automated Testing Started ---\n")

    for email in eval_set:
        print(f"Input Email: {email}")
        try:
            result = run_workflow(email)
            print(f"Model Output:\n{result}")
        except Exception as e:
            print(f"Error occurred: {e}")
        print("-" * 30)