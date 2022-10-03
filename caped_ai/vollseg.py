from vollseg import UNET, StarDist2D, StarDist3D, MASKUNET

class StarDist3D(StarDist3D):
     def __init__(self, config, name=None, basedir='.'):
        super().__init__(config=config, name=name, basedir=basedir) 
        
class StarDist2D(StarDist2D):
     def __init__(self, config, name=None, basedir='.'):
        super().__init__(config=config, name=name, basedir=basedir)         
        
class UNET(UNET):
        def __init__(self, config, name=None, basedir='.'):
            """See class docstring."""
            super().__init__(config=config, name=name, basedir=basedir)        
            
class MASKUNET(MASKUNET):
        def __init__(self, config, name=None, basedir='.'):
            """See class docstring."""
            super().__init__(config=config, name=name, basedir=basedir)             