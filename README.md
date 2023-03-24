***
Mission Start Date(started programming):  <strong>Mar 22, 9:42 PM</strong><br> 

Deadline(I run out of free time): <strong> Mar 24, 8:30am</strong>

To clarify any inconsistancies in work time ~24hrs - ~36hrs.
- the math function(3x+1) used in the prgroam is recycled from an earlier project i did for fun [see Histories](#histories-and-explination-of-project).
- it took me a few tries to get it right, i'll probably do the same again.


****

### [Navigation Bar](#nav)
# Disclaimer 🤚️ 
    This will update many times
<br>
Like with any project you can't help but be a little safe.<br>
Not everyithing in here will be done by tommorrow, but it is all within my scope.

<br>

***
UI skills are low, Hence the AI.<br>
😮‍💨️ if only i had time to focus more on sheek.
- upside though, it's like tutoring all over again.
- small steps, easy examples.

***
Again, <strong>AI</strong> is only assisting in the <strong>UI</strong> for <strong>HTML</strong>, <br>
I have to 🛠️ some of it to make it work,<br>
and the framework will probably meld it more into my own thing.
<br><br>

***
# General Outlines 👇️

- will add demo📽️ run files later, screenshots or video.

<br>

## nav
- [Some-Histories-and-Explination-of-Project](#histories-and-explination-of-project) 
- [General Goals](#General-Goals)
- ### Files
  - [html/](./html/)
    - mostly AI generated templates
    - I patched logic in between and fluffed it the way it needs to be.
  - [langs/](./langs/)
    - python.zip - so the program can be run independantly of system
  - [modules/](./modules/)
    - additional python or other libraries which may be needed
    - commonData.py
      - a controlable way to distibute information between .py modules
      - will need to fan it out later. 
  - [sampleRuns/](./sampleRuns/)
    - a way to demonstrate the program
    - videos/ - maybe
    - pictures/ - more than likely
  - [saves/](./saves/)
    - where each run of a math function is saved.
    - will be /data/3x+1/saves when it's better suited.

  - [progInit.py](#proginit)
  - [progLoop.py](#progloop)
  - [plotGraph.py](#plotgraph)
***
My main goals are in   
<strong>High Priority</strong>
<br><br>
***

### [Navigation Bar](#nav)

# Dependencies 💣️
- ### python3 -- embedded/zipped can be added for further portablitlity
  - ### [langs/python-embedable](./langs/)
- ### a web browser
  - WebUI -- comming soon
- ### command line knowledge
- Autorun files
    - "[run.sh](./run.sh)" and "[run.bat](./run.bat)" -- comming soon
    - <p> Yes these too will be <p style="font-style: italic;">hand-coded</p>i run linux, and am a Windows 98-etc-Win-10 vet/survivor.
    - none of it matters though it's a balance between: priciple and convience
  - steps
    - (bonus) check if we have a zip file
    - extract /langs/python Zip file
    - make sure it only runs from embeded, we don't want to install it.
    - clean up zip file if we want it more permanent
    - start [program](./progInit.py) with extracted python.exe file.


<br><br>
***

### [Navigation Bar](#nav)

# High-Priority 
- make everything presentable, readme, code, assessability.
- link the generate file function to UI
- link the view graph to graphPlot function via a table of selections
<br><br>
***

### [Navigation Bar](#nav)

# General-Goals
- unify into a configeration.json file.
- add more menus to console and HTML
<br><br>
***

### [Navigation Bar](#nav)

# progInit
## The launchpad of the program and it's general steps
- redirect current modules to the main starting point.
- steps
- - set/read a config file constants/variables
    - determine arg values on first run
      - we'll be Agile-ing this
  - check gitHub for updates - extra for now, we're not that big
  - launch server UI
<br><br>
***

### [Navigation Bar](#nav)

# progLoop
## the main loop of the program
- console command line math function takes arguments from an HTML UI interface, or the console.
  - console works, it asks for a number of times to make a random selection
  - files are deposited into /db/3x+1/saves, will update path when more relevant.
  - need to add abilty to choose a number
  - add multi threading on a # of threads = # cores on system
  
 - need to further unify html with python
 - add menu to run diffrent functions/simulations
<br><br>
***

### [Navigation Bar](#nav)
# plotGraph
- does what it says simply.
  - takes obj contained in save folders.
  - console can launch all, do not do with a lot in there
  - console can launch a single selection.
  - add as an option with it's own menu
  - compress into a class


<br><br>
***

### [Navigation Bar](#nav)

# Histories-and-Explination-of-Project
The AI world has always interested me and i've recently ventured to explore it. <br>
it only makes sense you'd  use a virtual coder to assist to save time when you're scratching your head. <br>
Or it's something numerous like prettying data, i'll get there.
***
Along with <strong>AI</strong>, Math has always been an interest to me,
numberphile on youtube is great.
along with computerphile.
***
There was an episode where they ran over this function(3x+1), since it hit one of my 2 triggers i just needed to play around with it a bit. Then that lead to another program i've yet to find which ran a small simulation of hunter/gathers in a selfish selfless random ratio...computer got warm.
***
Don't worry I keep most valuables backed up, but when i just play around with coding it's just fun.


</body>