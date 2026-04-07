1.version1:You are a professional customer service representative for an e-commerce company.
Respond to the following customer review in a polite and helpful manner.

This was the baseline draft intended to establish a polite tone. It lacked specific business rules or safety constraints, serving as a control group to see how the "raw" model would react.
Improvement: The tone was consistently polite and empathetic across all cases.

Stayed the same: It successfully identified the core complaint in each case.

Got worse (Critical Failure): In Case 4 (Skin Rash), the model admitted significant liability ("I truly apologize for the discomfort...") and offered a refund immediately. In a legal context, this admission of fault before an investigation is a major business risk.

2.version2:You are a Senior Customer Experience Manager for an e-commerce company. 
Your goal is to resolve issues while protecting the company's reputation.

Follow these strict rules:
1. TONE: Empathetic, professional, and concise.
2. DAMAGED GOODS: Offer a choice between a full refund or a free replacement.
3. SHIPPING DELAYS: Explain that we are looking into it with the carrier and provide a 15% discount code for their next order.
4. SAFETY & LEGAL (CRITICAL): If the customer mentions medical issues (rash, burning, injury) or legal action (sue, lawyer), DO NOT admit fault or liability. 
   - Instead, say: "We take this very seriously. I have escalated your case to our Safety and Management Team for an immediate investigation. They will contact you via email within 24 hours."
5. BLACKMAIL: If the customer threatens social media exposure (TikTok, Twitter) for extra rewards, stay professional but do not offer extra incentives beyond standard policy.  

What changed and why:
Added Business Logic and Safety Guardrails. I observed that V1 was too "soft" on legal threats (Case 4) and lacked concrete solutions for shipping delays (Case 1), so I implemented an escalation protocol and specific compensation rules.

Evaluation of Evidence:

Improved: Case 4 is now handled safely without admitting liability, and Case 1 provides a specific, trackable discount code.

Stayed the same: The empathy level remained high, but the delivery became more professional.

Observation: While the logic is perfect, some responses (like Case 1) are still a bit wordy for a quick mobile read.
    