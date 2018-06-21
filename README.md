# rnd-sites
This program will create a list of random websites and check if they exist. How he will create them will depends on the arguments.
# What its should do?
+ Create a txt file with list of random websites
+ Deduplicate
+ Check if they exist
+ if some of them are exist write to txt\sorted.txt
+ if don't -> remove all files and directories (which was created ofc)
# Arguments:
```
-p https ,  --protocol https     Choose http or https                    (default: https)
-l number,  --letter number      How long site name will be (5-7 avrg)   (default: False)
-d .com,    --domain .com        Domain: .com or .ru                     (default: .com)
-a 100,     --address 100        How many addresses you need to create   (default: False)
```
# Example:
**Full:**
```
python rnd.py -p https -l 5 -d .com -a 1000
```
**Without defaults:**
```
python rnd.py -l 5 -a 100
```
