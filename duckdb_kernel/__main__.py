from ipykernel.kernelapp import IPKernelApp
from .kernel import DuckdbKernel
IPKernelApp.launch_instance(kernel_class=DuckdbKernel)
