from spack import *

class Hwloc(Package):
    """The Portable Hardware Locality (hwloc) software package
       provides a portable abstraction (across OS, versions,
       architectures, ...) of the hierarchical topology of modern
       architectures, including NUMA memory nodes, sockets, shared
       caches, cores and simultaneous multithreading. It also gathers
       various system attributes such as cache and memory information
       as well as the locality of I/O devices such as network
       interfaces, InfiniBand HCAs or GPUs. It primarily aims at
       helping applications with gathering information about modern
       computing hardware so as to exploit it accordingly and
       efficiently."""
    homepage = "http://www.open-mpi.org/projects/hwloc/"
    url      = "http://www.open-mpi.org/software/hwloc/v1.9/downloads/hwloc-1.9.tar.gz"

    version('1.9', '1f9f9155682fe8946a97c08896109508')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)

        make()
        make("install")

