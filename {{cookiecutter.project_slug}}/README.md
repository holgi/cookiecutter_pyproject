{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

## Example:

```python

    import {{ cookiecutter.project_slug }}

    {{ cookiecutter.project_slug }}.run()
```


## Development

To install the development version of {{ cookiecutter.project_name }}:

    git clone {{ cookiecutter.remote_git_repo }}

    # create a virtual environment and install all required dev dependencies
    cd {{ cookiecutter.project_slug }}
    make devenv

To run the tests, use `make tests` or `make coverage` for a complete report.
