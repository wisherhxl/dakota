from conan import ConanFile
from conan.tools.cmake import cmake_layout

class DakotaRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("boost/1.82.0")
        self.requires("eigen/[>3.0]")

    def build_requirements(self):
        self.tool_requires("cmake/[>3.26]")

    def layout(self):
        cmake_layout(self)
