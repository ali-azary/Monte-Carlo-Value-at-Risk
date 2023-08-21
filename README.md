# Monte-Carlo-Value-at-Risk
Geometric Brownian Motion for Value at Risk and Expected Shortfall calculations
<h3>Modeling Stock Prices with Geometric Brownian Motion</h3>

In the realm of finance, the Geometric Brownian Motion (GBM) model serves as a fundamental tool for simulating and 
analyzing the behavior of stock prices over time. This model is based on the concept that stock prices evolve stochastically, 
influenced by drift and volatility.
<br>
The GBM model is represented by the following stochastic differential equation:

$dS_t = \mu S_t dt + \sigma S_t dW_t$
<br>
where:<br>
- $S_t$ is the stock price at time $t$<br>
- $\mu$ is the drift (expected return)<br>
- $\sigma$ is the volatility (standard deviation of returns)<br>
- $dW_t$ is a Wiener process (Brownian motion) increment<br>

The discretized version for discrete time steps can be written as:

$S_{t+1} = S_t \exp\left((\mu - \frac{1}{2} \sigma^2) \Delta t + \sigma \sqrt{\Delta t} Z_t\right)$
<br>
where:<br>
- $\Delta t$ is the time step<br>
- $Z_t$ is a random variable sampled from a standard normal distribution<br>

<h3>Value at Risk (VaR)</h3>

Value at Risk (VaR) is a risk assessment measure that quantifies the potential loss an investment might face over a specified 
time horizon at a given confidence level. In the context of the GBM model, VaR is calculated based on the simulated final prices.
 The $1 - \alpha$ quantile of these prices represents the maximum potential loss with a confidence level of $\alpha$.

$VaR_\alpha(X)=-\inf \left{x \in \text{R}: F_X(x)>\alpha\right}=F_Y^{-1}(1-\alpha)$


<h3>Conditional Value at Risk (CVaR)</h3>

Conditional Value at Risk (CVaR), also known as expected shortfall, provides an additional layer of risk assessment beyond VaR.
 It represents the average value of the losses that exceed the VaR at a specified confidence level. Mathematically, CVaR is 
 calculated as the average of all prices that fall below the VaR.

$\mathrm{ES}_\alpha(X)=-\frac{1}{\alpha} \int_0^\alpha \operatorname{VaR}_\gamma(X) d \gamma$

<h3>Python Implementation</h3>

To put the theory into practice, let's implement the GBM model using Python. We'll use historical stock price data 
for Apple and simulate potential price paths. Then, we'll calculate VaR and CVaR based on the simulated outcomes.


![img02](https://github.com/ali-azary/Monte-Carlo-Value-at-Risk/assets/69943289/ec0768cb-8634-4ec1-8cd0-7c32dec6fad3)

![img03](https://github.com/ali-azary/Monte-Carlo-Value-at-Risk/assets/69943289/e9b70d14-5ec3-4f53-a5a7-155f1d41dbee)


Value at Risk (VaR) at 5 % confidence level: 154.89<br>
Conditional Value at Risk (CVaR) at 0 % confidence level: 139.58
