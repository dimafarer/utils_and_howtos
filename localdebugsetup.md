# sam local debug in WSL

+ install the wsl -remote extension
+ in the root of your project directory create .vscode folder and include the below json in a file named launch.jason
+ when you mount your WSL workspace you must choose your project root folder as the root of your workspace so the workspaceFolder env var works across vscode

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "aws-sam",
            "request": "direct-invoke",
            "name": "[DISPLAY NAME]",
            "invokeTarget": {
                "target": "template",
                "templatePath": "${workspaceFolder}/[path to template]/template.yaml",
                "logicalId": "[FUNCTION NAME IN YAML TEMPLATE]"
            },
            "lambda": {
                "runtime": "python3.12",
                "payload": {},
                "environmentVariables": {
                    "PATH": "/home/wsluser/.local/bin:/usr/local/bin:/usr/bin:${env:PATH}",
                    "PYTHONPATH": "${workspaceFolder}",
                    "PYTHONARGS": "-Xfrozen_modules=off"
                }                
            },
            "sam": {
                "containerBuild": true,
                "dockerNetwork": "bridge"
            },
            "aws": {
                "credentials": "profile:default",
                "region": "us-west-2"
            }            
        }        
    ]
}
```
