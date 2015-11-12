import importlib

class VersionedEndpoint:
	"""
	Versions APIView endpoints
	"""

	def class_for_name(self, module_name, class_name):
		# load the module, will raise ImportError if module cannot be loaded
		m = importlib.import_module(module_name)
		# get the class, will raise AttributeError if class cannot be found
		c = getattr(m, class_name)
		return c

	def to_class(self, path):
		components = path.rsplit('.',1)
		return self.class_for_name(components[0], components[1])


	def numerical_version(self, version_string):
		return float(version_string)

	def dispatch(self, request, *args, **kwargs):
		"""
		`.dispatch()` is pretty much the same as Django's regular dispatch,
		but with extra hooks for startup, finalize, and exception handling.

		Now handles versioning of endpoints through versioning parameter loading in the correct view depending on version.
		"""
		self.args = args
		self.kwargs = kwargs
		request = self.initialize_request(request, *args, **kwargs)
		self.request = request
		self.headers = self.default_response_headers  # deprecate?

		try:
			self.initial(request, *args, **kwargs)

			if hasattr(self, 'versions') is False:
				raise Exception("Attempted to use a versioned endpoint without specifying versions. VersionedEndpoint requires a 'self.versions' dictionary")

			version = self.determine_version(self.request, *args, **kwargs)
			version = self.numerical_version(version[0])
			version_class = self.versions.get(version, None)
			if version_class is None:
				version_keys = self.versions.keys()
				latest_version = max(version_keys)
				version_class = self.versions.get(latest_version)
			return self.to_class(version_class).as_view()(request, *args, **kwargs)

		except Exception as exc:
			response = self.handle_exception(exc)

		self.response = self.finalize_response(request, response, *args, **kwargs)
		return self.response
