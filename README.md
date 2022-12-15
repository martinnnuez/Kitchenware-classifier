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

D) The [test-aws](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/test-aws.py) in charged of evaluating if the model deployment to AWS is working properly. 

D) The [test-local](https://github.com/martinnnuez/Kitchenware-classifier/blob/master/test-local.py) in charged of evaluating if the model deployment locally is working properly. 

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

If you prefer not to run all the code for the development of the model, which is slow and tedious, go to the **laizy/fast start section**.

3 - To train the final model run final_model.py, select a model and continue.

```bash
pipenv run python final_model.py
```

If you prefer to install the dependencies locally, run:

```bash
pipenv install
``` 
4 - Transform the selected final model to a tensorflow lite instance model. To achieve this run the tensorflow-lite-instance.py script. 
Remember to change the name of the model to the one you previously train and save.

```bash
pipenv run python tensorflow-lite-instance.py
```

Once we have created the tensorflow lite instance of our developed model we can follow the steps to make the model deployment. 

## Laizy/fast start 

A model example is uploaded to the repository in case you do not have time to train and select the models. Also the model transformation to tensorflow-lite-instance has been performed.

* Final model trained: **EfficientNetB411_0.970.h5**

* Tensorflow-lite-instance: **kitchen.tflite**

## Test lambda function code

Run the following code in the termina, to complete the event url, access https://www.kaggle.com/competitions/kitchenware-classification/data , look for an image and copy its url access link and paste it. Then try out the function classification. 

If the example web page is not expired, use it as example. 

* Example: https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221212%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221212T152149Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=734c5c334ce764fd60340d524e4a50ec3e5e35b44850f43100da2e5d75efaf8dafc3ae5d82f3caee653aee184aa75cdc183e2587a5689b5d25c16f0d2ead957e15f579305c68448331b63c8a78b1a67e67947cae95efb7dc75a1d8ad0ad8a20a41119cc7cfa9ca538be5658b279ac354d915be9bc6d125ff83b9c742cd1649d7dd53b29655b094b14077fa8e71ecaf03c8374d901ec4a20eb7768c4ec084994a265decfc02b49f48b9cddc685dffc8a328e7a1a909835136469410607f846a3f6d5f6f0ff0215d65256cfcc349a4fe08fc82890e76620b4e4e7584c4f61aa06ce8c529a98d906b88ff87fa2b89641f3cae5e0598a186523e7cce9ed96b07bcd7

```bash
ipython
import lambda_function

# event = {"url":''}

event = {"url":'https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221212%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221212T152149Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=734c5c334ce764fd60340d524e4a50ec3e5e35b44850f43100da2e5d75efaf8dafc3ae5d82f3caee653aee184aa75cdc183e2587a5689b5d25c16f0d2ead957e15f579305c68448331b63c8a78b1a67e67947cae95efb7dc75a1d8ad0ad8a20a41119cc7cfa9ca538be5658b279ac354d915be9bc6d125ff83b9c742cd1649d7dd53b29655b094b14077fa8e71ecaf03c8374d901ec4a20eb7768c4ec084994a265decfc02b49f48b9cddc685dffc8a328e7a1a909835136469410607f846a3f6d5f6f0ff0215d65256cfcc349a4fe08fc82890e76620b4e4e7584c4f61aa06ce8c529a98d906b88ff87fa2b89641f3cae5e0598a186523e7cce9ed96b07bcd7'}

lambda_function.lambda_handler(event,None)
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

* Remember to add an actualized url to the test-local.py script to access an image to classify, if the example image link has expired. To look for an image you should access https://www.kaggle.com/competitions/kitchenware-classification/data .

Once copied the url you need to paste and replace the one in test-local.py.

```bash
python test-local.py
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

* Remember to add an actualized url to the test-local.py script to access an image to classify, if the example image link has expired. To look for an image you should access https://www.kaggle.com/competitions/kitchenware-classification/data .


{
    "url": ""
    
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

* Remember to add an actualized url to the test-local.py script to access an image to classify, if the example image link has expired. To look for an image you should access https://www.kaggle.com/competitions/kitchenware-classification/data .

Once copied the url you need to paste and replace the one in test-aws.py.

* Later: 

```bash
python test-aws.py
```
