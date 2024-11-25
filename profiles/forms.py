from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = (
            'user',
            'wish_list',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field not in ['default_country', 'profile_image']:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs[
                    'class'
                ] = 'border-black rounded-0 profile-form-input'
                self.fields[field].label = False

        if 'profile_image' in self.fields:
            self.fields['profile_image'].label = "Upload Your Profile Image"
            self.fields['profile_image'].widget.attrs['class'] = (
                self.fields['profile_image'].widget.attrs.get('class', '')
                + ' form-control-file'
            )
