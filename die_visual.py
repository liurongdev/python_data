
from die import Die
import pygal
import cvs



die=Die()

results=[]


for i in range(1000):
    result=die.roll()
    results.append(result)


print(results)

frequences=[]


for  i in range(1,die.number+1):
    count=results.count(i)
    frequences.append(count)


print(frequences)


hist=pygal.Bar()


hist.title="title"
hist.x_labels=['1','2','3','4','5','6']

hist.x_title="resutl"

hist.y_title="frequences of result"

hist.add("D6",frequences)

hist.render_to_file("die_visual.svg")

