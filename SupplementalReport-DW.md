# Supplemental Final Report
***David West***<br/>
May 12, 2016

-------------------

**Table of Contents:**
- [Overview](./SupplementalReport-DW.md.md#overview)
- [Description of Region Adjacency Graphs](./SupplementalReport-DW.md#Description of Region Adjacency Graphs (RAG))
  - [Decriptive Analysis](./final_report.md#descriptive-analysis)
  - [Exploratory Analysis](./final_report.md#exploratory-analysis)
  - [Inferential Analysis](./final_report.md#inferential-analysis)
  - [Predictive Analysis](./final_report.md#predictive-analysis)
  - [Testing Assumptions](./final_report.md#testing-assumptions)
  - [Extended Exploratory Analysis](./final_report.md#extended-exploratory-analysis)
  - [Dimensionality Reduction](./final_report.md#dimensionality-reduction)
- [Methods](./final_report.md#methods)
  - [Decriptive Analysis](./final_report.md#descriptive-analysis-1)
  - [Exploratory Analysis](./final_report.md#exploratory-analysis-1)
  - [Inferential Analysis](./final_report.md#inferential-analysis-1)
  - [Predictive Analysis](./final_report.md#predictive-analysis-1)
  - [Testing Assumptions](./final_report.md#testing-assumptions-1)
  - [Extended Exploratory Analysis](./final_report.md#extended-exploratory-analysis-1)
  - [Dimensionality Reduction](./final_report.md#dimensionality-reduction-1)

## Overview
This supplemental final report explores the synaptic density data further. The [primary final report](https://github.com/Upward-Spiral-Science/uhhh/blob/master/FinalReport.md#final-report-uhhh) was prepared on May 5, 2016, and examines data taken from 2011 M. musculus V1 dataset from Network anatomy and in vivo physiology of visual cortical neurons (Bock et al). Amongst a few key insights, a primary finding of the initial analyses was that the y-axis of the 3D volume was aligned with the z-axis of the brain, or the axis along which cortical layers vary. The report found key inflection points in synaptic density down the volume's y-axis. The report also offered a cursory analysis of clustering and trends in synaptic distribution down the y-axis, as well as through the x and z axes.

As tissue varies down the cortical layers, multiple properties become vary. 

Here, we'll perform various analysis by constructing graphs and measure properties of those graphs to learn more about the data

## Description of Region Adjacency Graphs (RAG)
In the past we've considered density information alone (ie analysis density histogram distribution) and above we are considering only spacial information, which doesn't say anything. To construct a graph that consider both spacial and density information, we'll use a Region Adjacency Graph (RAG). RAGs are used largely in image processing, and it makes sense for our data to look more like an image. Since the data is evenly spaced, the absolute locations of the voxels don't matter. We can use the index in the matrix to represent spacial location, with the value at each pixel being the synapse density at that voxel. We've done this before in "real volume"

In RAGs, two nodes are considered as neighbor if they are close in proximity (separated by a small number of pixels/voxels) in the horizontal or vertical direction.

<img src="./docs/figures/plot_rag_1.png" width="400">

Since our data includes density values at each node (voxel, or pixel since we're looking at y-layers), we can weight by the inverse of density difference between two nodes. Inverse because strongly connected nodes should be close in weight. We have number of synapses S<sub>i</sub> at nodes $i$ and define weights $w$ between the nodes:

$$w = \dfrac{1}{S_i - S_{i+1}}$$

