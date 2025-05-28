from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import http.client
import json


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class SerperApiDevTool(BaseTool):
    name: str = "serper_dev"  # Use o mesmo nome referenciado no agents.yaml
    description: str = "Ferramenta para buscar resultados reais na web via Serper Dev API."
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> Any:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": argument,
            "tbs": "qdr:w"
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY", ""),
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        if res.status != 200:
            raise RuntimeError(f"Serper API error {res.status}: {data.decode()}")
        return json.loads(data)

    async def _arun(self, argument: str) -> Any:
        # Reaproveita o código síncrono
        return self._run(argument)