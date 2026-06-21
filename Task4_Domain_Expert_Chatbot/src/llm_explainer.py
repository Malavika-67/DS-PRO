from langchain_community.llms import Ollama

llm = Ollama(
    model="gemma:2b"
)


def generate_answer(
    query,
    context,
    history=""
):

    context = context[:12000]

    prompt = f"""
You are an expert Computer Science Research Assistant.

Use ONLY the information from the research papers provided below.

Research Papers:
{context}

Conversation History:
{history}

User Question:
{query}

Instructions:

- Give a direct answer first.
- Use bullet points where appropriate.
- Compare methods if comparison is requested.
- Mention advantages and limitations.
- Mention datasets only if actually found.
- Mention performance metrics only if actually found.
- Do NOT invent information.
- If information is unavailable, clearly say so.
- Keep the answer concise and professional.

Answer:
"""

    try:
        return llm.invoke(prompt)

    except Exception as e:
        return str(e)


def summarize_text(text):

    prompt = f"""
Summarize the following research abstract.

Provide:

1. Research Objective
2. Methodology
3. Key Results
4. Significance

Abstract:
{text[:2500]}

Summary:
"""

    try:
        return llm.invoke(prompt)

    except Exception as e:
        return str(e)


def explain_concept(
    concept,
    context=""
):

    prompt = f"""
Explain the following Computer Science concept.

Concept:
{concept}

Context:
{context}

Provide:

- Definition
- How it works
- Advantages
- Limitations
- Applications

Explanation:
"""

    try:
        return llm.invoke(prompt)

    except Exception as e:
        return str(e)