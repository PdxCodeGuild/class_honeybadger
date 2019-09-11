
import math
import time
import chalk
import random



colors = [chalk.red, chalk.yellow, chalk.green, chalk.blue, chalk.cyan, chalk.magenta]

for i in range(10000):
    color = colors[(i//40)%len(colors)]
    print(color(' '*int(14+10*math.sin(i/10)) + 'xxxx'), end='')
    print(color(' '*int(14+10*math.cos(i/10)) + 'xxxx'), end='')
    print(color(' '*int(14+10*math.sin(i/10)) + 'xxxx'))
    time.sleep(0.01)

exit()

colors = [chalk.red, chalk.yellow, chalk.green, chalk.blue, chalk.cyan, chalk.magenta]

for i in range(10000):
    color = colors[(i//40)%len(colors)]
    print(color(' '*int(28+10*math.sin(i/10)) + 'xxxx'))
    time.sleep(0.01)

exit()

colors = [chalk.red, chalk.yellow, chalk.green, chalk.blue, chalk.cyan, chalk.magenta]

for i in range(10000):
    color = colors[(i//5)%len(colors)]
    print(color('x'*int(28+10*math.sin(i/10))), end='   ')
    print(color('x'*int(28+10*(1-math.sin(i/10)))))
    time.sleep(0.01)

exit()



colors = [chalk.red, chalk.green, chalk.blue, chalk.magenta, chalk.cyan, chalk.yellow]

for i in range(10000):
    color = random.choice(colors)
    print(color('x'*int(28+10*math.sin(i/10))), end='   ')
    print(color('x'*int(28+10*(1-math.sin(i/10)))))
    time.sleep(0.01)

exit()

scale = 3
for i in range(10000):
    color = random.choice(colors)
    print(color('(ᵔᴥᵔ)'*int(2*scale+scale*math.sin(i/10))), end='   ')
    print(color('(ᵔᴥᵔ)'*int(2*scale+scale*(1-math.sin(i/10)))))
    time.sleep(0.01)

exit()


