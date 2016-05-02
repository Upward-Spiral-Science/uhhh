- find orientation in dataset
- ooh, what are these peaks / troughs?
- once we know where the bounds of each layer are (approx), what qualities differ between layers?
- look across different axes, but we think y is most interesting
- Overlay image

- figures we want:
	- histogram in each axis
	- MIP
	- 3d (@dw)...added in figures
	- Some screenshots of the actual data
- Original histogram
- Histogram considering unmasked
- Fitting a gaussian
- mean, variance of the data

# Final Report

## Abstract
The field of connectomics suffers from increasingly large datasets without proportionally improving algorithms with which to process them. In order to keep up with the pace of embiggening data, it is commonly useful to reduce the size or complexity of a dataset by either downsampling or reducing the question of what is being inspected. For instance, the 2011 *M. musculus* V1 dataset from *Network anatomy and in vivo physiology of visual cortical neurons* (Bock et al)<sup id="r-dbock">[1](f-dbock)</sup> is over 20TB at native resolution. This volume of data is unmanageable on a conventional personal computer, and so an informed "downsampling" was performed wherein computer vision algorithms computationally detected synapses, and the volume was then spatially downsampled, with each supervoxel being replaced by the number of subvoxels within it that were taken up by synapse volume.

During this semester, we developed strategies to illustrate how **meaningful neuroscientific analysis can still be performed on this reduced dataset**. We beleive that this method of reduction (from EM spatial data to synaptic volume data) may not be suitable for all types of inquiry, but **for certain investigations, such as determining the dataset's orientation and location in cortical space, this comparatively tiny (MB instead of TB) dataset is, we posit, sufficient**.


## Background
### Overview
Our data are taken from the 2011 *M. musculus* V1 dataset from *Network anatomy and in vivo physiology of visual cortical neurons* (Bock et al)<sup id="r-dbock">[1](f-dbock)</sup>. The data are simplified by downsampling, where the value of a downsampled voxel is the sum of all of its constituent voxels. 

## Significance
We posit that synaptic density may serve as an indicator of computationally important volumes of brain tissue: When generating a map of connectivity, it is these areas of high synaptic density that are most influential to the resultant graph.

Synaptic density may also be an indicator of a greater overarching pattern or layout to areas of highly structured brain tissue (namely, cortex). The concept of cortical motifs — recurrent cortical machinery — is a highly contested concept in modern computational neuroscience. The neuroscience community widely agrees that such motifs exist in V1 (hypercolumns) where they represent retinotopic layout, and PAC (cochlear tonotopy). However, the existence of these columns in other, non-sensory cortex remains up for debate. If patterns can be found in synaptic density across layers of cortex (a simpler task than inspecting the tissue or connectome itself), then this lends credence to the theory that cortical columns extend beyond primary sensory areas such as V1 and PAC.

Such information might be useful for establishing a baseline understanding of synaptic density that might, in future studies, be used to understand diseases thought to arise in the cortex. Discrepencies between the model described by this analysis and models describing a clinical population could yield understanding of a diseased state (i.e. Alzheimers, Dementia).

### Description of Data
#### Defining `unmasked`
Our first inquiry was to formally define the meaning of the `unmasked` keyword in our input data. Before we embarked on any meaningful analyses, we needed to understand the fundamental definition of our descriptor. First, we discovered that $min(\texttt{unmasked})=0$ and $max(\texttt{unmasked})=165789$. This upper bound seems like an arbitrary value, and we were unable to characterize it meaningfully.<sup id="r-what-165789">[1](f-what-165789)</sup> <!-- TODO: Characterize it meaningfully. -->

We also inspected the distribution of the `unmasked` values ([**Fig. 1**](#fig-1).)

> ![](http://i.imgur.com/2T5CcGo.png)
> <small><b>Figure 1.</b> *Histogram of the distribution of the `unmasked` descriptor.* From the figure above, it is clear that there are points of high intensity at around the 150,000 point and higher. There is also an immense peak at $0$, suggesting that a large portion of the computer-recognized data were considered insignificant after human intervention.</small>


Our next goal was to understand the meaning of the metric. Through personal communication, we established that `unmasked` describes *the number of voxels within the supervoxel that fell in an area that should be considered.* That is, if `unmasked` is zero, then the cell should be ignored entirely. We found that the values of all cells with an `unmasked` value of $0$ were already zero.


## Preliminary Data Exploration
Our first forays into the data were to characterize the different columns of our raw csv. We began this process by determining that the $x$, $y$, and $z$ columns represented coordinates — a safe assumption, as we knew that this dataset represented spatial data. However, we did not yet know the orientation of the data volume in 3D (cortical) space. (For comments on this, see the section on 3D orientation, below).

We first plotted our volume by binning nearest synapse-groups, and scaling by count (and by proxy, density). These plots are provided below (Figure 2).

> ![](http://imgur.com/QGkJTjm.png)
> <img src="http://imgur.com/EwTgPwc.png" alt="Drawing" style="width: 200px;"/> <img src="http://imgur.com/YotRb5V.png" alt="Drawing" style="width: 200px;"/> <img src="http://imgur.com/RMtPzQS.png" alt="Drawing" style="width: 200px;"/>
> <small><b>Figure 2.</b> 3D visualization of synapse density. In this figure it is clear that there are zones of high density (see the $xy$ plot, third of the three subplots) and zones of low density. It is very clear from these alone that, qualitatively, synaptic distribution in cortex is non-uniform.</small>

We then established other characterizations of our data: We calculated the [mean](https://github.com/Upward-Spiral-Science/uhhh/blob/master/code/Mean%20of%20Si.ipynb) and [variance](https://github.com/Upward-Spiral-Science/uhhh/blob/master/code/Var%20of%20Si.ipynb) of the $s_i$ synaptic distribution for all layers. We later reproduced this calculation for each layer along the $y$ axis (for reasons explained in the [3D orientation section](#establishing-dataset-3d-orientation)).

> <img src="http://s32.postimg.org/pydpjjvf9/Synapse_Histogram.png" alt="Drawing" style="width: 400px;"/>

## Preliminary Data Analysis
histogram(?), heatmaps of 2D MIP


## Rejecting H<sub>o</sub>, Synapse Uniformity


## Establishing Dataset 3D Orientation





## Advanced Analytics (better name)


-----

## Footnotes
1. [Bock et al. Nature (2011)](http://reid.med.harvard.edu/pdf/Bock-Lee-etal-Reid-2011-Nature.pdf) [↩](#"r-dbock")
1. The closest power of two (without going over) is $2^{18}=262,144$ which is wildly higher than the $165,789$ value.  [↩](#"r-what-165789")


