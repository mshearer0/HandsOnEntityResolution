class RepeatedLabelError(Exception) :
    MESSAGE ='''
ERROR: Unable to tag this string because more than one area of the string has the same label

ORIGINAL STRING:  {original_string}
PARSED TOKENS:    {parsed_string}
UNCERTAIN LABEL:  {repeated_label}

When this error is raised, it's likely that either (1) the string is not a valid person/corporation name or (2) some tokens were labeled incorrectly

To report an error in labeling a valid name, open an issue at {repo_url} - it'll help us continue to improve probablepeople!'''

    DOCS_MESSAGE = '''

For more information, see the documentation at {docs_url}'''
    
    def __init__(self, original_string, parsed_string, repeated_label) :

        self.message = self.MESSAGE.format(original_string=original_string,
                                           parsed_string=parsed_string,
                                           repeated_label=repeated_label,
                                           repo_url=self.REPO_URL)
        if self.DOCS_URL :
            self.message += self.DOCS_MESSAGE.format(docs_url=self.DOCS_URL)

        self.original_string = original_string
        self.parsed_string = parsed_string

    def __str__(self) :
        return self.message
