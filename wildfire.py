import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("wildfire.csv")

# Set figure size to make it less squished
plot.figure(figsize=(10, 6))

data.plot(x="Entity", y="Annual number of fires", kind="scatter", title="Wildfire")

plot.show()
plot.savefig("wildfiregraph.png")
