# 3D Distribution of Synapses in Cortex

*Richie Mishaan, David West, Jordan Matelsky*

-------------


### Opportunity
A 2011 study _Network anatomy and in vivo physiology of visual cortical neurons_ produced a data set that describes the number of synapses within particular voxels of a 3D reconstructed cortex section. For example:

```
cx,cy,cz,unmasked,synapses
19,1369,55,5063,0
19,1369,166,3576,0
19,1369,277,4561,0
19,1369,388,1521,0
19,1369,499,1521,0
19,1369,610,14940,17
19,1369,721,1521,0
19,1369,832,4563,0
...
```

[data source](https://raw.githubusercontent.com/Upward-Spiral-Science/data/master/syn-density/output.csv)

These data describe synapse location in a large neuroscience volume (as annotated in the *Bock 2011* paper dataset). We propose that these data may be useful for understanding synaptic density and distribution in 3D throughout a volume of examined cortex. Through the analysis of these data, we anticipate developing early hypotheses to model synaptic distribution throughout mammalian sensory cortex, which can later be substantiated in larger volumes.

This publication provides us with one of the (historically) first opportunities to examine synapse distributions over a ground-truth sample of 3D data. Using recently-published toolkits such as NeuroData, we anticipate comparing our numeric data to spatial (image) data to propose biologically meaningful hypotheses.


### Significance
Synaptic density is an indicator of *"meaningful"* areas of cortex. That is, an area with density $d=0$ is not computationally important when considering neural interconnectivity. Areas rich in synapses, on the other hand, are *highly* relevant, as they are the interfaces between neurons, and thus represent the computational machinery of the brain.<sup>[1](#_f1)</sup> Thus, generating a graph or network representation of the brain — an enormous task — can be greatly reduced in size-complexity by effectively ignoring these low-density, irrelevant areas.

Synaptic density may also be an indicator of a greater overarching pattern or layout to areas of highly structured brain tissue (namely, cortex). The concept of cortical motifs — recurrent cortical machinery — is a highly contested concept in modern computational neuroscience. The neuroscience community widely agrees that such motifs exist in V1 (hypercolumns) where they represent retinotopic layout, and PAC (cochlear tonotopy). However, the existence of these columns in other, non-sensory cortex remains up for debate. If patterns can be found in synaptic density across layers of cortex (a simpler task than inspecting the tissue or connectome itself), then this lends credence to the theory that cortical columns extend beyond primary sensory areas such as V1 and PAC.

Such information might be useful for establishing a baseline understanding of synaptic density that might, in future studies, be used to understand diseases thought to arise in the cortex. Discrepancies between the model described by this analysis and models describing a clinical population could yield understanding of a diseased state (i.e. Alzheimers, Dementia).


### Feasibility
The current state of technology allows us to perform large-scale image- and data-processing on large volumes of data. On a personal computer, it is possible to process terabytes of data in a reasonable ($O(weeks)$) amount of time. Synaptic location information can be reduced to mere bytes per synapse if each is represented by a simple tuple such as centroid-coordinates (e.g. $[c_x \ c_y \ c_z]$).

### Innovation



https://github.com/Upward-Spiral-Science/Syllabus/blob/master/assignment1.md


<small>
> From annotated electron microscopy (EM) images we can analyze properties of neurons and organelles, including the distribution of synapses between neurons in space. Are synapses evenly distributed in the cortex? If not, what distribution are they sampled from?
>
> http://www.nature.com/nature/journal/v471/n7337/abs/nature09802.html
>
> http://www.ncbi.nlm.nih.gov/pubmed/25206325
</small>

#### Footnotes
<a name="_f1">1</a>: This relies on the assumption that neural communication is performed entirely at the synaptic cleft, and not in the neuron body or membrane. Because the available biological data are post-mortem and these non-visual locations cannot be expressed in imagery, we must rely exclusively on image-visible representations, and thus synapses are our primary target.
