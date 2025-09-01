import { z } from "zod";
import { tool } from "@langchain/core/tools";
import { ChatOpenAI } from "@langchain/openai";
import { StateGraph, MessagesAnnotation, Annotation, CompiledGraph } from "@langchain/langgraph";

const getWeather = tool(async ({ city }) => {
  return `It's sunny in ${city}`;
}, {
  name: "get_weather",
  description: "Get the weather for a specific city",
  schema: z.object({
    city: z.string().describe("A city name")
  })
});

const rawModel = new ChatOpenAI({ model: "gpt-4o-mini" });
const model = rawModel.withStructuredOutput(getWeather);

// Extend the base MessagesAnnotation state with another field
const SubGraphAnnotation = Annotation.Root({
  ...MessagesAnnotation.spec,
  city: Annotation<string>,
});

const modelNode = async (state: typeof SubGraphAnnotation.State) => {
  const result = await model.invoke(state.messages);
  return { city: result.city };
};

const weatherNode = async (state: typeof SubGraphAnnotation.State) => {
  const result = await getWeather.invoke({ city: state.city });
  return {
    messages: [
      {
        role: "assistant",
        content: result,
      }
    ]
  };
};

const subgraph = new StateGraph(SubGraphAnnotation)
  .addNode("modelNode", modelNode)
  .addNode("weatherNode", weatherNode)
  .addEdge("__start__", "modelNode")
  .addEdge("modelNode", "weatherNode")
  .addEdge("weatherNode", "__end__")
  .compile({ interruptBefore: ["weatherNode"] });

import { MemorySaver } from "@langchain/langgraph";

const memory = new MemorySaver();

const RouterStateAnnotation = Annotation.Root({
  ...MessagesAnnotation.spec,
  route: Annotation<"weather" | "other">,
});

const routerModel = rawModel.withStructuredOutput(
  z.object({
    route: z.enum(["weather", "other"]).describe("A step that should execute next to based on the currnet input")
  }),
  {
    name: "router"
  }
);

const routerNode = async (state: typeof RouterStateAnnotation.State) => {
  const systemMessage = {
    role: "system",
    content: "Classify the incoming query as either about weather or not.",
  };
  const messages = [systemMessage, ...state.messages]
  const { route } = await routerModel.invoke(messages);
  return { route };
}

const normalLLMNode = async (state: typeof RouterStateAnnotation.State) => {
  const responseMessage = await rawModel.invoke(state.messages);
  return { messages: [responseMessage] };
};

const routeAfterPrediction = async (state: typeof RouterStateAnnotation.State) => {
  if (state.route === "weather") {
    return "weatherGraph";
  } else {
    return "normalLLMNode";
  }
};

const graph = new StateGraph(RouterStateAnnotation)
  .addNode("routerNode", routerNode)
  .addNode("normalLLMNode", normalLLMNode)
  .addNode("weatherGraph", subgraph)
  .addEdge("__start__", "routerNode")
  .addConditionalEdges("routerNode", routeAfterPrediction)
  .addEdge("normalLLMNode", "__end__")
  .addEdge("weatherGraph", "__end__")
  .compile({ checkpointer: memory , });

graph.getGraphAsync({ xray: true }).then(img => console.log(img.drawMermaid()))
// graph TD;
//         __start__([<p>__start__</p>]):::first
//         routerNode(routerNode)
//         normalLLMNode(normalLLMNode)
//         weatherGraph_modelNode(modelNode)
//         weatherGraph_weatherNode(weatherNode<hr/><small><em>__interrupt = before</em></small>)
//         __end__([<p>__end__</p>]):::last
//         __start__ --> routerNode;
//         normalLLMNode --> __end__;
//         weatherGraph_weatherNode --> __end__;
//         routerNode -.-> normalLLMNode;
//         routerNode -.-> weatherGraph_modelNode;
//         routerNode -.-> __end__;
//         subgraph weatherGraph
//         weatherGraph_modelNode --> weatherGraph_weatherNode;
//         end
//         classDef default fill:#f2f0ff,line-height:1.2;
//         classDef first fill-opacity:0;
//         classDef last fill:#bfb6fc;