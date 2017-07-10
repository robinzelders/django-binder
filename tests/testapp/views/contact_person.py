from binder.views import ModelView

from ..models import ContactPerson

class ContactPersonView(ModelView):
	model = ContactPerson
	unwritable_fields = ['created_at', 'updated_at']
