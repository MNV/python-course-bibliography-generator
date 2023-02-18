# Bibliography Generator

Console application for creating a bibliography list.

The application allows you to automate the process of generating a bibliography list according to the specified citation standard.

Supported citation styles:
- ГОСТ Р 7.0.5-2008 
- American Psychological Association (APA)

## Installation

Clone the repository to your computer:
```bash
git clone https://github.com/mnv/python-course-bibliography-generator.git
```

### Requirements:

Install the appropriate software:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Usage

1. Copy the given template file into the input Excel file that will allow you
to fill it without changing the original template:
    ```shell
    cp media/template.xlsx media/input.xlsx
    ```
   
2. To configure the application copy `.env.sample` into `.env` file:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

3. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.

4. To see the documentation for the console command run:
    ```shell
    docker compose run app python main.py --help
    ```
   
5. Now it is possible to run the command inside the Docker container 
    as usual, passing needed arguments to the console application:
    ```shell
    docker compose run app python main.py --citation gost --path_input /media/input.xlsx --path_output /media/output.docx
    ```
   
   Also, it is possible to omit the arguments to use their defaults:
    ```shell
    docker compose run app python main.py
    ```

### Automation commands

The project contains a special `Makefile` that provides shortcuts for a set of commands:
1. Build the Docker container:
    ```shell
    make build
    ```

2. Generate Sphinx documentation run:
    ```shell
    make docs-html
    ```

3. Autoformat source code:
    ```shell
    make format
    ```

4. Static analysis (linters):
    ```shell
    make lint
    ```

5. Autotests:
    ```shell
    make test
    ```

    The test coverage report will be located at `src/htmlcov/index.html`. 
    So you can estimate the quality of automated test coverage.

6. Run autoformat, linters and tests in one command:
    ```shell
    make all
    ```

Run these commands from the source directory where `Makefile` is located.

## Documentation

The project integrated with the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation engine. 
It allows the creation of documentation from source code. 
So the source code should contain docstrings in [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

To create HTML documentation run this command from the source directory where `Makefile` is located:
```shell
make docs-html
```

After generation documentation can be opened from a file `docs/build/html/index.html`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
