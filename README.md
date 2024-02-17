# Car-Dealerships-Full-Stack-Application

The project is divided into several modules, and below I have provided an overview of each module:-

a) Added user management to the Django application.
 
 - Implemented user management using the Django user authentication system and created a REACT frontend.

b) Implemented backend services.

 - Created a Node.js server to manage dealers and reviews using MongoDB and Dockerized it.
 - Deployed a sentiment analyzer on Code Engine.
 - Created Django models and views to manage car model and car make.
 - Created Django proxy services and views to integrate dealers and reviews together.

c) Added dynamic pages with Django templates.

 - Created a page that displays all the dealers.
 - Created a page that displays reviews for a selected dealer.
 - Created a page that lets the end user add a review for a selected dealer.

d) Implemented CI/CD, and then run and test your application

 - Set up continuous integration and delivery for code linting.
 - Run the application on Cloud IDE.
 - Tested the updated application locally.
 - Deployed the application on Kubernetes.


***Solution architecture***

The solution will consist of multiple technologies:-

1) The user interacts with the "Dealerships Website", a Django website, through a web browser.

2) The Django application provides the following microservices for the end user:

- get_cars/ - To get the list of cars from
- get_dealers/ - To get the list of dealers
- get_dealers/:state - To get dealers by state
- dealer/:id - To get dealer by id
- review/dealer/:id - To get reviews specific to a dealer
- add_review/ - To post review about a dealer

3) The Django application uses SQLite database to store the Car Make and the Car Model data.

4) The "Dealerships and Reviews Service" is an Express Mongo service running in a Docker container. It provides the following services:

- /fetchDealers - To fetch the dealers
- /fetchDealer/:id - To fetch the dealer by id
- fetchReviews - To fetch all the reviews
- fetchReview/dealer/:id - To fetch reviews for a dealer by id
- /insertReview - To insert a review

5) "Dealerships Website" interacts with the "Dealership and Reviews Service" through the "Django Proxy Service" contained within the Django Application.

6) The "Sentiment Analyzer Service" is deployed on IBM Cloud Code Engine, it provides the following service:

- /analyze/:text - To analyze the sentiment of the text passed. It returns positive, negative or neutral.

7) The "Dealerships Website" consumes the "Sentiment Analyzer Service" to analyze the sentiments of the reviews through the Django Proxy contained within the Django application.

![image](https://github.com/KingAyussh1/Car-Dealerships-Full-Stack-Application/assets/72377031/7c143785-e75d-4a64-a12c-ee4b05313448)

