import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

data = pd.DataFrame(yf.download('AAPL', 
                                start='2021-01-01', 
                                end='2022-01-01')['Close'])
data ['return'] = np.log(data / data.shift())

plt.figure()
data.plot(subplots=True)

S0 = data['Close'].iloc[-1]
r = data['return'].mean()
sigma = data['return'].std()
I =1000
T = 252
S = np.zeros((T+1, I))
S[0] = S0
for t in range(1,T+1):
    S[t] = (S[t-1] * np.exp(r - .5 * sigma **2 + 
            sigma * np.random.standard_normal(I)))
            
plt.figure()
plt.hist(S[-1], bins=50)             
plt.xlabel('frequency')
plt.ylabel('price')

data = pd.DataFrame(yf.download('AAPL',start='2022-01-01')['Close'])[:253]

plt.figure()
plt.plot(data.index,S, alpha=.5)
plt.plot(data, '-k', lw=2, label='Apple')
plt.xlabel('time')
plt.ylabel('price')
plt.legend()

    
# VaR and CVaR
S_f = S[-1]
S_f.sort()
alpha = 0.05  
VaR = np.percentile(S_f, 100 * alpha)
CVaR = np.mean([s for s in S_f if s <= VaR])

print('Value at Risk (VaR) at %.0f %% confidence level: %.2f' 
      %(alpha*100, VaR)) 
print("Conditional Value at Risk (CVaR) at %.0f %% confidence level: %.2f"
      %(alpha, CVaR))

