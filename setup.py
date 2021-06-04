from setuptools import setup,find_packages
setup(
    name="ashar",
    version="1.1.4",
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='''This project is for data encryption with password protection.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license="Apache Software License",
    packages=find_packages(),
    url="https://github.com/byRo0t96/ashar",
    project_urls={
        'Author WebSite': "https://byro0t96.github.io/",
    },
    install_requires=['pipincluder'],
    keywords=['python', 'ashar', 'encode', 'decode', 'key', 'password', 'encrypt anything with password'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)