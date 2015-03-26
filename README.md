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

## Stats
```
http://slackrandom.com/stats
```