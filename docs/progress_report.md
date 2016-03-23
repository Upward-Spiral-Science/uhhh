## Progress Report - March 24th, 2016
**Table of Contents:**
- [Overview](./progress_report.md#overview)
- [Scientific Questioning](./progress_report.md#scientific-questioning)
  - [Decriptive Analysis](./progress_report.md#descriptive-analysis)
  - [Exploratory Analysis](./progress_report.md#exploratory-analysis)
  - [Inferential Analysis](./progress_report.md#inferential-analysis)
  - [Predictive Analysis](./progress_report.md#predictive-analysis)
  - [Testing Assumptions](./progress_report.md#testing-assumptions)
  - [Next Steps](./progress_report.md#next-steps)
- [Methods](./progress_report.md#methods)
  - [Decriptive Analysis](./progress_report.md#descriptive-analysis-1)
  - [Exploratory Analysis](./progress_report.md#exploratory-analysis-1)
  - [Inferential Analysis](./progress_report.md#inferential-analysis-1)
  - [Predictive Analysis](./progress_report.md#predictive-analysis-1)
  - [Testing Assumptions](./progress_report.md#testing-assumptions-1)

----------

### Overview
Mental illness plagues humanity. Causing huge financial social burden, mental illness is the leading cause of disability globally. As such, we have been analyzing the structure of brain graphs with the goal of understanding underlying patterns or features which allow us to classify subjects based on observed covariates.

### Scientific Questioning
Here we will discuss our analysis of this data, starting with exploratory and descriptive analysis, up to preliminary work on hypothesis testing and classification. The questions posed and their outcomes are described sequentially, with code and methods used to answer them described at the end of this report.

#### Descriptive Analysis
The natural first step when working with any data is to ask exploratory and descriptive questions about it. We have been working with the KKI2009, SWU4, and MRN114 datasets, so we began by seeking some basic understanding of this data. It was important to understand the structure of our data, so we began by asking questions such as dataset size, number of nodes, and number of invalid (i.e. Inf/Na/NaN) data points were present in our data. Tabulated below are the results of these questions, where N  is the number of subjects, and |V| is the number of vertices. The final descriptive question asked was regarding the sparsity of our graphs: how many edges with weight greater than 0 exist out of the total possible number of edges. We found that across the entire dataset the edge density was 0.561.

| Query | MRN114 | KKI2009 | SWU4 |
|-------|--------|-------|------|
|N      | 114    | 42    | 454  |
| \|V\| | 70     | 70    | 70   |
|Invalid values | 0 | 0 | 0 |

#### Exploratory Analysis
Knowing now that our graphs are all equal in size (i.e. number of nodes), contain no obviously invalid data, but vary greatly in number of subjects, we seek to understand some more features specific to each dataset. The first exploratory question we asked was seeking to determine the average edge degree for each dataset. These results are tabulated below. We also compute the mean brain graph and visualize it, below.

<img src="../figs/mean_graph.png" data-canonical-src="../figs/mean_graph.png" width="300" height="300" />

| Query | MRN114 | KKI2009 | SWU4 |
|-------|--------|---------|------|
|Average Degree | 40.88| 19.95 | 40.69 |

We notice here there is a large difference in the mean degree in these graphs, so in order to understand this further we plotted a histogram of the edge weights for each dataset. This can be seen below.

<img src="../figs/histograms.png" data-canonical-src="../figs/histograms.png" width="300" />

We notice from these graphs that most of the edges are very low weights, and likely due to some type of noise. Taking the log of our graphs may make these graphs more robust to outliers in our further analysis.

#### Inferential Analysis
We now seek to understand class conditional differences within our datasets. From here, we will be only looking at the KKI2009 dataset. The covariate we are seeking to separate graphs based upon is sex. Firstly we must pick a feature of our graphs to test this difference under. As we'd looked at this feature in our exploratory analysis, we chose to use edge density as our feature. Running a wilcoxon test on this population, in which 22 subjects were male and 20 subjects were female, we found the following mean probabilities of edge based on class.

| Class | Mean edge probability |
|-------|-----------------------|
| Female| 0.014041836735        |
| Male  | 0.013130376117        |

We found that the difference between these populations was statistically significant with an alpha value of 0.05, produciing a p value of 0.022768743719. Since we found a statistically significant difference between classes, we can naturally proceed to trying to classify subjects based on their edge density.

#### Predictive Analysis
Now that a class conditional edge probability difference has been observed, we can attempt to explot this to classify subjects. Several types of classifiers were trained and tested using LOO cross-validation, and their results are tabulated below. Note that chance classification in this dataset is 47% accuracy, since the dataset has more males than females.

| Classifier | Accuracy | Standard Deviation |
|------------|----------|--------------------|
|Nearest Neighbors | 0.48 | +/- 1.00 |
|Linear SVM | 0.55 | +/- 1.00 |
|Random Forest| 0.57 | +/- 0.99 |
|Linear Discriminant Analysis| 0.45 | +/- 1.00 |
|Quadratic Discriminant Analysis| 0.71 | +/- 0.90|

Here we notice that with the only classifier which performs significantly better than chance is the Quadratic Discriminant Analysis. In order to gain some understanding as to why this is the case, we proceed to reevaluate our procedure thus far and test the assumptions we've been making up until this point.

#### Testing Assumptions
Up to this point, our analysis had made two large assumptions about our data: the graphs are sampled idependently and identically, and edges within the graph were sampled independently and identically. Another assumption made implicitly when doing classification with QDA that differs from the other techniques is that our covariance matrix differs across classes. Here, we test each of these assumptions to see if we can impove our model.

First, we test whether the graphs are sampled independently from each other and identically. Plotted below is the covariance matrix of our graphs. Significant content in the off-diagonal suggests that these graphs are in fact dependent. Below that, is a figure which plots the BIC score when doing GMM clustering on the graphs. We see that the optimal number of clusters is greater than 1, suggesting they are not identically distributed, either.

<img src="../figs/graphs_covariance.png" data-canonical-src="../figs/graphs_covariance.png" width="300" />
<img src="../figs/graphs_identical.png" data-canonical-src="../figs/graphs_identical.png" width="300" />

Next, we investigate the same properties about our edges. Shown below are the same two figures for edges rather than graphs. We again notice lots of content in the off-diagonal of our covariance matrix, suggesting dependence between edges. Notice in the identical test, however, that a clear "optimal" number of clusters does exist whereas previously the plot seemed monotonically increasing. Here we notice an optimal clustering of 4, which can later be leveraged when doing clustering or classification.

<img src="../figs/edges_covariance.png" data-canonical-src="../figs/edges_covariance.png" width="300" />
<img src="../figs/edges_identical.png" data-canonical-src="../figs/edges_identical.png" width="300" />

Finally, we test whether or not the assumption made implicitly in QDA, that our classes have different covariance matrices, is true. Shown below is a plot of each of the class covariance matrices, as well as a plot of the absolute difference of this matrix. We can see a significant difference in this matrix, which suggests why QDA outperformed the other methods (certainly LDA, which explicitly assumes classes have an identical covariance matrix).

<img src="../figs/class_covariance.png" data-canonical-src="../figs/class_covariance.png" width="300" />

#### Next Steps
Thus far we have learned a fair amount about the edge densities and properties of our data. Moving forward, we can analyze the mean and covariance of the clusters found in our assumption checking, and cluster our data prior to testing hypotheses and classifying over covariates. We can also expand to regressing subject age, with several methods. Finally, once we are confident in and satisfied with a method testing on this dataset, we can expand towards testing the method on the MRN114 and SWU4 datasets, as well.

### Methods
Each of the questions required code and (for the inferential, predictive, and assumption checking portions) mathematical theory. This is all explained in detail in each file, tabulated below. Here, we will discuss the methods used in each of these sections, rationalize decision made, and discuss alternatives that could have been performed instead.

| Question Type | Code |
|---------------|------|
| Descriptive | [**``./code/descriptive_and_exploratory_answers.ipynb``**](./code/descriptive_and_exploratory_answers.ipynb) |
| Exploratory | [**``./code/descriptive_and_exploratory_answers.ipynb``**](./code/descriptive_and_exploratory_answers.ipynb) |
| Inferential | [**``./code/inferential_simulation.ipynb``**](./code/inferential_simulation.ipynb) |
| Predictive  | [**``./code/classification_simulation.ipynb``**](./code/classification_simulation.ipynb) |
| Testing Assumptions | [**``./code/test_assumptions.ipynb``**](./code/test_assumptions.ipynb) |

#### Descriptive Analysis
When answering descriptive questions, we sought out values which could summarize the dataset. Our sample sizes, graph size, and amount of obviously invalid data were chosen because they would be important in virtually any downstream task. More complicated features could have also been looked at, such as dynamic range of edge weights, or distribution of genders in each dataset as well.

#### Exploratory Analysis
Three exploratory questions were answered here: average degree, average graph, and plotting the histograms of edge weight. The average degree for each graph was computed by summing the binary edge count for each graph and dividing by the number of nodes. The graphs were binarized, but not thresholded or scaled before to remove small magnitude edges. This means that the estimated degree is an upper bound estimate based on these graphs.

The mean connectome was computed simply here due to the graphs being graph matched (i.e. same nodes). The edge-weight for each location was simply averaged across all graphs. We did not do this, but perhaps should (and certainly could) for each individual dataset as well, to see if population specific mean connectomes are significantly different from one another.

There was very limited computation or design when computing the histograms.

#### Inferential Analysis
Here we needed to define a model and test statistic for our hypothesis test. We wanted to test whether or not males and females are sampled from the same distribution, so we chose a test statistic that is a function of distribution: edge probability. We could have fit a GMM or other distribution to our data and then compared them, but as a preliminary measure this enabled us to proceed easily. We also needed to choose a statistical text. We choose the Wilcoxon test because it is a non-parametric test that makes significantly fewer assumptions about the data (i.e. doesn't impose a distribution) than the t-test. In order to prove that our test in fact convered to 1 in power as the number of samples approached infinity under the alternate model (that a class conditional probability exists), and would stay at our alpha value under the null model (no relationship exists), we simulated data that have similar properties to our graphs. Shown below is a figure illustrating that this test converges as desired.

<img src="../figs/inference_power.png" data-canonical-src="../figs/inference_power.png" width="300" />

#### Predictive Analysis
Similarly to the inferential analysis, we needed to here specify a model and loss function for our classification task. The model again used edge probability as the feature. Here the loss function was simply the indicator function over assigned label by the classifer compared to true label - if the labels were the same, there was no loss; otherwise, the loss was 1. Here we tested 5 different classifiers on the data and compared their performance. Some of the tests were non-parametric (LDA, QDA), while others required some parameters to be set (K-nearest neighbour, Linear SVM, and Random Forest). The parameters chosen for each of these algorithms was not at all tuned to our data, but were the default parameters suggested by the sklearn website, where the implementations were found. Improving this, and choosing parameters that match our assumptions or expectations about our data could drastically improve the performance of these classifiers.

Shown below is a figure illustrating the performance of each of these classifiers tested on simulated data that is sampled from a distribution similar to our observed data.

<img src="../figs/classifier_performance.png" data-canonical-src="../figs/classifier_performance.png" width="300" />

#### Testing Assumptions
When performing any analysis that requires assumptions, it is wise to test the assumptions made. We made three types of assumptions here: samples are independent, samples are identical, and there exists a class conditional covariance matrix (i.e. classes have different covariances). For testing independence, we chose to look at linear dependence. We computed the covariance matrix across all samples (first this meant graphs were samples, then samples were edges within the graphs), and looked at what portion of this lay in the off diagonal. If a significant portion of the covariance matrix lay in the off diagonal, we could say that the samples were not linearly independent.

For testing whether or not samples were identically distributed, we attempted to cluster the data using a Gaussian Mixture Model while varying the number of clusters. We ran Bayesian Information Criterion (BIC) on all of the clusterings and plotted the curve of BIC values over varying dimension. Where BIC is maximized, we have found the optimal number of clusters for this data (using this clustering method). Therefore, if the ideal number of clusters is 1, we can feel confident that our data may be identically distributed. However, when the optimal BIC is at a higher number, or monotonically increasing, it suggests that our data are not identically distributed.

The final test, which asserts a class conditional covariance, was perhaps the most obvious to test. We computed the covariance of all the data in each class, and then took the difference of the two class covariance matrices. We found that the covariance matrices were very different, which lead us to believe that this assumption was in fact correct.
