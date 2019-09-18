# Random Sampling and Standard Distributions

## 1. check the functions in `numpy.random`
    - https://docs.scipy.org/doc/numpy-1.16.0/reference/routines.random.html
    - https://numpy.org/devdocs/reference/random/index.html

## 2. plot histograms

1. 1M samples generated from N(0,1)
    - `np.random.normal()`
2. 1M samples from a continuous uniform distribution U(0,1)
    - `np.random.uniform()`
3. 1M discrete random integer samples from U(0,1000)
    - `np.randint()`
5. 1M trials from binomial distribution with $n=100$ trials and the probability of success (or head) p = 0.3
    - $Pr[X=1] = 0.3 = p$  
    - https://en.wikipedia.org/wiki/Binomial_distribution
    - `np.random.binomial()`

4. 1M samples from Bernoulli distribution with $P(X=1) = 0.3$

    - https://en.wikipedia.org/wiki/Bernoulli_distribution
    - the set of samples is composed of two numbers only, 0 and 1 (or A and B).
    - you can use `np.random.binomial()` or `np.random.uniform()` to generate samples from Bernoulli distribution.

  
## 3. CDF (Cumulative distribution function), PDF (Prob. distribution function), PMF (Prob. Mass Function)

- https://en.wikipedia.org/wiki/Cumulative_distribution_function

1. plot cdf and pdf of Normal (or Gaussian) distribution with (`$$mean=0$$`, `$$\sigma=1$$`) and (`$mean=0$`, `$\sigma=5$`), respectively.
2. plot cdf and pdf of uniform distribution `$U[0,1]$`
3. plot cdf and pmf of Bernoulli distribution with `$p=0.3$`
4. plot cdf and pmf of `$binomial(n=100, p=0.3)$`
  
  
