# Pandas on Spark

## Problem of using Pandas on productive big data platforms

When writing pandas applications using scalable big data clusters, the main problem is the application execution. When using pandas, all the logic and transformations applied to the data are executed only in the Driver node of the cluster. Using a scalable big data cluster means that you have to leverage all the nodes (Driver and workers) to execute the applicaiton, and the pandas library can't make good use of the clusters.

When using Pyspark, all the nodes of the clusters are well leveraged. But rewriting all the source code from pandas to pyspark can't be hard for some data anlysts or data scientists.

## Solution - Pandas API on Spark

Using pandas on Pyspark! Simply importing a pandas class from pyspark framework allows the data builders to use the pandas functions while leveraging the distributed assets of pyspark and big data clusters. All the data transformations defined using this class are distributed among the driver and executor nodes!

```Python
import pyspark.pandas as pd

df_users = pd.read_json(path)

# Other pandas transformations here...
```

