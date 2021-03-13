from fastapi import Query


class LinkSchema:
    def __init__(self,
                 link: str = Query(
                     ...,
                     description='Enter the link'
                 )):
        self.link = link
