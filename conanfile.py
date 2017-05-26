from conans import ConanFile

class StatsdClient(ConanFile):
    name = "statsd-client"
    version = "0.0.2"
    license = "MIT"
    url = "https://github.com/vthiery/conan-statsd-client"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = None
    options = {"path": "ANY"}
    default_options = "path="

    def source(self):
        self.run("git clone --recursive https://github.com/vthiery/cpp-statsd-client")

    def build(self):
        del self
        # Do nothing - header only

    def package(self):
        header_dir = "include"
        if self.options.path != "":
            header_dir += "/" + str(self.options.path)
        self.copy("*.hpp", dst=header_dir, src="cpp-statsd-client/src", keep_path=True)

