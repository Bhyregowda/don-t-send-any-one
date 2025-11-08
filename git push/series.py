#import neccesary libraries
import pandas as pd
#given series
seriesA=[10,20,30,40,50,60]
seriesB=[40,50,60,70,80,90]
#converting both the series to set
seriesAA=set(seriesA)
seriesBB=set(seriesB)
#finding not common elements in both
notcommon=seriesAA.difference(seriesBB)
print(notcommon)
#finding smallest and largest elements in series-A
small=min(seriesA)
large=max(seriesA)
print('small',small, 'largest=',large)
#find the sum of seriesB
sum=sum(seriesB)
print(sum)
#find the average of seriesA
import statistics as st
avge=st.mode(seriesA)
print(avge)
#finding median in seriesB
median=st.median(seriesB)
print(median)