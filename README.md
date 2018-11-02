# What Makes an Amazon Review Helpful?

## Abstract

We have a general story we would like to tell: what makes an Amazon review helpful? Useful reviews are important to Amazon because they drive sales. If Amazon can determine what reviews are helpful, then they can show or hide reviews to provide a more comfortable environment for a customer to make purchases in. Amazon already has a user-voting system to determine the usefulness of a review. We hope to discover a process to identify helpful and unhelpful reviews which could completely automate determining if a review is useful - from the moment it is posted.

Our Motivation: We've all seen Amazon listings that are plagued with unhelpful reviews. And our personal experience tells us that we are very unlikely to buy a product that has no reviews, or only has unhelpful reviews. Because of this, a helpful review can push us to make a purchase when we are on the fence. Our dataset includes images, prices, other purchases, and product information. We believe that we can use this information to draw strong conclusions about what 'makes' a review helpful.

## Research Questions

There are a few easier questions that we can answer just by looking at the dataset:
- Which words are associated with a useful review?
- Does the length of a review impact its usefulness?
- Can a user's review history predict a new reviews' helpfulness?
- Does the usefulness have a correlation to the general rating of a product?
- Are there trends over time for how many useful reviews are posted?

This question is the bread-and-butter and will take up the majority of time to answer:
- Can we predict the usefulness of a review?

## Dataset

We are going to use the Amazon reviews dataset found at [this link](http://jmcauley.ucsd.edu/data/amazon/).

This dataset has an abundance of information and metadata that we can use (83 million reviews with no duplicates!). There is 20GB of data, so we will do the processing on the ADA cluster. The data is formatted in json. We are only going to use reviews that have been written by users with at least five reviews (this is about 9.9GB of data). We have enough reviews to draw meaningful conclusions, and this subset of the data is the most relevant for the research questions we proposed.

There are a few ways that we can clean the data:
- Fix misspellings
- Standardize punctuation
- Standardize capitalization
- Remove non-unicode (or invalid) characters
- Detect and remove reviews that are not in English

## Internal Deadlines For Milestone 2

### By November 9

- Figure out how to display and load the data in the cluster
- Research what needs to be done to standardize and clean the data
- Look for the best libraries and tools to help us with our goal

### By November 16

- Divide responsibilities for the project
- Cleanup and standardize the dataset

### By November 25

- Prepare the notebook for the deadline
- Answer some of the easier questions that we have outlined earlier
- Set future deadlines and add addional questions to answer

## Questions for TAs
1. What obstacles do you anticipate we'll encounter?
2. Are there any technologies you would recommend for this specific project?
3. Is our scope realistic?
