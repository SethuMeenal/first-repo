TASK-1:

repeat_purchase_flag is the label - it should ideally contain the result of what we are going to find with the model - it says finally whether the customer will churn or stay.



discount_used_on_repeat_order is the leaky feature - because based on whether the customer has purchased within 30 days or not , the discount can be provided or not provided to the user, after the purchase.

As we don't need it for training or testing now, it can be removed now.



Task-2: Steps missed are,

Problem framing - it matters mainly because of the cost involved - it can be proceeded with ML approach only if ML is required.
EDA and Prepping the data - greater the quality of data , greater the precision and results
Splitting the data - Data needs to be split for training, testing and validation otherwise it would overfit when we test it with same data again.