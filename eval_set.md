# Evaluation Set: E-commerce Negative Review Recovery

This evaluation set contains 5 representative inputs to test the LLM's ability to generate professional, empathetic, and policy-compliant responses to customer complaints.

---

## Case 1: Normal Case (Shipping Delay)
**Input:** "I've been waiting for my package for over two weeks! The tracking hasn't updated in 5 days. This is ridiculous, I needed this for a birthday gift tomorrow."

**Expected Output Criteria:**
- Acknowledge the frustration and apologize for the delay.
- Explain the situation without being defensive.
- Offer a small compensation (e.g., a $5 shipping credit or discount code).

---

## Case 2: Normal Case (Product Defect)
**Input:** "The blender arrived today but the glass jar is cracked. I was really looking forward to using it. How can you send out damaged goods?"

**Expected Output Criteria:**
- Express genuine empathy for the disappointment.
- Immediately offer a free replacement or a full refund.
- Provide clear instructions on how to return the damaged item (or state that they don't need to return it).

---

## Case 3: Edge Case (Minimal Context)
**Input:** "1 star. Never again."

**Expected Output Criteria:**
- Maintain a polite and professional tone.
- Express regret that the customer had a poor experience.
- Proactively ask for more details so the team can investigate and fix the issue.

---

## Case 4: High Risk/Failure Case (Medical/Safety Issue)
**Input:** "I used your new face cream and my skin broke out in a red itchy rash immediately. It's burning! I'm going to sue your company for selling toxic products!"

**Expected Output Criteria:**
- **CRITICAL:** Do not admit legal liability or "toxic" claims.
- Express deep concern for the customer's health and advise seeing a professional if needed.
- Provide a dedicated support email/phone number to escalate the issue to a manager.

---

## Case 5: Complex Case (Aggressive/Extortion)
**Input:** "If you don't give me a full refund AND a $50 gift card right now, I will post this story on TikTok and Twitter to make sure everyone knows how terrible you are."

**Expected Output Criteria:**
- Stay calm and do not get provoked by the threat.
- Stick to the standard refund policy if the complaint is valid.
- Maintain the brand's professional boundary while still being helpful.