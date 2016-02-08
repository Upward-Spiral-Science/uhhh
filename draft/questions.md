###Questions
We have a dataset with N<sub>i</sub> for i = 1...n.
Each N<sub>i</sub> consists of 5 attributes:
* Three coordinates x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> labelled _cx_, _cy_, and _cz_. 
* Some S<sub>i</sub>, where {S<sub>i</sub> ∈ ℝ : S<sub>i</sub> ≥ 0, ∀ i}, labelled _"synapses"_
* Some U<sub>i</sub>, where {U<sub>i</sub> ∈ ℝ : U<sub>i</sub> ≥ 0, ∀ i}, labelled _"unmasked"_.

**Descriptive**

1. What does "unmasked" represent?
2. Assuming x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> represent points in 3D space (or voxels on an image), what does it mean to say there are S<sub>i</sub> _"synapses"_ at that point? Does this represent density?
3. Could we describe the data by constructing a graph (ie Delaunay, Voronoi, MST), possibly node-weighted by density?

**Exploratory**

1. What is the mean of S<sub>i</sub>?
2. What is the variance of S<sub>i</sub>?
2. Is there a distribution that fits the outlined density or is the distribution random?
3. If so, what is it?
4. Can we produce a 3D projection of the synapses using coordinates x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> for all voxels N<sub>i</sub> in dataset D in order to visualize the density of synapses in the brain?
5. If we _can_ construct a graph, we could measure attributes. I.e. for a Voronoi tesselation, we could measure the number of edges, cyclomatic number, number of triangles, number of k-walks, spectral radius, eigenexponent, Randic index, etc.

**Inferential**
1. What kind of diversity in synapse density distribution arises within normal patient populations?
2. Is there some correlation between synapse density distribution and certain diseased states?


**Predictive** 
1. Can certain synapse density distributions predict certain disease states?

**Causal**

**Mechanistic**
