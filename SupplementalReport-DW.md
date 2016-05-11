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
