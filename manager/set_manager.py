class SetManager:
    """A class for managing a set of qualities from a collection of bicycles."""

    def __init__(self, bicycle_manager):
        """
        Initialize a SetManager object.

        Args:
            bicycle_manager: An instance of BicycleManager containing the collection of bicycles.
        """
        self.bicycle_manager = bicycle_manager
        self.bicycle_index = 0
        self.quality_index = 0

    def __iter__(self):
        """Return an iterator over the qualities from the bicycles in the collection."""
        for bicycle in self.bicycle_manager.bicycles:
            for qualities in bicycle.the_best_qualities:
                yield qualities

    def __len__(self):
        """Return the total number of qualities from all the bicycles in the collection."""
        length = 0
        for bicycle in self.bicycle_manager.bicycles:
            length += len(bicycle.the_best_qualities)
        return length

    def __getitem__(self, item):
        """
        Get a quality from the set by index.

        Args:
            item: The index of the quality.

        Returns:
            The quality at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        for bicycle in self.bicycle_manager.bicycles:
            qualities_list = list(bicycle.the_best_qualities)
            if item < len(qualities_list):
                return qualities_list[item]
            item -= len(qualities_list)
        raise IndexError("Index out of range")

    def __next__(self):
        """
        Return the next quality from the set.

        Returns:
            The next quality in the set.

        Raises:
            StopIteration: If there are no more qualities in the set.
        """
        if self.bicycle_index >= len(self.bicycle_manager.bicycles):
            raise StopIteration

        bicycle = self.bicycle_manager.bicycles[self.bicycle_index]
        qualities_list = list(bicycle.the_best_qualities)

        if self.quality_index >= len(qualities_list):
            self.bicycle_index += 1
            self.quality_index = 0
            return self.__next__()

        value = qualities_list[self.quality_index]
        self.quality_index += 1
        return value
