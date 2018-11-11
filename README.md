# Arguments:
```
-p https ,  --protocol https     Choose http or https                    (default: https)
-l 7,       --letter 7           Second level domain (5-7 avrg)          (default: False)
-d .com,    --domain .com        Top-level Domain: .com or .ru           (default: .com)
-a 100,     --address 100        How many addresses you need to create   (default: False)
```
# Usage:
**Full:**
```
python rnd.py -p https -l 5 -d .com -a 100
```
**Without defaults:**
```
python rnd.py -l 5 -a 100
```
