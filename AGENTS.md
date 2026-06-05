# AGENTS.md

## Project Overview

This repository supports a summer school in France for political scientists and sociologists who are learning how to use Large Language Models (LLMs) in social science research.

The audience consists primarily of researchers, PhD students, and advanced master's students with varying levels of programming experience. Many participants will be new to Python and notebook-based workflows.

The course is delivered by multiple instructors. Different instructors are responsible for different half-day sessions. Materials should therefore be modular, self-contained, and easy to hand over between teaching teams.

## Core Principle

This repository is designed for teaching social scientists how to use LLMs in research.

Pedagogical clarity, methodological rigor, accessibility, and hands-on learning are more important than technical sophistication.

When in doubt, prioritize understanding, reproducibility, and critical thinking over advanced engineering techniques.

---

## Audience Assumptions

Assume participants are:

* Political scientists
* Sociologists
* PhD students
* Researchers
* Advanced master's students

Do not assume prior knowledge of:

* Python
* APIs
* Software engineering
* Machine learning
* Command-line tools

Explain technical concepts when first introduced.

---

## Language Policy

This summer school is delivered in French.

### Explanatory Content

All pedagogical content intended for participants must be written in French, including:

* Notebook introductions
* Learning objectives
* Section titles
* Explanatory markdown cells
* Exercise instructions
* Discussion questions
* Methodological notes
* Conclusions and summaries
* Error explanations intended for learners

Use clear academic French appropriate for social science researchers.

### Code

Code should remain in English whenever possible:

* Variable names
* Function names
* Class names
* File names
* Package names
* API parameters

Example:

```python
speech_df = pd.read_csv("speeches.csv")

sentiment_scores = analyze_sentiment(speech_df["text"])
```

Preferred over:

```python
discours_df = pd.read_csv("discours.csv")

scores_sentiment = analyser_sentiment(discours_df["texte"])
```

### Comments Inside Code

Short technical comments may be written in English.

When comments are pedagogical and intended to explain concepts to participants, French is preferred.

### Generated Notebooks

For all notebooks:

* Markdown cells → French
* Python code → English
* Variable names → English
* Function names → English
* Charts and figure titles → French unless there is a specific reason to use English
* Exercise statements → French
* Research interpretation and discussion → French

---

## Educational Goals

Participants should learn:

1. Basic concepts behind LLMs.
2. Prompt engineering and interaction design.
3. Using LLMs from Python.
4. Working with APIs and hosted models.
5. Text analysis workflows relevant to social science research.
6. Reproducible research practices.
7. Critical evaluation of LLM outputs.
8. Ethical, legal, and methodological considerations.

The emphasis is on practical research applications rather than machine learning engineering.

---

## Scope

This course teaches the use of LLMs in social science research.

It does not focus on:

* Training foundation models
* Deep learning engineering
* Neural network implementation
* GPU optimization
* MLOps
* Large-scale deployment

Use the simplest technical explanation compatible with the learning objectives.

---

## Technical Environment

Primary environment:

* Google Colab
* Jupyter Notebooks (.ipynb)
* Python 3.x

Assume participants can run notebooks in Google Colab without local installation.

Prefer libraries that install easily in Colab.

Common libraries may include:

* pandas
* numpy
* matplotlib
* scikit-learn
* statsmodels
* requests
* openai
* google-generativeai
* transformers

Avoid requiring GPUs unless explicitly needed.

---

## Colab-First Development

All materials should run in Google Colab.

Avoid:

* Local file path assumptions
* Docker
* Conda environments
* Complex installation procedures
* Local servers

Prefer:

* pip install in notebook cells
* Public datasets
* Self-contained examples
* Simple authentication workflows

Each notebook should be independently runnable.

---

## API Credentials

Never hardcode API keys.

When demonstrating API usage:

* Use environment variables
* Use Colab Secrets when appropriate
* Provide placeholder examples
* Explain security best practices

Example:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

---

## Repository Structure

Suggested structure:

```text
notebooks/
  01_am_introduction/
  01_pm_prompting/
  02_am_apis/
  02_pm_text_analysis/
  03_am_research_application/
  ...

data/
  sample_data/
```

---

## Notebook Header

Every notebook should begin with:

* Session title
* Instructor name(s)
* Estimated duration
* Learning objectives
* Required prerequisites
* Required packages

This facilitates collaboration across instructors.

---

## Notebook Design Principles

When creating or modifying notebooks:

* Begin with learning objectives.
* Explain concepts before code.
* Keep cells short and readable.
* Include comments where useful.
* Prefer reproducibility over optimization.
* Minimize setup complexity.
* Include expected outputs when useful.
* Use markdown extensively.
* End major sections with a short summary.

Assume readers are social scientists, not software engineers.

---

## Active Learning and Hack-Time

This summer school is highly interactive.

Notebooks should regularly alternate between:

1. Explanation
2. Demonstration
3. Hack-time exercise
4. Group discussion

Avoid long sequences of passive content.

Participants should frequently modify code, test prompts, inspect outputs, and discuss results.

---

## Hack-Time Sections

Each notebook should contain multiple short "Hack-Time" sections.

A typical hack-time exercise should:

* Take 5–15 minutes
* Focus on a single concept
* Require modifying existing code rather than writing everything from scratch
* Encourage experimentation
* Produce a visible result
* Be feasible for beginners

Use the following structure:

```markdown
### Hack-Time

Description courte de l'activité, instructions...

**Défi optionnel**

Extension pour les participants plus rapides.
```

---

## Types of Hack-Time Activities

### Technical Exploration

Participants interact with code.

Examples:

* Modify a prompt
* Change model parameters
* Analyze a new dataset
* Test alternative workflows
* Compare model outputs

### Research Reflection

Participants critically evaluate results.

Examples:

* Identify hallucinations
* Discuss bias
* Compare coding strategies
* Assess validity
* Assess reproducibility
* Discuss ethical implications

---

## Notebook Rhythm

As a general rule:

* Introduce a concept.
* Demonstrate it.
* Include a hack-time activity within the next 10–20 minutes of instruction.

Avoid notebooks that contain more than 20 minutes of teaching material without an interactive activity.

Every major concept should be followed by a short hands-on exercise that allows participants to experiment with the technique and reflect on its implications for social science research.

---

## Teaching Style

Explanations should:

* Use plain language.
* Avoid unnecessary technical jargon.
* Connect examples to political science and sociology.
* Explain why a method is useful for research.
* Highlight limitations and sources of bias.
* Encourage critical interpretation of results.
* Explicitly discuss methodological trade-offs.

---

## Methodological Orientation

LLMs should be presented as research tools, not sources of truth.

Every substantive use of an LLM should discuss:

* Reliability
* Validity
* Reproducibility
* Bias
* Transparency
* Research ethics

Whenever possible, connect computational methods to established social science research practices.

---

## Preferred Research Examples

Whenever possible, use examples relevant to French and European social science research:

* Assemblée nationale debates
* Sénat debates
* Political manifestos
* Election campaigns
* Public consultations
* Policy documents
* Survey responses
* Interview transcripts
* Press articles
* Social media discussions

International examples may be used when pedagogically useful.

Avoid examples that require sensitive personal data.

---

## Code Standards

* Write clear and readable Python.
* Favor explicitness over cleverness.
* Use descriptive variable names.
* Include docstrings for reusable functions.
* Avoid excessive abstraction.
* Prefer notebook-friendly code.

Code should support learning rather than demonstrate advanced software engineering practices.

---

## Data Handling

When using datasets:

* Use small demonstration datasets when possible.
* Respect privacy and ethical constraints.
* Avoid distributing restricted data.
* Clearly document data sources.
* Prefer open and reproducible datasets.

---

## LLM Usage Guidelines

When demonstrating LLMs:

* Show prompts explicitly.
* Explain model parameters when relevant.
* Discuss reproducibility limitations.
* Demonstrate output validation.
* Compare outputs across prompts when useful.
* Emphasize that LLM outputs may contain errors or hallucinations.

Participants should learn both the capabilities and limitations of LLM-based research workflows.

---

## Collaboration Across Instructors

Because multiple instructors contribute:

* Keep materials modular.
* Avoid dependencies between sessions when possible.
* Clearly document assumptions.
* Maintain consistent naming conventions.
* Include a brief instructor note at the top of each notebook.
* Make handoffs between sessions explicit.

Assume another instructor may need to teach from your notebook with little prior preparation.

---

## Desired Output Style

When generating educational content:

* Prioritize clarity over completeness.
* Provide step-by-step explanations.
* Include short summaries.
* Use markdown extensively.
* Balance conceptual understanding and practical exercises.
* Encourage active participation.
* Encourage critical reflection.

The primary objective is to help social scientists become informed, critical, and effective users of LLMs in research workflows.

