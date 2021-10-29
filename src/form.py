class Form:
    '''
    Esta clase contiene y especifica los atributos necesarios
    para la creacion de un formulario con los datos oportunos
    para la consulta de una oferta de trabajo. (WIP)
    '''
    def __init__(self,name:str,title:str,location:str,
            department:str,salary_range:list(float),company_profile:str,
            description:str,requirements:str,benefits:str,telecommuting:bool,
            logo:bool, questions:bool, employment_type:str, req_experience:str,
            req_education:str, industry:str, function:str):
            
            self.name = name
            self.title=title
            self.location=location
            self.department=department,
            self.salary_range=salary_range
            self.company_profile=company_profile
            self.description=description
            self.requirements=requirements
            self.benefits=benefits
            self.telecommuting=telecommuting
            self.logo=logo
            self.questions=questions 
            self.employment_type=employment_type
            self.req_experience=req_experience
            self.req_education=req_education
            self.industry =industry
            self.function=function