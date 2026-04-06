# GenAI Workflow Report: Business Email Risk Assistant

## 1. Business Use Case

**Problem Statement:** In professional communication, employees often send emails that contain unintended negative tones, potential legal liabilities (such as making unrealistic guarantees), or compliance violations. These errors can damage client relationships, lead to HR disputes, or create legal risks for the company.
**Solution:** The "Business Email Risk Assistant" acts as an automated safety layer. It analyzes outgoing drafts to identify specific risk categories and provides a professional rewrite, ensuring that every communication aligns with corporate standards and legal safety.

## 2. Model Selection

**Model Chosen:** `gemini-1.5-flash`
**Reasoning:** I chose this model because it offers the best balance between speed (latency) and reasoning capability for text analysis. During development, I initially observed that `gemini-1.5-flash` was significantly faster at processing the 5-case evaluation set compared to larger models, while still maintaining high accuracy in identifying subtle tone shifts. Although I briefly tested `gemini-pro`, the 1.5 Flash version was more robust in handling the specific system instructions I provided.

## 3. Methodology & Prompt Iteration

I improved the system through two key iterations to enhance its reliability and output quality:

* **Baseline Design:** The initial prompt focused on basic risk identification and rewriting. It often provided overly polite rewrites but failed to emphasize the severity of compliance issues or provide a clear risk hierarchy.
* **Final Design:** In the final iteration, I updated the prompt to include a mandatory **[Risk Level] (Low, Medium, High)** indicator and forced the model to use a more critical lens for corporate policy.
* **Improvement Observed:** In the final version, the model correctly flagged the request to "ignore compliance" as **High Risk**, whereas the baseline merely tried to make the request sound "nicer." The addition of the Risk Level allows users to quickly prioritize which emails need the most attention.

## 4. Evaluation Results

The results are in app.py.

## 5. System Limitations & Human Review

Despite its effectiveness, the prototype still has limitations, particularly with **deeply nested sarcasm** or **industry-specific jargon** that falls outside its general training data. For instance, it might misinterpret "inside jokes" between long-term colleagues as professional risks.

**Human Review Requirement:** The system is designed to assist, not replace, human judgment. Any email flagged as **"High Risk"** (especially in Legal or Compliance categories) must be blocked from sending automatically and routed to a manager or legal representative for manual sign-off.

## 6. Deployment Recommendation

**Recommendation:** I recommend deploying this workflow as an **Internal Assistive Tool (Co-pilot)** rather than a fully automated gatekeeper.

**Conditions for Deployment:**
1.**User-in-the-loop:** The system should present the "Rewrite" as a suggestion that the employee must manually review and accept before the email is sent
2. **RAG Integration:** Future versions should be connected to a company-specific compliance handbook via Retrieval-Augmented Generation (RAG) to improve accuracy regarding internal policies.
3. **Auditing:** A weekly log of flagged high-risk communications should be audited by HR to determine if certain departments need additional professional communication training.
