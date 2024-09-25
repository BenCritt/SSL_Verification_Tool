# This is the form for the SSL Certificate Checker app.
class SSLCheckForm(forms.Form):
    url = forms.CharField(
        label="Enter Website URL",
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "bencritt.net"}),
        error_messages={
            "required": "Please enter a URL.",
            "invalid": "Please enter a valid URL.",
        },
    )

    def clean_url(self):
        url = self.cleaned_data.get("url")

        # Check if URL has a scheme (http or https)
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            # If no scheme is provided, prepend 'https://'
            url = "https://" + url

        return url
