import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberrycurve.field_element import FieldElement

@strawberry.type
class Query:
    @strawberry.field
    def hello_curve(self) -> str:
        return 'Hello world!'
    
@strawberry.type
class Mutation:
    @strawberry.field
    def write_field_element(self, x: int, y:int) -> str:
        fe = FieldElement(x,y)
        return f'{fe.__repr__()}'

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")