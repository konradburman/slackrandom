# Slack Random

## Set-up
### Slash Commands
```
1. Goto Account -> Integrations
2. Search and select 'Slash Commands'
3. Enter the command that you would like to use (recommend /random)
4. URL enter 'http://slackrandom.com/random'
5. Method 'POST'
6. Fill out Autocomplete help text (optional)
6. A. Description 'Generates random values'
6. B. Usage hint '[min max] [max] [uuid] [coin #] [dice #]'
7. Fill out Description Lebel (optional)
8. Save Integration
```
### Webhooks
```
Coming Soon
```
---
## Commands
Using '/random' as our Slash Command

#### Random Integers
Integer between 1 - 100
```
/random
```
Example:
```
/random
Slack Bot: 96
```
---
Integer between 1 - MAX
```
/random MAX
```
Example:
```
/random 10000
Slack Bot: 4578
```
---
Integer between MIN - MAX
```
/random MIN MAX
```
Example:
```
/random 456 789
Slack Bot: 510
```
---
#### UUID
UUID as per [UUIDv4](http://en.wikipedia.org/wiki/Universally_unique_identifier)
```
/random uuid
```
Example:
```
/random uuid
Slack Bot: 078b9d6d-95c1-4428-866d-c3dc1b27a888
```
---
#### Coin
Single Heads/Tails Coin toss
```
/random coin
```
Example:
```
/random coin
Slack Bot: Heads
```
---
N Heads/Tails Coin tosses where 1 <= N <= 100
```
/random coin N
```
Example:
```
/random coin 10
Slack Bot: Heads Tails Heads Tails Tails Heads Tails Tails Heads Tails
```
---
#### Dice
Single 6-sided Dice roll
```
/random dice
```
Example:
```
/random dice
Slack Bot: 1
```
---
N 6-sided Dice rolls where 1 <= N <= 100
```
/random dice N
```
Example:
```
/random dice 10
Slack Bot: 6 2 5 2 5 6 4 2 6 1
```
---
#### Colour
Hex Colour
```
/random [colour || color]
```
Example:
```
/random colour
Slack Bot: #e0fb01
```
---
#### Bytes
Hex byte
```
/random byte hex
```
Example:
```
/random byte hex
Slack Bot: 3b
```
---
N Hex bytes where 1 <= N <= 10000
```
/random byte hex N
```
Example:
```
/random byte hex 10
Slack Bot: e3 7b 54 97 10 89 99 e8 22 5c
```
---
Octal byte
```
/random byte octal
```
Example:
```
/random byte octal
Slack Bot: 007
```
---
N Octal bytes where 1 <= N <= 10000
```
/random byte octal N
```
Example:
```
/random byte octal 10
Slack Bot: 016 270 113 107 175 252 363 165 315 244
```
---
Binary byte
```
/random byte binary
```
Example:
```
/random byte binary
Slack Bot: 01100001
```
---
N Binary bytes where 1 <= N <= 10000
```
/random byte binary N
```
Example:
```
/random byte binary 10
Slack Bot: 11101001 00111001 10111010 10111000 11100100 00011110 01101100 00111010 
11101111 01100110
```

## Stats
```
http://slackrandom.com/stats
```