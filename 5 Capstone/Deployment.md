
# Deployment


## SaaS vs PaaS vs IaaS

|    | description | examples |
|--- |---          |---       |
| SaaS | Software as a Service: they provide nearly everything through an interface of their web application | Wordpress, Squarespace |
| PaaS | Platform as a Service:  they provide the software and hardware, you copy files over and configure | PythonAnywhere, NearlyFreeSpeech, Windows Azure, AWS |
| IaaS | Infrastructure as a Service: they provide the hardware, you install software | Digital Ocean, AWS |
| Self-hosted | You manage all the software and hardware |    |

[read more](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/)


## Domain registrars



## Deploying with Python Anywhere

[tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject), [video](https://www.youtube.com/watch?v=Y4c4ickks2A)


How to print to the error log on pythonanywhere

```python
import sys
print('check the error log', file=sys.stderr)
```

Find more info about virtual environments [here](https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/docs/Virtual%20Environments.md)

Deploying with Django channels is [more complicated](https://channels.readthedocs.io/en/latest/deploying.html)
