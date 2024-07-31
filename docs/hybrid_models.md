# Hybrid Models

## Overview
Hybrid models combine different machine learning techniques to improve performance and robustness. MachiEm allows you to easily integrate and manage hybrid models.

## Example: Combining Models

```python
from hybrid_models import combine_models

# Example models
model1 = ...
model2 = ...

# Combine the models
hybrid_model = combine_models(model1, model2)
