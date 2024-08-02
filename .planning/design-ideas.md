# Entities

First level entities:
* Chatbots: pipelines which can be deployed with chat interface
* Jobs: pipelines which can be executed on demand or on schedule

Second level entities (building blocks):
* Scripts: custom python scripts which interacts with standard parts using a unified interface
* Agents: pre-made GenAI agents (no-code or based on a script)
* Knowledge Bases: information retrieval system (no-code or based on a script)
* Tools: functions agents can execute (no-code or based on a script)
* Connectors: access providers to external resources (no-code or based on a script)
* Deployments: where to deploy chatbots and jobs. For now it will be only local, inprocess with the app.
* Model selectors?

Non-user facing entities:
* Pipeline: well, the thing itself
* Step: a step in a pipeline. Here are some step types
    * ChatIngress: abstract interface which offers ChatAPI access of specific implementation (langserve, OpenAI, etc). Mandatory for Chatbot pipeline.
    * Selector: abstract selector, like model selector or database selector.
    * Agent or LLM
    * Script
* PipelineExecutor and StepExecutor

> I am not entirely sure that I should use a term Pipeline for Chatbots. They won't be
> passing data down in the pipeline, they will be just implementations of Chatbots
> with various functions (or without them). But they also should have a drag'n'drop
> interface. But its a DAG per-se, connections will be bi-directional. So there should be
> a better representation.

## Connectors

Connectors should serve as an inventory of external resources for the system. They should provide an
interface to configure authentication and authorization (specific permissions) to external resources.

Examples of connectors:

* remote system (SSH)
* craftai (rewriting itself)
* data storages: vector databases, (No)SQL databases, graph databases, information retrieval systems, knowledge databases
* access to the internet
* OpenAPI specification
* GSuite, social networks
* smart Home systems
* llm providers

So connectors are responsible for all remote IO in the system. No remote IO should be happening without a connector.

> For now, this rule is more of a reference to follow, but in the future for proper sandboxing of custom scripts we may enforce it:
> 1. Run a script without a network access
> 2. Provide access to API proxies

## Scripts

For now, only Python scripts. Script should implement a function `execute(inputs: dict[str, Any], config[str, Any], connectors: list) -> dict[str, Any]`. Context argument provides access to the inputs from previous steps, configs, and connectors. The function should return script output results, using only provided arguments.

> Ideas for proper sandboxing:
> 1. Script is run in docker with no ingress/egress by default
> 2. Connectors define ALLOW rules
> 3. Additional checks in script: heurestics to detect malicious code, and maybe a check by LLM?

Script can be used as a standalone step, or as a basis for other entity so it can be seamlessly plugged into something else: a tool for an agent for example.

# Pipeline represenation
Framework: [React Flow](https://reactflow.dev/)

Examples for jobs:
* [Attio](https://attio.com/product/automations)

Examples for chatbots:
* https://github.com/langflow-ai/langflow
