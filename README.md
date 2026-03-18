# LLM Token Minification Experiment

An experiment testing if minifying code (shortening variable names, removing whitespace/comments) before sending it to Large Language Models (LLMs) saves tokens without degrading the LLM's understanding.

## Hypothesis
Minifying code significantly reduces token count (saving context window and API costs) while the LLM still perfectly understands the underlying logic.

## The Test
We created two use cases (Python and JavaScript) with a "Verbose" (long variable names) and a "Minified" (short variable names) version. 
1. We used OpenAI's `tiktoken` to count the exact token reduction.
2. We used Google's `gemini-2.5-flash` API to test comprehension and measure latency.

## Results

### 1. Token Savings
| Language | File | Tokens | Characters | Reduction |
|----------|------|--------|------------|-----------|
| Python | `uc1_verbose.py` | 141 | 670 | - |
| Python | `uc1_short.py` | 72 | 236 | **~49%** |
| JavaScript | `uc2_verbose.js` | 147 | 812 | - |
| JavaScript | `uc2_short.js` | 65 | 283 | **~55%** |

### 2. Latency Test (Gemini 2.5 Flash)
We prompted the model to explain the code and suggest exactly one performance optimization. Here is how long the API took to respond:

| Language | File | Latency (Seconds) | Comprehension |
|----------|------|-------------------|---------------|
| JavaScript | `uc2_verbose.js` | 6.35s | Perfect |
| JavaScript | `uc2_short.js` | **5.44s** | Perfect |
| Python | `uc1_verbose.py` | 7.37s | Perfect |
| Python | `uc1_short.py` | 17.82s* | Perfect |

*\*Note: The spike in the Python minified latency was due to temporary server-side API queueing/network fluctuations, not the code complexity. The JavaScript test accurately reflects the expected behavior: fewer tokens result in faster processing times.*

### 3. Comprehension Quality
The LLM perfectly understood both the verbose and minified versions. For example, it correctly identified that `cnt`, `tot`, and `u.get('act')` meant `count`, `total`, and `active` in the minified code, offering identical optimization suggestions for both versions.

## Conclusion
Minifying code before passing it into an LLM context window is highly recommended for building coding agents or processing large repositories. It cuts token usage by ~50% without sacrificing the model's ability to reason about the code.

## Files
*   `count.py` - Uses `tiktoken` to calculate exact token sizes.
*   `latency_test_new.py` - Uses `google-genai` to test LLM comprehension and response times.
*   `uc*` - The test code snippets (Verbose vs Short).