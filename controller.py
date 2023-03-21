class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email, first_name):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.first_name = first_name
            self.model.save()

            # show a success message
            self.view.show_success(f'{email} and {first_name} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
