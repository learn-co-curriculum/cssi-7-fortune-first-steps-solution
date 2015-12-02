

#Fortune Teller Potential Solutions

Before moving on to adding user functionality today, feel free to clone this repository onto your local machine so we can all start on the same page. 

Notice that because multiple handlers need a way to access a message indexed at either a random  or  specific number, a global function, `getMessage()` is defined. `getMessage()` is outside any of the handler classes so that it can be used multiple times:

```
def getMessage(any_list,specificNumber=0):
    #if there is no second parameter passed, then pick a random index
    if specificNumber == 0:
        index = random.randint(0,len(any_list)-1)
    #if there is a specificNumber, then use that to index the messages
    else:
        index = specificNumber
    return any_list[index]
```

<a href='https://learn.co/lessons/cssi-7-fortune-first-steps-solution' data-visibility='hidden'>View this lesson on Learn.co</a>
