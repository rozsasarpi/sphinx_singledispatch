# sphinx singledispatch

Illustration of a sphinx issue with `singledispatch` + `autodoc_mock_imports`.

`docs/conf.py`: if `autodoc_mock_imports` is used together automatically documenting `singledispatch` functions
then the build gets stuck (hangs forever).