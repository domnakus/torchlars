from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="torchlars",
    packages=["torchlars"],
    package_dir={"torchlars": "torchlars"},
    ext_modules=[
        CUDAExtension(
            "torchlars._adaptive_lr",
            ["torchlars/adaptive_lr.cc", "torchlars/adaptive_lr_cuda.cu"],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
