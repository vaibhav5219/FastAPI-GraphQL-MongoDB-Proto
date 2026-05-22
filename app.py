from fastapi import FastAPI
import strawberry
from query import Query
from mutation import Mutation
from strawberry.fastapi import GraphQLRouter

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphqlApp = GraphQLRouter(schema=schema)

app = FastAPI()

app.include_router(graphqlApp, prefix="/graphql")
