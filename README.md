# YoutubeGraph-Dyn
Datasets to study the temporal evolution of graphs are scarce. To encourage the research of novel dynamic graph learning algorithms we introduce YoutubeGraph-Dyn, an evolving graph dataset generated from YouTube real-world interactions. YoutubeGraph-Dyn provides intra-day time granularity (with 416 snapshots taken every 6 hours for a period of 104 days), multi-modal relationships that capture different aspects of the data, multiple attributes including timestamped, non-timestamped, word embeddings, and integers. Our data collection methodology emphasizes the creation of time evolvinggraphs from non-timestamped data. 

We  collected  the  metadata  from  6,342  channels, 277,604 videos, and more than 20 million comments from 2018/07/13 18:00:00 to 2018/10/26 with a frequency of 6 hours (00:00, 06:00, 12:00, and 18:00). These 6,342 channels were selected based on their mentions or their videos mentions on Twitter. The rationale behind this design choice is that content with the potential of becoming popular is being discussed in other social networks beyond YouTube, e.g., on Twitter. We bootstrapped the original channel list from 16,209 YouTube video links posted in Twitter from 2018/07/06 to 2018/07/12.

Please refer to [Tracking Temporal Evolution of Graphs using Non-Timestamped Data](https://arxiv.org/abs/1907.02222) for complete details about the dataset.

## Repository Structure
* **anonymyzed_graphs**: contains Youtube graphs with the names of the files in the format: graph-yyyymmdd-hhhh.pickle. 
* **anonymyzed_timeseries**: contains timeseries data for channels. Channels have comment, subscriber, video and view counts. The topic categories per channel are provided.
* **anonymyzed_graphs.py**: file to anonymyze the original data.

## Data Format
We store all graphs using the [Graph](https://networkx.github.io/documentation/stable/reference/classes/graph.html) as **undirected unweighted graph** in python package networkx. The node ids are in the format 'c_XXX' and 'v_XXX' for channel nodes and video nodes respectively.

The time series data has channels as columns and values at each time step as the row.

## Cite
