# Multi-Modal AI Assistant

## Overview

The Multi-Modal AI Assistant is an intelligent image understanding system that combines computer vision, optical character recognition (OCR), contextual reasoning, and conversational memory to analyze images and answer user queries.

Unlike traditional image captioning applications, this assistant performs multi-modal reasoning by extracting visual information from images, maintaining conversational context across interactions, validating responses using extracted evidence, and providing explainable answers supported by visual facts.

The system is implemented using Streamlit and integrates image captioning, OCR, color analysis, contextual reasoning, and evidence-based response generation into a single interactive application.

---

## Features

### Image Understanding

* Automatic image caption generation using BLIP (Bootstrapping Language-Image Pre-training).
* Visual scene interpretation and object description.

### OCR Text Extraction

* Extracts text from uploaded images using EasyOCR.
* Supports reading text from posters, cards, banners, documents, and signs.

### Color Analysis

* Detects dominant colors present in uploaded images.
* Provides visual insights beyond image captions.

### Context-Aware Conversation

* Maintains chat history during the session.
* Supports follow-up questions based on previous interactions.

### Evidence-Based Responses

* Generates answers supported by:

  * Image captions
  * OCR results
  * Detected visual features
* Displays supporting evidence for transparency.

### Ambiguity Handling

* Interprets references such as:

  * "it"
  * "tell me more about it"
  * "that object"
* Uses previous conversation context to resolve ambiguity.

### Response Validation

* Verifies the availability of visual evidence before generating responses.
* Prevents unsupported conclusions.

### Explainable AI

* Displays reasoning steps used to generate answers.
* Improves transparency and user trust.

---

## System Architecture

Image Upload
↓
Image Captioning (BLIP)
↓
OCR Text Extraction (EasyOCR)
↓
Dominant Color Detection
↓
Visual Fact Extraction
↓
Context Memory
↓
Reasoning Engine
↓
Evidence Validation
↓
Response Generation

---

## Technologies Used

* Python 3.x
* Streamlit
* Transformers (Hugging Face)
* BLIP Image Captioning Model
* EasyOCR
* NumPy
* Pillow

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd MultiModal_AI_Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run chatbot.py
```

The application will open automatically in your browser.

---

## Usage

### Step 1

Upload an image in JPG, JPEG, or PNG format.

### Step 2

Click **Analyze Image**.

The system will:

* Generate an image caption.
* Extract text from the image.
* Detect dominant colors.
* Store visual facts for reasoning.

### Step 3

Ask questions related to the uploaded image.

---

## Example Questions

### Image Understanding

* Describe the image.
* What is shown in the image?
* What objects are visible?

### OCR

* Read the text from the image.
* What text is present?
* Is there any writing?

### Color Analysis

* What colors are visible?
* What are the dominant colors?

### Evidence-Based Reasoning

* Why do you think that?
* What evidence supports your answer?
* Explain your conclusion.

### Context Awareness

* Tell me more about it.
* What did we discuss earlier?

---

## Project Highlights

* Multi-modal AI system combining vision and language.
* Context-aware conversational interaction.
* Evidence-based answer generation.
* Explainable reasoning process.
* OCR-powered text understanding.
* Visual feature extraction and analysis.

---

## Future Enhancements

* Object Detection using YOLO.
* Visual Question Answering (VQA).
* Vector-based long-term memory.
* Multi-language OCR support.
* Speech input and voice responses.
* Advanced scene understanding.

---


## Author

Malavika Raj B S

