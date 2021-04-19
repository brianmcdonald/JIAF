# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
# !conda install openpyxl -y


# %%
input = pd.read_excel('JIAF template - Scenario A.xlsx', sheet_name='hh data')

# %%
input

# %% [markdown]
# ## Check input data for errors
# - Check that required variables are present
# - Check for missing values
# - Check for missing indicator values
#
# For the 'data' tab, each row represents a unique household. For the 'area data' tab each row represents an indicator for its most detailed available admin-level.

# %% [markdown]
# ## Reconcile area-level indicators to corresponding households
# To use area-level indicator with household-lvel data, each area level indicator must be attached to housholds in the matching lowest-level admin area and population group.

# %% [markdown]
# ## Aggregate severity scores for all indicators for each household
# The **mean of max 4 method** is the arithemetic mean of the 4 indicators with the highest severity score. The resulting number represent the overall severity for each household.

# %% [markdown]
# ## Check if any "Critical Indicator" (see section 4.1.4) severity score is higher than the computed severity score.
# Households where the computed severity score is lower than any critical indicator are hightlighted for review in the expert judgement stage.
# Note: It's unclear whether this informs a review prior to the end expert judgement session

# %% [markdown]
# ## Aggregate households to desired admin-level and population groups

# %% [markdown]
# ## Append Assistance, Risk and Projections info to inform expert judgement
# Note to self: It is currently unclear how to incorportate existing assistance, risk and projections correctly into the hh and area-level data. Current issues include:
# - Marking "Already ongoing assistance as Yes/No is meaningless without knowing what assitance it is and if its related to the indcators representing the needs.
# - Information on risks at the HH-level and some admin-levels would need summarization to be used in the Risk column.
# - Projections could include intentions survey data, but only if incorporated into the same HH survey.

# %%
# !conda install -c conda-forge jupytext -y


# %%
