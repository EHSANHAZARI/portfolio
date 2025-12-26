class Project :

    """
    Represent a project class showcasing the project's information.
    """
    def __init__ (
            self,
            id : int,  
            title : str, 
            type : str,  
            link : str , 
            explanations : list[str],
            image :  str | None , 
    ):
        
        """  
        Verb <thing>; used for <purpose>; <constraints/examples if any>.

        Docstring for __init__
        
        :param self: Represent a instance object pointing to the object itself
        :param id: Represent a unique project identifier used for internal refrencing 
        :param title: Display the name of the project 
        :param type: Dsiplay the project category 
        :param link: Dsiplay the link to the project 
        :param explanations: Display the bulle-point explaining the project descriptions 
        :param image: Display the image of the project 

        """

        self.id : id
        self.title : title
        self.type : type
        self.link : link
        self.explanations : explanations
        self.image : image
