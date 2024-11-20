# G1S8_Project-3_Python-for-DS
Domain: Finance and Banking
Objective: Automate the loan eligibility prediction process for Dream Housing Finance to enhance efficiency and reduce manual validation effort.

Project Summary:
Developed and deployed a loan eligibility prediction model for Dream Housing Finance Company using a logistic regression classification algorithm. The project involved end-to-end development, starting from data preprocessing and model building to deployment via a Flask web application. The web application provides a user-friendly interface for customers to register, log in, input personal and financial details, and check their loan eligibility instantly.

The model was trained on a dataset containing 13 attributes, including demographics, income details, loan amount, and credit history, with Loan Status as the target variable. Key steps included handling missing data, encoding categorical variables, scaling numerical features, and optimizing model accuracy.

The Flask application integrates with a MySQL database to manage user authentication and stores user details. The model was pickled for seamless integration with the application, enabling real-time predictions.

Key Features:

User-friendly interface for registration, login, and loan prediction.
Automated backend processes including data validation and loan eligibility prediction.
Integration with MySQL for user management.
Secure and scalable application architecture for deployment.
Tools and Technologies: Python (Flask, Sklearn, Pandas, NumPy), MySQL, Logistic Regression, Data Visualization, Pickle.

This project showcases my ability to combine data science techniques with web development to solve real-world business problems in the Finance and Banking domain.

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

