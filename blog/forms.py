from PIL import Image
from django import forms
from django.forms import FileInput, TextInput

from .models import Blog
from django.utils.translation import ugettext as _


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('published_at',)
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Введите название статьи'}),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget = FileInput(attrs={
            'id': 'go',
            'onchange': 'readURL(this)',
            'class': 'choose_file',
            'Placeholder': 'Upload'
        })

    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        if image:
            img = Image.open(image)
            w, h = img.size

            # validate dimensions
            max_width = max_height = 715
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    _('Please use an image that is smaller or equal to '
                      '%s x %s pixels.' % (max_width, max_height)))

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
                raise forms.ValidationError(_('Please use a JPEG or PNG image.'))

            # validate file size
            if len(image) > (1 * 1024 * 1024):
                raise forms.ValidationError(_('Image file too large ( maximum 1mb )'))
        else:
            raise forms.ValidationError(_("Couldn't read uploaded image"))
        return image
