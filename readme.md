This is a fourth project in our training.
We were set to develop an API that can provide access to a webshop.

This includes an API Gateway that links to Cloud Functions that have access to a PostgreSQL database.
When the user checks out, a receipt is sent to the customer by email.

The API supports all CRUD operations for four different tables in database.
Sensitive information is hidden in GCP Secret Manager. Cloud Functions have access to them.

All infrastructure can be created through Terraform.
CI/CD pipeline mirrors the GitHub repository to GCP Cloud Source Repository. Cloud Build can then build any changes to infrastructure through Terraform.