import json

regions = json.loads(open("teams.json").read())

seeds = [
  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
  [1,3,5,7,9,11,13,15],
  [1,5,9,13],
  [1,9],
  [1]
]

for region in regions:
  print '<div class="region">'

  for i in range(5):
    print "\t"+'<div class="round">'

    for j in range(2**(4-i)):

      team = region[seeds[i][j]-1]

      print "\t\t"+'<div class="team">'+team+'</div>'

    print "\t"+'</div>'

  print '</div>'