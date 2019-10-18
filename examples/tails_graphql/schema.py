from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel
from models import Perro as PerroModel


import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType




class Perro(SQLAlchemyObjectType):
    class Meta:
        model = PerroModel
        interfaces = (relay.Node, )


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    employee = relay.Node.Field(Employee)
    # Allow only single column sorting
    all_employees = SQLAlchemyConnectionField(
        Employee, sort=Employee.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    all_roles = SQLAlchemyConnectionField(Role)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department, sort=None)

    all_perros = SQLAlchemyConnectionField(Perro)

    find_perro = graphene.Field(lambda: Perro, name=graphene.String(), years=graphene.String())

    def resolve_find_perro(self, info, name, years):
        perro_query = Perro.get_query(info)
        query = perro_query.filter_by(name=name, years=years).first()
        return query



schema = graphene.Schema(query=Query, types=[Department, Employee, Role, Perro])
