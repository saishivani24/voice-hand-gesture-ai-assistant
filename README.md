# Voice and Gesture

```
(myenv) (base) C:\Users\Shivani\OneDrive\Desktop\Gesture-Controlled-Virtual-Mouse-main\src>python --version
Python 3.8.5
```

# set microphone to 45%

# Anaconda Navigator

```
Anaconda Navigator 1.10.0:
Release Date: November 20, 2020.
Notable Feature: Navigator now remembers the last environment used instead of loading the default environment each time. Additionally, it has improved integration with Anaconda Team Edition2.
```

# Fine tuning mode: 
```
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        temperature=temperature,
        top_k=50,  # Consider top-50 tokens during sampling
        top_p=0.95,  # Use nucleus sampling with cumulative probability cutoff
        repetition_penalty=1.2,  # Discourage repetition in generated sequences
        no_repeat_ngram_size=3,  # Avoid repeating n-grams of size 3
        early_stopping=True  # Stop generation when EOS token is reached
    )
```

# Follow these steps to run the code

## steps
- `Clone the repo https:github.com/sai8151/balu`
- `Open anaconda`
- `launch vs code`
- `create a venv else activate if exist`
- `to activate in windows:`
```
cd myenv
cd Scripts
activate
```
- `install all libraries in req.txt`
- `make sure you have gpt2`
- `pip install opencv-python mediapipe pyautogui comtypes protobuf screen_brightness_control pycaw`
```
python test.py
```
- `voice command:"run Gesture Controller" this will run the Gesture Controller python code in the same dir`
