#import python libraries
import pandas as pd
seriesA=['a','b','c','d','e','f']
seriesB=['x','y','z','a','b','c']
#converting both the series to set
seriesAA=set(seriesA)
seriesBB=set(seriesB)
#finding notcommon elements in both
notcommon=seriesAA.difference(seriesBB)
notcommon1=seriesBB.difference(seriesAA)
print(notcommon,notcommon1)
#common elements in both series
common=list(set(seriesAA)&(set(seriesBB)))
print(common)
#print the elements in both series
series=seriesA+seriesB
print(series)