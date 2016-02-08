###Questions
We have a dataset with N<sub>i</sub> for i = 1...n.
Each N<sub>i</sub> consists of 5 attributes:
* Three coordinates x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> labelled _cx_, _cy_, and _cz_. 
* Some S<sub>i</sub>, where {S<sub>i</sub> ∈ ℝ : S<sub>i</sub> ≥ 0, ∀ i}, labelled _"synapses"_
* Some U<sub>i</sub>, where {U<sub>i</sub> ∈ ℝ : U<sub>i</sub> ≥ 0, ∀ i}, labelled _"unmasked"_.

**Descriptive**

1. What does "unmasked" represent?
2. Assuming x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> represent points in 3D space (or voxels on an image), what does it mean to say there are S<sub>i</sub> _"synapses"_ at that point? Does this represent density?
3. Can we produce a 3D projection of the synapses using coordinates x_i, y_i, z_i for all voxels Ni in dataset D in order to visualize the density of synapses in the brain

**Exploratory**

1. Is there a distribution that fits the outlined density or is the distribution random
2. If so, what is it?

**Inferential**

**Predictive** 

**Causal**

**Mechanistic**
