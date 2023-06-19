import datetime


class BicycleManager:
    """A class for managing a collection of bicycles."""

    def log_calls(file_path):
        """Decorator that logs method calls to a file."""

        def decorator(func):
            def wrapper(*args, **kwargs):
                current_time = datetime.datetime.now()
                method_name = func.__name__
                call_info = f" {current_time} : {method_name}"

                with open(file_path, 'a') as file:
                    file.write(call_info)

                result = func(*args, **kwargs)

                return result

            return wrapper

        return decorator

    def print_len_of_iterate_object(func):
        """Decorator that prints the length of an iterable object returned by a method."""

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if hasattr(result, '__iter__'):
                length = len(result)
            else:
                length = 1
            print("Length of iterate object is : ", length)
            return result

        return wrapper

    def __init__(self):
        """Initialize a BicycleManager object."""
        self.bicycles = []

    def __iter__(self):
        """Return an iterator for the bicycles collection."""
        return iter(self.bicycles)

    def __len__(self):
        """Return the length of the bicycles collection."""
        return len(self.bicycles)

    def __getitem__(self, item):
        """Get a bicycle from the collection by index."""
        return self.bicycles[item]

    def add_bicycles(self, bicycle):
        """Add a bicycle to the collection."""
        self.bicycles.append(bicycle)

    def find_bicycles_with_max_speed_more_than(self, max_speed):
        """Find bicycles with a maximum speed greater than the given value."""
        return filter(lambda bicycle: bicycle.max_speed > max_speed, self.bicycles)

    def find_bicycles_by_brand(self, brand):
        """Find bicycles by brand."""
        return filter(lambda bicycle: bicycle.brand == brand, self.bicycles)

    def result_of_get_max_distance(self):
        """Return a list of the maximum distances for each bicycle in the collection."""
        return [bicycle.get_max_distance() for bicycle in self.bicycles]

    @log_calls('for_loging_calls')
    def enumerate_objects(self):
        """Enumerate the bicycles in the collection and return a list of index-value pairs."""
        return [
            f"Index => {i} - value => {j}"
            for i, j in enumerate(self.bicycles)
        ]

    def zip_return(self):
        """Return a list of tuples containing a string representation of each bicycle and its maximum distance."""
        return list(zip(map(lambda x: str(x), self.bicycles), self.result_of_get_max_distance()))

    @print_len_of_iterate_object
    def all_and_any(self, condition):
        """
        Check if all or any of the bicycles in the collection satisfy the given condition.

        Args:
            condition: A function that takes a bicycle as input and returns a boolean value.

        Returns:
            A dictionary with 'all' and 'any' keys, indicating if all or any of the bicycles satisfy the condition.
        """
        any_is_electric_bicycle = any(condition(bicycle) for bicycle in self.bicycles)
        all_are_electric_bicycles = all(condition(bicycle) for bicycle in self.bicycles)
        return {"all": all_are_electric_bicycles, "any": any_is_electric_bicycle}
