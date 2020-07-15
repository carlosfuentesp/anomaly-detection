# Instructions for running ML pipeline

## Run the pipeline with different model parameters

Goals

* Run python pipeline locally
* Make a change and run again to see the effects

### Run the tests locally

If you want to run things locally, you can follow this recipe. If you just want
to run things with Jenkins, you can skip this. Running with Jenkins requires that
you commit and push the code changes. 

```bash
./run_tests.sh
```


Flake8 checks for style violations. We suggest you stick to standard PEP8 style
guidelines. If you use the PyCharm IDE (or other IDEs properly-configured), it will show
style violations while you type. If however, you miss some, this Flake8 checker will
cause it to fail the test stage. If that is undesirable, it can be removed 
from run_tests.sh.

Once the shell has been activated, which you can do with 
```bash
source .venv/bin/activate
```

you can run the ML pipeline with

```bash
python3 run_python_script.py pipeline
```

## ML Flow

Open your browser to the following page to see MLflow.

[http://localhost:12000/#/](http://localhost:12000/#/)

On the left, under experiments, click on jenkins to see the jobs launched from 
the jenkins server.

If you run the pipeline through Jenkins at least once, you will see a list of runs in the 
table with the metric r2_score on the far right. Click on the date field to se more information.

Artifacts like plots can be added. We haven't implemented this yet though. 
The model can also be saved in mlflow as an artifact.

One of the most important thing recorded is the git commit hash. So if you ever need to roll back
to a previous model, you can check out that version of the code or at least check the parameters
to see what they were.


