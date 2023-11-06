#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
int size, elem;

size = PyList_Size(p);

if (size < 0)
{
PyErr_Print();
return;
}
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

for (elem = 0; elem < size; elem++)
{
PyObject *item = PyList_GetItem(p, elem);

printf("Element %d: %s\n", elem, Py_TYPE(item)->tp_name);
}
}
