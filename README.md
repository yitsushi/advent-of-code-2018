Download all input files from under the corresponding directory with the name of 'input'

```
$ export PYTHONPATH="${PYTHONPATH}:`pwd`"
$ ./system solve --day <n> --part <1|2>
```

## Example

### Day-01:

```
❯ ./system solve --day 1 --part 2
The solution for day-01/part2:
390

Timing:
  setup   : 0.0008s
  solution: 0.0393s

  full    : 0.0401s
```

### Day-10:

```
❯ ./system solve --day 10 --part 1
#####   ######   ####   #       #####   #    #  ######  ######
#    #  #       #    #  #       #    #  ##   #       #  #
#    #  #       #       #       #    #  ##   #       #  #
#    #  #       #       #       #    #  # #  #      #   #
#####   #####   #       #       #####   # #  #     #    #####
#  #    #       #       #       #  #    #  # #    #     #
#   #   #       #       #       #   #   #  # #   #      #
#   #   #       #       #       #   #   #   ##  #       #
#    #  #       #    #  #       #    #  #   ##  #       #
#    #  ######   ####   ######  #    #  #    #  ######  ######
The solution for day-10/part1:
You can see your answer above.

Timing:
  setup       : 0.0044s
  fast-forward: 0.0179s
  solution    : 0.0530s

  full        : 0.0753s

❯ ./system solve --day 10 --part 2
The solution for day-10/part2:
10007

Timing:
  setup       : 0.0051s
  fast-forward: 0.0183s
  solution    : 0.0001s

  full        : 0.0235s
```
