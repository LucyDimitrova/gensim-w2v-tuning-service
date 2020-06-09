## Django service for hyperparameter tuning of a Gensim model

### Endpoints

The service exposes 3 endpoints:

#### POST /tune/iteration/create 

Example request body:

{ "params": { "param1": "value1", "param2": [1, 10] } }

Example response:

{ "success": True, "message": "Iteration created.", "iterationId": 1 }

#### POST /tune/iteration/start/:iteration_id

Query param - iteration_id

#### GET /tune/iteration/performance/:iteration_id

Query param - iteration_id