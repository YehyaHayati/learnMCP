# learnMCP

```mermaid
graph TD;
        __start__([<p>__start__</p>])
        routerNode(routerNode)
        normalLLMNode(normalLLMNode)
        weatherGraph_modelNode(modelNode)
        weatherGraph_weatherNode(weatherNode<hr/><small><em>__interrupt = before</em></small>)
        __end__([<p>__end__</p>])
        __start__ --> routerNode;
        normalLLMNode --> __end__;
        weatherGraph_weatherNode --> __end__;
        routerNode -.-> normalLLMNode;
        routerNode -.-> weatherGraph_modelNode;
        subgraph weatherGraph
        weatherGraph_modelNode --> weatherGraph_weatherNode;
        end
```
