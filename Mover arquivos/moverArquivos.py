import os
from datetime import date

dia = date.today()

#Move e renomea com a data no nome.
os.rename('pasta1/ico.jpg','pasta2/icoMovido_'+str(dia)+'.jpg') 
