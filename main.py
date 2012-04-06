import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from ncspace.ext import captcha
import config

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
			chtml = captcha.displayhtml(
            public_key = config.recaptcha_public_key,
            use_ssl = False,
            error = None)
			template_values = {}
			template_values['captchahtml'] = chtml
			template_values['user_name'] = user.nickname()
			

			path = os.path.join(os.path.dirname(__file__), 'template/index.html')
			self.response.out.write(template.render(path, template_values))
            
        else:
            self.redirect(users.create_login_url(self.request.uri))
	
    def post(self):
	
        # Verification: reCAPTCHA
        challenge = self.request.get('recaptcha_challenge_field')
        response  = self.request.get('recaptcha_response_field')
        remoteip  = os.environ['REMOTE_ADDR']
        template_values = {}
        cResponse = captcha.submit(
                         challenge,
                         response,
                         config.recaptcha_private_key,
                         remoteip)
		
        if cResponse.is_valid:
			template_values['recaptcha_error'] = 0
        else:
            chtml = captcha.displayhtml(
                public_key = config.recaptcha_public_key,
                use_ssl = False,
                error = cResponse.error_code)
            template_values['captchahtml'] = chtml
        user = users.get_current_user()
        template_values['user_name'] = user.nickname()
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        output = template.render(path, template_values)
        self.response.out.write(output)	
		
class AboutPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
			template_values = {
				'user_name': user.nickname()
				}

			path = os.path.join(os.path.dirname(__file__), 'template/about.html')
			self.response.out.write(template.render(path, template_values))
            
        else:
            self.redirect(users.create_login_url(self.request.uri))

class ContactPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
			template_values = {
				'user_name': user.nickname()
				}

			path = os.path.join(os.path.dirname(__file__), 'template/contact.html')
			self.response.out.write(template.render(path, template_values))
            
        else:
            self.redirect(users.create_login_url(self.request.uri))
			
application = webapp.WSGIApplication(
                                     [('/', MainPage),
									 ('/about', AboutPage),
									 ('/contact', ContactPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()