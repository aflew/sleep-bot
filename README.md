# sleep-bot
## Inspiration
Both of us are always tired, yet when it is time to go to bed, we still stay up late. We also know that sleep is extremely important. Some study's say that up to 96% of college students do not get enough sleep on a regular basis. We know our bot wont change much, but in those few situations where the time just start slipping away, hopefully Sleep Bot will provide enough of a nudge so that you can get a good nights sleep.
## What it does
Sleep Bot is a discord bot bordering on malware, where you can input your wake up time for every day of the week. When it is < 9 hours from your wake up time and you are still active on, Sleep Bot will send you a gentle nudge to get to bed. If time goes by, and you are still on discord, Sleep Bots nudges start to become _not_ _so_ _gentle_. Furthermore, If Sleep Bot notices that you had a poor sleep (< 5 hours), it will ask you how you are feeling. On future nights, where you are ignoring Sleep Bot and staying awake, Sleep Bot will start to use your testimonials to help convince you to go to bed.
## How we built it
A lot of research. All the code was written in python, and we used the discord.py library.
## Challenges we ran into
Neither of us had any experience coding a discord bot or any type of app. At the start of the hackathon, only one of us knew python. 
## Accomplishments that we're proud of
It fully functions. We were able to implement every part of the design that we had set out to do. 
Now both of us know python (kinda).
## What we learned
How to make a discord bot (how to send messages, read messages, check the time, etc.). 
In Python we learned everything for one of us and more specifically how to use asynchronous functions, and tasks.
## What's next for Sleep Bot
Future implementations of Sleep Bot could add a service that compares when you set your alarm to when you actually got out of bed. This way it could make recommendations for when you need to set your alarm for each day.
We should also determine a better data storage method that isn't just making a bunch of User objects within the program if we ever want to scale up. 
