# G1S8_Project-3_Python-for-DS
Classification model,pickled and deployed using flask(loan predictor)
Domain:
○ Finance and Banking.
Context:
Dream Housing Finance company deals in all home loans. They have presence
across all urban, semi urban and rural areas. Customers first apply for a home
loan after that company manually validates the customer eligibility for loan.
Company wants to automate the loan eligibility process based on customer
detail provided while filling the details online.
They need a web application where a user can access their website and
register, login, and enter the required details such as Gender, Marital Status,
Education, Number of Dependents, Income, Loan Amount, Credit History and
others for checking the eligibility for the home loan.

Objective of Project:Need to predict customer eligibility to avail a loan.

Data Set description:
The data set contains 13 attributes of which Loan Status is the target variable.
1.Loan ID Unique- Loan ID
2. Gender- Male or Female
3. Married Applicant- married (Y/N)
4. Dependents- Number of dependents
5. Self employed- Self employed (Y/N)
6. Education -Graduate/Undergraduate
7. Applicant -Income Applicant income (in dollars)
8. Co Applicant Income- Co Applicant Income (in dollars)
9. Loan Amount- Loan amount in thousands (in dollars)
10. Loan Amount -Term Term of loan in months
11. Credit History -Credit history meets guidelines Yes/No(1/0)
12. Property area -Urban/Semi Urban/Rural
13. Loan Status (Target)

Steps undertaken:

1.Import the data set and understand the data sample.
2.Checked for missing values and drop redundant column :- loan id dropped
3.There were missing values in both categorical data and numeric data which was replaced  by taking the mode in categorical and mean in numeric data
4.Visualised the loan status with respect to various categorical features.
5.Encoded  the categorical variables manually
6. Using sklearn model_selection train_test_split split data into training and test data
7. Using Standard Scaler scaled data
8. Performed Logistic Regression and checked accuracy on both train and test data sets
9. Pickled the model and saved it in Flask app model1.pkl file
10.Created application file that is designed to call some of the implemented APIs and methods, such as connecting to the MYSQL database and creating a table for the database, and APIs such as user to register, login, enter_details, predict, and logout.
11.Once app is run the user can then signup enter his  details and predict if he can get a loan or not.
