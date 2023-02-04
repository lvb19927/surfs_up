# surfs_up
## Overview
### The Beginning:
Our client W. Avy wishes for further analysis on the wweather patterns before he opens his surf shop. He requested the months of June and December be analyzed for Oahu. We used coding metrics to find the summary statistics of June and December.

## Results
### The Key Facts:
After creating the summary stats, we can find that there is not much of a difference between June and December.

<img width="137" alt="surfs_up_June" src="https://user-images.githubusercontent.com/117100491/216774806-45f97d0a-5ee3-4b88-974a-41be6f0d0a1f.png">

<img width="132" alt="surfs_up_Dec" src="https://user-images.githubusercontent.com/117100491/216774814-0dbb06ac-e13b-4e13-9887-b776e30b2f14.png">
- There is a higher count for June temps than Dec temps (1700 to 1517)
- There is a 3 degree change from the average temp between June average temps and Dec average temps (Dec = 71, June = 74)
- The minimum temps are the largest dipsarities between June and Dec, with June min equaling 64 and Dec min equaling 56.

## Summary
### The End 
The results show that there is not much disparity in temperature between the June months and the December months. However, there is a disparity between the data counts in between June and December. 
We could pull out a few more data points to help bridge the gap.

### Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns=['date','precipitation'])
### Sort the dataframe by date
df.set_index(df['date'], inplace = True)

We could bring in the precipation levels as other data point. Pulling from the full data set.

We could use the df function to create several different summary charts with different levels of data, code = df = pd.DataFrame(results, columns = [something to be put in here]
We could create a summary index to complete the analysis.
