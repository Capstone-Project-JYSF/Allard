## Structure

```
.
│   about.html
│   backend.py
│   backend_functions.py
│   favicon.ico
│   index.html
│   questionaires.html
│   README.md
│   result.html
│   result_script.js
│   script.js
│
├───css
│       about.css
│       questionaries.css
│       result_style.css
│       style.css
│
├───images
│       law_main.jpg
│       logo.png
│       questionaires_background.webp
│       questionnaire.jpg
│       result.jpg
│       result_background.webp
│
└───__pycache__
        backend.cpython-310.pyc
```


## Instruction of how to run the backend

1. pip install fastapi，pydantic， and uvicorn
2. Make sure you are in the `Web_Interface` directory
3. run `uvicorn backend:app --reload` in terminal
4. Open a browser, paste the local host IP showed in terminal (should be something like http://127.0.0.1:8000)