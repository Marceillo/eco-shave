
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Select Images')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
    
    # Changed the widget to support multiple images
    # def __init__(self, attrs=None):
    #     super().__init__(attrs)
        # self.attrs.update({'multiple': True})

        