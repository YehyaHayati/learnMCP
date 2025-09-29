# learnMCP

```mermaid
graph TD;
<<<<<<< Updated upstream
        __start__([<p>__start__</p>])
=======
        __start__([<p>__start__</p>]):::first
>>>>>>> Stashed changes
        routerNode(routerNode)
        normalLLMNode(normalLLMNode)
        weatherGraph_modelNode(modelNode)
        weatherGraph_weatherNode(weatherNode<hr/><small><em>__interrupt = before</em></small>)
<<<<<<< Updated upstream
        __end__([<p>__end__</p>])
=======
        __end__([<p>__end__</p>]):::last
>>>>>>> Stashed changes
        __start__ --> routerNode;
        normalLLMNode --> __end__;
        weatherGraph_weatherNode --> __end__;
        routerNode -.-> normalLLMNode;
        routerNode -.-> weatherGraph_modelNode;
<<<<<<< Updated upstream
        subgraph weatherGraph
        weatherGraph_modelNode --> weatherGraph_weatherNode;
        end
```
=======
        routerNode -.-> __end__;
        subgraph weatherGraph
        weatherGraph_modelNode --> weatherGraph_weatherNode;
        end
        classDef 0 b;
        classDef 1 l;
        classDef 2 a;
        classDef 3 c;
        classDef 4 k;
```
>>>>>>> Stashed changes
