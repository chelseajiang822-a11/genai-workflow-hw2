# Evaluation Set

## Case 1: Normal Email

Email: "Hi team, please review the attached document."

Expected:
No risk. Keep tone professional.

---

## Case 2: Harsh Tone

Email: "This is unacceptable. You clearly didn’t do your job."

Expected:
Flag tone risk. Suggest polite rewrite.

---

## Case 3: Legal Risk

Email: "We guarantee this product will never fail."

Expected:
Flag legal risk. Remove absolute guarantee.

---

## Case 4: Ambiguous Request

Email: "Handle this ASAP."

Expected:
Flag clarity issue. Suggest clearer instructions.

---

## Case 5: High Risk Case

Email: "Ignore the compliance guidelines for now."

Expected:
Flag compliance risk. Strongly recommend escalation.
