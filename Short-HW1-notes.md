# Short HMW 1 Part 1

Does being smarter (IQ) have any real effect on how diligent someone is? 
Using survey data from School A.

This is really a question about whether two variables are related, and linear regression is the tool for testing that.

I'm fitting a linear regression model:
Y_i = β0 + β1 * X_i + ε_i

Let X = IQ and Y = diligence. 
β1 answers the Q (slope), i.e. how much diligence 
changes per unit of IQ. If β1 is basically zero, IQ and diligence 
aren't related. If it's clearly nonzero, they are.

Any sample of data will produce some slope. Typically this is too noisy. So I am using Hypothesis testing further.
- H0: β1 = 0: no real relationship, whatever slope I see is noise
- H1: β1 ≠ 0: there's a genuine relationship
