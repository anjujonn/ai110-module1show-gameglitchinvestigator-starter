# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
it was hoenstly really buggy. Making the correct guess seemed impossible as it felt like the game was against me
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1. new button functionality doesnt fully work--there is no real new session being generated even though the new random number is generated (the secret). When I try to submit new guesses, it wont let me! What I expect is that the session restarts and all values are reset for me to actually start a new game.
2. the guess vs secret number check is not working where the "higher"/"lower" message is opposite of what it should be. When my guess is low it says I need to make my guess even lower...
3. for some reason I'm having to click submit multiple times occasionally for the "higher"/"lower" message to update. I expect it to update immedietly after clicking the submit button.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
ClaudeCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
For the new_game logic, it originally wasn't fully resetting the game. For this issue, Claude basically added code to fully reset code by resetting the game status and history. I verified this result by looking through the Dev Debug section on the website and checking the live values. I also tested the update by going through the userflow to see if I was getting previous or new errors
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I was having issues with my cmd prompts--when I was trying to run pytest in terminal, I was having trouble as I was running pytest directly instead of adding python tags before (i.e. `pytest` instead of `python -m pytest`). When I asked Claude about the issue, originally it suggested that I needed to download requirements.txt because pytest wasn't downloaded into the environment, however, I've already run requirements.txt prior to running the pytest command. I prompted it again and was more clear about my situation and got the correct solution to add `python -m` before the `pytest`
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I would run through a full or necessary amount of user-flow
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Well when I ran the test checking the check_guess function, I realized I fixed one part of it correctly, but incorrectly reversed a part (the too low/high messages). I realized I altered a bit much and fixed the code correctly. It showed me that despite my edits, there were still issues
- Did AI help you design or understand any tests? How?
  AI helped me design the tests by going through my functions and helping me generate proper tests for each function. It understood what each function was doing and helped me build tests that properly and correctly tested functions' functionality
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
well it would change if I either trigger restart via streamlit, refresh the page, or if I start a new game
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
if you rerun the website, streamlit will run the website again from top to bottom regardless of where you previously were. 

Everytime you're on the website theres a lot of data thats flowing through the website (like the number of guesses you have left, etc.), but that data needs to keep changing, especially when you have major events like "new game". Session state is this major event-like data that survives the rerun.  
- What change did you make that finally gave the game a stable secret number?
Just by checking if secret isnt in the session state. It should be generated at the start and then never again until a new game is triggered
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I would like to reuse is how I shifted a lot of the time-consuming and thoughless-labor to AI. For example, isntead of manually cut-and-past-ing the code from app.py to logic_utils.py, I had Claude do it 
- What is one thing you would do differently next time you work with AI on a coding task?
Probably prompt a bit better than I did for this project.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think it made me feel a lot less guilty than I normally would feel. It feels like a cheetcode to a puzzle. Although I knew this already, I struggled to actively view AI as a tool and not a cheetcode.