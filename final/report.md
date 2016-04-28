- find orientation in dataset
- ooh, what are these peaks / troughs?
- once we know where the bounds of each layer are (approx), what qualities differ between layers?
- look across different axes, but we think y is most interesting
- Overlay image

# Final Report

## Abstract
The field of connectomics suffers from increasingly large datasets without proportionally improving algorithms with which to process them. In order to keep up with the pace of embiggening data, it is commonly useful to reduce the size or complexity of a dataset by either downsampling or reducing the question of what is being inspected. For instance, the 2011 *M. musculus* V1 dataset from *Network anatomy and in vivo physiology of visual cortical neurons* (Bock et al)<sup id="r-dbock">[1](f-dbock)</sup> is over 20TB at native resolution. This volume of data is unmanageable on a conventional personal computer, and so an informed "downsampling" was performed wherein computer vision algorithms computationally detected synapses, and the volume was then spatially downsampled, with each supervoxel being replaced by the number of subvoxels within it that were taken up by synapse volume.

During this semester, we developed strategies to illustrate how **meaningful neuroscientific analysis can still be performed on this reduced dataset**. We beleive that this method of reduction (from EM spatial data to synaptic volume data) may not be suitable for all types of inquiry, but **for certain investigations, such as determining the dataset's orientation and location in cortical space, this comparatively tiny (MB instead of TB) dataset is, we posit, sufficient**.


## Background
### Overview
Our data are taken from the 2011 *M. musculus* V1 dataset from *Network anatomy and in vivo physiology of visual cortical neurons* (Bock et al)<sup id="r-dbock">[1](f-dbock)</sup>.

### Description of Data
stuff about data (copy pasta)


## Preliminary Data Exploration
i.e. distribution of data, mean, var, etc 

## Preliminary Data Analysis
histogram(?), heatmaps of 2D MIP

## Establishing Dataset 3D Orientation

-----
## Footnotes
<b id="f-dbock">1</b> [Bock et al. Nature (2011)](http://reid.med.harvard.edu/pdf/Bock-Lee-etal-Reid-2011-Nature.pdf) [↩](#"r-dbock")


