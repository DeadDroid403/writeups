 so we can have to check all the 2_000_000 means 2 million checkboxes.
when we click one check box, the site sends the a json type message with a list of check boxes we checked.
i tried to generate a list using python of 2 million numbers and send it using that web socket but it can't even paste such large number. i tried the same with 1 million and my burp repeater stuck again. so i started with small lists like 1000 or 10000 and then i gradually increase the size of list.
in the end i found i could only send the largest web socket message of 100k means 1 lack numbers list using the web socket connection. i could create a script to send 20 packets of that 1 lakh numbers list to reach 2 million checkbox but i was lazy to make a script and my brain was rotted enough to do it manually. so i send 20 web socket packet one by one each by crafting 20 different numbers list and finally reached the 2 million check box goal and i got the flag.

flag{7d798903eb2a1823803a243dde6e9d5b}
