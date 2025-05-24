from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from py2neo import Graph
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "cr8UuA6Te6Gyt_U"))

# Input schema
class UserRequest(BaseModel):
    user_name: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/recommendations")
def recommend_cities(request: UserRequest):
    user_name = request.user_name

    query = """
    MATCH (u:User {name: $userName})-[:VISITED|LIKES]->(p1)
    WITH u, collect(DISTINCT p1) AS userPlaces

    MATCH (other:User)-[:VISITED|LIKES]->(p2)
    WHERE other <> u AND p2 IN userPlaces

    MATCH (other)-[:VISITED]->(recPlace:Place)-[:LOCATED_IN]->(recCity:City)
    WHERE NOT (u)-[:VISITED]->(:Place)-[:LOCATED_IN]->(recCity)

    RETURN recCity.name AS recommendedCity, count(*) AS score
    ORDER BY score DESC
    LIMIT 5
    """

    try:
        result = graph.run(query, userName=user_name)
        recommendations = [
            {"city": record["recommendedCity"], "score": record["score"]}
            for record in result
        ]
        print(recommendations)
        return {"user": user_name, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
