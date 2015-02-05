__author__ = 'nickbortolotti'

import os
import jinja2
import webapp2

#Entorno Jinja para trabajar plantillas y el HTML
Entorno_Jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Panel(webapp2.RequestHandler):
    def get(self):
            #Definicion de los datos para insertar en HTML. Jinja2
            plantilla_values = {
                'data': "data",
                'query': "query",
            }

            #Inferencia de la plantilla con el HTML correspondiente
            template = Entorno_Jinja.get_template('paper/newsletter.html')
            self.response.write(template.render(plantilla_values))

application = webapp2.WSGIApplication([
                                    ('/', Panel), ], debug=True)