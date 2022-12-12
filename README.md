# Capstone 1 project for the Machine Learning Zoomcamp

## Objectives of the project

* Think of a problem that's interesting for you and find a dataset for that
* Describe this problem and explain how a model could be used
* Prepare the data and doing EDA, analyze important features
* Train multiple models, tune their performance and select the best model
* Export the notebook into a script
* Put your model into a web service and deploy it locally with Docker
* Bonus points for deploying the service to the cloud

# Kitchenware Classification

## Problem description

It is an image classification competition organized by DataTalks.Club.

* https://datatalks.club/

In this competition you need to classify images of different kitchenware items into 6 classes:

* cups
* glasses
* plates
* spoons
* forks
* knives

Competition web page:

https://www.kaggle.com/competitions/kitchenware-classification

Dataset download:

https://www.kaggle.com/competitions/kitchenware-classification/data

or 

```bash
kaggle competitions download -c kitchenware-classification
```

## Files

A) The first file is the [notebook](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/notebook.ipynb) where the data preparation, exploratory data analysis, model selection process and hyperparameter tuning is done.

B) The [final_model](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/final_model.py) file is the file in charged of performing the final model training with the best hyperparameters found while performing the model optimization. Remember after training, all the models are going to be saved in to the directory, you need to select the best performing model and save its name. 

C) The [tensorflow-lite-instance](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/tensorflow-lite-instance.py) file is the one that produces transformation of our previous trained model to a tensorflow lite instance. Remember to change the name of the model to the one you have previously trained and selected.  

D) The [test](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/test.py) in charged of evaluating if the model is working properly. If you comment the Locally deployment url and uncomment the AWS deployment url you can test out how the lambda function deployment works.  

E) The [lambda_function](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/lambda_function.py) file is the one that allows to implement the tensorflow lite instance as a lambda function for AWS.  

# Instructions to run

## Complete and simple way:

1- Clone github repo:

```bash
git clone repo name
```

2 - Open a terminal and navigate to the directory. Then download the data sets for the development of this problem.
All the needed files can be found at: 

https://www.kaggle.com/competitions/kitchenware-classification/data

The needed files are: 

* train.csv - the training set (Image IDs and classes)
* test.csv - the test set (Just image IDs)
* images/ - the images in the JPEG format

Check all the steps of exploratory data analisys and model development followed in notebook.ipynb, and then continue with the model training. 

3 - To train the final model run final_model.py, select and save a model.

```bash
pipenv run python final_model.py
```

If you prefer to install the dependencies locally, run:

```bash
pipenv install
``` 
4 - Transform the trained final model to a tensorflow lite instance model. To achieve this run the tensorflow-lite-instance.py script. 
Remember to change the name of the model to the one you previously train and save.

```bash
pipenv run python tensorflow-lite-instance.py
```

Once we have created the tensorflow lite instance of our developed model we can follow the steps to make the model deployment. 

## Test lambda function code

```bash
ipython
import lambda_function

# Cup image
event = {"url":'https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221207T161008Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=2603df96a71f8ef00d6bea2e1540626e057b8874de18601df650ef695d6a677f7705ca0397cfd6c8f0c55d87c250db99ae4551065907e0e734e61beb0a7f2d8fcab9c099c49c7ff14fb69f784c57b45865360f49559b8913ffa6b777238085091738ad6af68561f96dbd571b7dbf31f797424ad05e1b808c979674f8b2eafc43924824812b71b1710b5e8bddcf6426e98bd9195b1cb1da9b6493e5ee2cb03d19f8a76cfa292b29672f5052b13925ce38e0185924f048a0f1e398776f6e0cb1bca879ed239f52e2a300b2752fe3cf89d2d9ffd5724d9cc10aa344b66328e9bf372e9f5aeb8a0ec3e5c22af607f4c8cd217bc0843ee16b8cd44954d2173c937c2b'}

lambda_function.predict(event,None)
```

## Test Docker image locally

1. Docker build
```bash
docker build -t kitchen-model .
```
2. Test image
```bash
docker run -it --rm -p 8080:8080 kitchen-model:latest
```

3. Open a new termianl and run
```bash
python test.py
```

## Productization using lambda function

1. Publish previous created docker image in to an Amazon ECR (Elastic Container Registry):

```bash
pip install awscli

aws ecr create-repository --repository-name kitchenware-image
```

2. Once the ECR is created, retrieve an authentication token and authenticate your Docker client to the registry.
```bash
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 889921088684.dkr.ecr.us-east-1.amazonaws.com
```

3. Create a Docker image with the following command.
```bash
docker build -t kitchen-model .
```

4. When the build is complete, tag the image so you can push it to this repository:
```bash
docker tag kitchen-model:latest 889921088684.dkr.ecr.us-east-1.amazonaws.com/kitchenware-image:latest
```

5. Run the following command to push this image to the newly created AWS repository:
```bash
sudo docker push 889921088684.dkr.ecr.us-east-1.amazonaws.com/kitchenware-image:latest
```

6. Once the image is pushed, we need to create the lambda function.

* Enter to your AWS account and look for lambda.

* Create a function.

* Container image. 

* Give a name.

* Select the image we just upload to the ECR. 

* Create function. 

7. Test the function we have just created. 

* Name: cup

* Event: 

{
    "url": "https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221207T161008Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=2603df96a71f8ef00d6bea2e1540626e057b8874de18601df650ef695d6a677f7705ca0397cfd6c8f0c55d87c250db99ae4551065907e0e734e61beb0a7f2d8fcab9c099c49c7ff14fb69f784c57b45865360f49559b8913ffa6b777238085091738ad6af68561f96dbd571b7dbf31f797424ad05e1b808c979674f8b2eafc43924824812b71b1710b5e8bddcf6426e98bd9195b1cb1da9b6493e5ee2cb03d19f8a76cfa292b29672f5052b13925ce38e0185924f048a0f1e398776f6e0cb1bca879ed239f52e2a300b2752fe3cf89d2d9ffd5724d9cc10aa344b66328e9bf372e9f5aeb8a0ec3e5c22af607f4c8cd217bc0843ee16b8cd44954d2173c937c2b"
    
}

* Configuration:
    * Edit:
        * Increase Timeout.
        * Increase Memory.

8. Need to expose the lambda function like a web service via API Gateway.

* Go to AWS API Gateway. 

* Create API.

* Select REST API.

* Configurate API: name,...

* Create API.

9. Once is created:

* Actions:
    * Create Resource: 
        * Configure resourse.

* Create resource. 

* Actions: 
    * Create Method:
        * Select and create a POST method. 
        * Configure.

* Accept permision to lambda function. 

* Click the test blink and try it out with the previos json.

10. Deploy API Gateway:

* Actions:
    * Deploy API:
        * Give a name and deploy. 

Now we have a url for comunicating with the API. 

I replace it in test.py and try it out:

* First you need to uncomment it and comment the other url.

* Remember to add a /method_name to the url AWS provided. 

* Later: 

```bash
python test.py
```
