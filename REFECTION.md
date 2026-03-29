The agent implemented most features on the first try pretty well, it was just that some of them were buggy. 
I think overall my spec was pretty good, as was the prompt that was given. So Copilot did a really good job of making a list of pass,warn,fails 
(of which no fails were present).
The AI review was super useful. There were no bugs that really broke the code badly, but there were a lot of lifestyle changes and security changes copilot 
suggested as a result of the review, which were all helpful and productive for the overall quality of the outcome of the project.
In hindsight, I remain confident that my spec was pretty good, however there were some shortcomings. One of the biggest shortcomings was that I did not
explicitly state that there should be more questions than just the 5 sample ones that I gave it. So It only implemented the 5 questions which I think
is a pretty problematic outcome. Also it feels like UX was not always in mind, given that every question asks users if they want a hint, before the users
can answer the question, which feels pretty couterintuitive or annoying for many users.
I think this workflow is pretty effective overall. Something I would prefer to do is have AI also write a very high quality spec, and also determine
what some potential shortcomings, likely bugs, or error protection protocols that we should ensure that we implement in the eventual implementation.
Gemini or ChatGPT or another thoughtful agent would be good at this. Then the resulting high-quality spec can be passed to Claude or Copilot or Cursor or 
something else that is known to be very good at coding. Then, of course, I can have another agent (perhaps another instance of claude, copilot, or cursor 
like mentioned above) to do the reviewing. This is clearly an effective model, especially with good specs (which I think agents can probably be very good at 
helping people to write), so I am likely to use it in many different situations or for many different types of projects.
