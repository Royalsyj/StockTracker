# StockTracker

## This is a hobby software stocker tracking application.
## End goal is to enable this script to run 24/7 on a Raspberry Pi with sound alerts/alarms

Usage: Run in cmd line, periodically checks .txt file for user information
``` 
Some cmd line here
```

## Main Features

### Periodic Update
- Periodic update (at least once per minute)

### Simple data analysis
- Detects trends (dropping, rising, volatile, stable)
- Keeps track of the past 5 days (?)

### Alarm
- Plays unique sounds for different alarm settings
- Settings:
  - When stock rises to a certain value
  - When stock falls to a certain value
  - When analysis tracks a significant change in value
    - Falling to raising (recovering)
    - Raising to falling (peaked)
    - Rocketing
    - Crashing

## Usage
User inputs in txt file:
[stonk name]
[owned stonk details]


[options]
[owned option details]


[alarm settings]
rise/drop to specific value