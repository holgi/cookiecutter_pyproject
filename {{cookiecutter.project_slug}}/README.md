{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

## Example:

```python

    import {{ cookiecutter.project_slug }}

    {{ cookiecutter.project_slug }}.run()
```


## Development

To install the development version of SartoriUSB:

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

    # create a virtual environment and install all required dev dependencies
    cd {{ cookiecutter.project_slug }}
    make setupdev

To run the tests, use `make tests` or `make coverage` for a complete report.
