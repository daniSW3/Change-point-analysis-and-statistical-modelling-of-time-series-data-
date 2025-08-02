import pymc as pm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'])
log_returns = np.log(df['Price'] / df['Price'].shift(1)).dropna()

with pm.Model() as model:
    # Prior for switch point (uniform over data range)
    tau = pm.DiscreteUniform('tau', lower=0, upper=len(log_returns) - 1)

    # Priors for means
    mu1 = pm.Normal('mu1', mu=0, sd=0.1)
    mu2 = pm.Normal('mu2', mu=0, sd=0.1)

    # Switch function
    sigma = pm.HalfNormal('sigma', sd=0.1)
    mu = pm.math.switch(tau >= np.arange(len(log_returns)), mu2, mu1)

    # Likelihood
    returns = pm.Normal('returns', mu=mu, sd=sigma, observed=log_returns)

    # Sampling
    trace = pm.sample(2000, tune=1000, return_inferencedata=False)

# Check convergence
pm.summary(trace)
pm.plot_trace(trace)
plt.show()