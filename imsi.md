## Short range plan

1. random num. generation, get acquainted with prob. concepts
- don't forget to see mathematical equations
- Expection $\mathbb{E}$
- Bernoulli, binomial, Multinomial, Gaussian, beta

- Multi-dimensional Gaussian
    - sample generation
    - sample density plot by scatter plot
    - sample mean / sample covariance definition & computation
        - connect to PCA
            - 1D data -> 2D embedding -> scatter plot -> noise in y-direction -> rotation (x = R z) -> eigen decomposition -> recover 1D data
    
1. plt plotting, MATLAB & OO style, scatter plot, histogram

1. data exploration & visualization
- `matplotlib`
- datasets in sklearn: https://scikit-learn.org/stable/datasets/index.html
    - iris
    - search for a dataset!
    
1. information theory
    * Bishop Book Chapter 1.6
        * https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf

1. decision tree
- entropy = `expection of information` = `average information` (for discrete r.v.'s)
- Gini = `expection of not-me` = `expectation of mislabeling by random labeling according to p_i`
