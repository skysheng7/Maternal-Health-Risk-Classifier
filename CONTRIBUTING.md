# Contributing to the project

We welcome any input, feedback, bug reports and contributions via the [project's GitHub Repository](https://github.com/GloriaYi/Maternal-Health-Risk-Classifier).

All contributions, suggestions and feedback you submitted are accepted under the [Project's license](LICENSE). You represent that if you do not own copyright in the code that you have the authority to submit it under the [Project's license](LICENSE). All feedback, suggestions or contributions are not confidential. The project abides by the [UBC MDS Code of Conduct](https://ubc-mds.github.io/resources_pages/code_of_conduct/).

## How to contribute

### Setting up the environment

Fork the `Maternal-Health-Risk-Classifier` repository on GitHub and then clone the fork to your local machine:

``` bash
git clone https://github.com/YOUR-USERNAME/Maternal-Health-Risk-Classifier.git
```

Navigate to the root of the project directory:

``` bash
cd Maternal-Health-Risk-Classifier
```

#### Docker Setup

For more information about the project dependencies and environment, see [README.md](README.md).
If you are using Windows or Mac, make sure Docker Desktop is running.

Start the Docker container by running:

``` bash
make up
```

This will build and launch the Jupyter Lab environment. Browse to http://localhost:8886/ to access Jupyter Lab.

To run the data analysis, open a terminal and run the following commands:

```
python scripts/download_data.py \
    --url="https://archive.ics.uci.edu/static/public/863/maternal+health+risk.zip" \
    --write-to=data/raw

python scripts/validate_data.py \
    --raw-data="data/raw/Maternal Health Risk Data Set.csv" \
    --data-to=data/processed \
    --log-to=results/logs

python scripts/split_preprocess_data.py \
    --validated-data=data/processed/validated_data.csv \
    --data-to=data/processed \
    --preprocessor-to=results/models

python scripts/fit_maternal_health_risk_classifier.py \
    --training-data=data/processed/maternal_health_risk_train.csv \
    --pipeline-to=results/models \
    --plot-to=results/figures \
    --seed=522
```

#### Clean Up

To shut down the container and clean up the resources, type `Ctrl` + `C` in the terminal where you launched the container, and then run:

``` bash
make stop
```

### Creating a Branch

Once your local environment is up-to-date, you can create a new git branch which will contain your contribution (always create a new branch instead of making changes to the main branch):

``` bash
git switch -c <your-branch-name>
```

With this branch checked-out, make the desired changes to this project.

### Creating a Pull Request

Once you have tested and are happy with your changes, you can commit them to your branch by running:

``` bash
git add <modified-file>
git commit -m "Some descriptive message about your change"
git push origin <your-branch-name>
```

You will then need to submit a pull request (PR) on GitHub asking to merge your branch into the main project repository. Please provide a clear description of the changes you have made and their purpose. Tag a reviewer to ensure that your PR is reviewed in a prompt manner. Reviewers may provide feedback or request changes. Once the PR is approved, you will be able to merge it into the main branch of the project's repository. 

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms. 

## Attribution

These contributing guidelines are adapted from the [altair feedback and contribution guidelines](https://github.com/vega/altair/blob/main/CONTRIBUTING.md).
