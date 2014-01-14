import myMath
import imp
imp.reload(myMath)      # makes sure you're working with the up-to-date version

print(myMath.distance((3,0), (8,5)))
print(myMath.circle_area(1))
print(myMath.quadratic(1, 3, 2))