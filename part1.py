import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("SchoolA.csv")
print(df.columns)  # run this first, then fill in the real names below

# Fit regression: diligence ~ IQ
X = df["IQ"]          # replace with your actual IQ column name
Y = df["diligence"]   # replace with your actual diligence column name

result = stats.linregress(X, Y)
print("slope:", result.slope)
print("p-value:", result.pvalue)
print("stderr:", result.stderr)

# Residual check
predicted = result.intercept + result.slope * X
residuals = Y - predicted

stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ-plot of residuals")
plt.show()
