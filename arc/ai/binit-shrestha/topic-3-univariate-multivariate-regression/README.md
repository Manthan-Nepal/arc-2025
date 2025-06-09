## Topic 3

## Univariate and Multivariate Linear Regression

### **For univariate, did 2 tasks**
- First was building univariate linear regression model from scratch
    - Defined each function (loss, gradient descent, fit) individually
- Second was using the SKLearn library
    - Only needed to split the data, everything was handled automatically
- Metrics were compared, SKLearn method was slightly better
    - Scratch method was ran until the loss stagnated

### **For multivariate, most of the time went into EDA**
- Although there were only 5-6 features for the target Price
    - Data wrangling, visualization was done to observe the data
    - Transformations were done as per need
- Also utilized SKLearn for training, ended up using RandomForestRegressor
- The model outcome right now isn't  ideal since, R2 score is 0.5237