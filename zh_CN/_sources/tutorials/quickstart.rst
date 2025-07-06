.. _quickstart:

.. role:: python(code)
    :language: python

Quick-start
=========================

.. note::
    :class: margin

    ``Galyst`` is built on top of `pynbody <http://pynbody.readthedocs.io>`_ and `tangos <http://tangos.readthedocs.io>`_. For advanced usage and deeper understanding, please refer to their documentation.

``Galyst`` is designed for the analysis and management of galaxy simulation data, providing a unified framework for multi-dimensional galaxy property calculations, model fitting, and data management.

- **Data Management** (:mod:`galyst.core`):

    - At the simulation level, `tangos <http://tangos.readthedocs.io>`_ is used to organize and access data from multiple simulations, as well as to store analysis results.
    - At the raw data level, `pynbody <http://pynbody.readthedocs.io>`_ enables reading simulation data files and performing detailed calculations and analyses.

``Galyst`` provides essential tools for calculating galaxy properties across multiple dimensions:

- **Computation** (:mod:`galyst.calculators`):

    - **0D**: Global properties such as mass, size, and angular momentum.
    - **1D**: Radial profiles, including density, age, and metallicity.
    - **2D**: Images, such as surface brightness and velocity fields.

    ``Galyst`` also interfaces with external tools like `agama <https://agama.software/>`_ and `galpy <http://galpy.readthedocs.io>`_ for orbital analysis, and `skirt <https://skirt.ugent.be/root/_home.html>`_ for radiative transfer to generate synthetic observations.

Flexible multi-dimensional model fitting capabilities are available:

- **Model Fitting** (:mod:`galyst.fitting`):

    - **1D**: Fit theoretical profiles, probability density functions, radial density profiles, and star formation history templates.
    - **2D**: Perform multi-component model fitting with `imfit <http://imfit.readthedocs.io>`_, ellipse fitting with `photutils <https://photutils.readthedocs.io>`_, and Fourier decomposition.
    - **3D**: Fit three-dimensional models, such as ellipsoid fitting.

Additionally, ``Galyst`` offers a collection of pre-defined computed properties and methods in :mod:`galyst.properties`.


Setting up Paths
----------------

``Galyst`` uses ``tangos`` to organize and access simulation data. In ``tangos``, the ``TANGOS_SIMULATION_FOLDER`` environment variable should point to your simulation data directory, and ``TANGOS_DB_CONNECTION`` should point to your tangos database.

If these two environment variables are not set, the default paths are:

.. code-block:: bash

    TANGOS_SIMULATION_FOLDER = ~/
    TANGOS_DB_CONNECTION = ~/tangos_data.db

Set the environment variables as follows:

.. code-block:: bash

    export TANGOS_SIMULATION_FOLDER=~/Simulation/sims
    export TANGOS_DB_CONNECTION=~/tangos_data.db

Alternatively, before running Python, you can set them within your script:

.. code-block:: python

    import os

    os.environ['TANGOS_SIMULATION_FOLDER'] = os.path.expanduser('~/Simulation/sims')
    os.environ['TANGOS_DB_CONNECTION'] = os.path.expanduser('~/tangos_data.db')


Connecting to the Database
--------------------------

``Galyst`` automatically connects to the database and creates a new one if needed, initializing the permissions management system.

.. ipython:: python

    from galyst.core import Simulation

If you connect to a database that does not exist, the system will automatically create a new database and set the current user as the database author. 
After running :python:`from galyst.core import Simulation`, you will see output similar to the following, indicating that a new database has been created and the creator has been set as the author:

.. code-block:: text
    :class: full-width

    [2025-07-06 14:16:42.024] < galyst.core.permissions > | INFO | First user detected. Setting as Author.
    [2025-07-06 14:16:42.176] < galyst.core.permissions > | INFO |   - User 'yxi@yxi' has been set as the Author.
    [2025-07-06 14:16:42.337] < galyst.core.permissions > | INFO | Connection successful. User: 'yxi', Roles: ['author']

If the database already exists, you will see similar output indicating a successful connection:

.. code-block:: text
    :class: full-width

    [2025-07-06 14:34:47.458] < galyst.core.permissions > | INFO | Connection successful. User: 'yxi', Roles: ['author']


Adding Simulations
------------------

Before analyzing your data, you need to add your simulation to ``Galyst``. Initially, there are no simulations present.

.. ipython:: python

    print(Simulation.all_simulations())

Here, we add a high-resolution zoom-in simulation. When you use the ``Simulation`` class, it first checks the ``tangos_data.db`` database to see if the simulation already exists. If it does not, it parses the specified path, creates a new simulation instance, and adds it to the database.

.. ipython:: python

    sim = Simulation("~/Simulation/sims/TNG50_l7_Halo274_l11")

    print(sim)

    print(Simulation.all_simulations())

The folder structure is as follows:

.. code-block:: none

    TNG50_l7_Halo274_l11/
    └── output/
        ├── groups_000/
        ├── ...
        ├── groups_099/
        │   ├── fof_subhalo_tab_099.0.hdf5
        │   ├── ...
        │   └── fof_subhalo_tab_099.10.hdf5
        ├── snapdir_000/
        ├── ...
        └── snapdir_099/
            ├── snapshot_099.0.hdf5
            ├── ...
            └── snapshot_099.10.hdf5

When adding a simulation, Galyst will automatically extract some basic properties and store them in the database. You can view these properties with the following code:

.. ipython:: python

    print(sim.properties)

Adding TimeSteps
----------------

You can access all timestep files with the following code:

.. ipython:: python

    print('Number of timestep files:', len(sim.all_timestep_files))

    print('Last timestep file:', sim.all_timestep_files[-1])

You can view the timesteps currently stored in the database. The following code displays the timesteps for this simulation that are not yet stored in the database, so it returns an empty list.

.. ipython:: python

    print(sim.timesteps)

However, you can still access a ``TimeStep`` that has not yet been stored in the database by using a numerical index:

.. ipython:: python

    timestep = sim[99]

    print(timestep)

Alternatively, you can access a specific time step using its unique string identifier from the timestep files. In some cases, this method may be more precise.

.. ipython:: python

    timestep = sim['snap_099']  # or '099'

    print(timestep)

After accessing a ``TimeStep`` in this way, it will automatically be added to the simulation in the database.

.. ipython:: python

    print(sim.timesteps)

.. note::
    :class: margin

    Note that "halos" here typically refer to objects identified by the Subfind algorithm, while "groups" represent larger structures usually found by the FOF algorithm.


Adding Halos
------------

Within a ``TimeStep``, you can inspect information about objects at that particular snapshot.
For example, you can view the halos at this time step. Since no objects have been added yet, this will return an empty list.

.. ipython:: python

    print(timestep.halos())

Next, let's add a halo to this time step.

.. ipython:: python

    timestep.add_halos(max_object=1)

    print(timestep.halos())

Now, ``timestep.halos()`` contains a halo object. You can access it by index:

.. ipython:: python

    halo = timestep.halos()[0]

    print(halo)

Alternatively, you can access a halo by specifying the ``finder_id``:

.. ipython:: python

    print(timestep.halos(finder_id=0))

    halo = timestep.halos(finder_id=0)[0]

The halo object is a :class:`galyst.core.SimulationObject` that contains all the properties of the halo at this time step. You can view all the properties stored in the database for this object. Since nothing has been stored yet, the list will be empty:

.. ipython:: python

    print(halo.keys())

Next, you need to load the particle data for this halo into memory to perform further calculations and analyses.
The variable ``halo_particles`` is a ``SimSnap`` class from ``pynbody``.

.. ipython:: python

    halo_particles = halo.load()
    
    print(halo_particles)


Calculating Basic Properties
----------------------------

A suite of tools for processing particle data is provided in :mod:`galyst.calculators`. Before performing analysis, it is recommended to orient ``halo_particles`` face-on.

.. ipython:: python

    from galyst import calculators

    trans = calculators.transformator.faceon(halo_particles)

You can then use other tools in :mod:`galyst.calculators` for further calculations and analysis. For example, :mod:`galyst.calculators.basic` provides functions for computing fundamental galaxy properties.
For example, to compute the half-mass radius:

.. ipython:: python

    Re = calculators.basic.RadiusContain2D(frac=0.5)

    print(
        "Half-mass radius (total):", Re(halo_particles),
        "\nHalf-mass radius (DM):", Re(halo_particles.dm),
        "\nHalf-mass radius (stars):", Re(halo_particles.s),
        "\nHalf-mass radius (gas):", Re(halo_particles.g),
    )

Here, the ``frac`` parameter specifies the mass fraction used to compute the radius.
Setting ``frac=0.5`` returns the radius containing half of the total mass (i.e., the half-mass radius).

To compute the rotational energy fraction:

.. ipython:: python

    krot = calculators.basic.RotationEnergyFraction()

    print(
        "Rotation energy fraction (total):", krot(halo_particles),
        "\nRotation energy fraction (DM):", krot(halo_particles.dm),
        "\nRotation energy fraction (stars):", krot(halo_particles.s),
        "\nRotation energy fraction (gas):", krot(halo_particles.g),
    )


Calculating 1D Profiles
-----------------------

The :mod:`galyst.calculators.profile` module provides tools for calculating 1D profiles. For example, you can use the basic :class:`galyst.calculators.profile.Profile` class:

.. ipython:: python

    pr = calculators.profile.Profile(halo_particles, ndim=2, rmax=30, qweights='mass')

The ``ndim`` parameter specifies the dimensionality; here, ``2`` indicates that the profile is computed in projection. ``rmax`` sets the maximum radius for the profile, and ``qweights`` determines the weighting used when calculating percentiles.

Let's examine the density profiles for different components:

.. ipython:: python

    import pylab

    @suppress
    pylab.clf()

    pylab.plot(pr['rbins'], pr['density'], label='Total')
    pylab.plot(pr['rbins'], pr['star-density'], label='Stars')
    pylab.plot(pr['rbins'], pr['gas-density'], label='Gas')
    pylab.plot(pr['rbins'], pr['dm-density'], label='Dark Matter')
    pylab.yscale('log')
    pylab.xlabel('Radius ' + f"$[{pr['rbins'].units.latex()}]$")
    pylab.ylabel('Density ' + f"$[{pr['density'].units.latex()}]$")
    pylab.xlim(0, 30)

    @savefig halo_manipulation_denpro.png width=8in
    pylab.legend()

Here, the prefixes ``star-``, ``gas-``, and ``dm-`` specify different matter components.


Let's also look at the distribution of gas temperature:

.. ipython:: python

    @suppress
    pylab.clf()

    pylab.plot(pr['rbins'],pr['gas-temp_50'],c='k')
    pylab.fill_between(pr['rbins'], pr['gas-temp_30'], pr['gas-temp_70'], alpha=0.3, color='grey', label='30-70th percentile')
    pylab.yscale('log')
    pylab.xlabel('Radius '+ f"$[{pr['rbins'].units.latex()}]$")
    pylab.ylabel('Temp '+ f"$[{pr['gas-temp_50'].units.latex()}]$")
    pylab.xlim(0,30)

    @savefig halo_gas_temp_profile.png width=8in
    pylab.legend()

Here, ``gas-temp_50``, ``gas-temp_30``, and ``gas-temp_70`` represent the 50th, 30th, and 70th percentiles of the gas temperature, respectively.


Plotting Halo Images
--------------------

The :mod:`galyst.calculators.image` module provides tools for generating images of halos.

For example, to plot the gas surface density distribution:

.. ipython:: python

    @suppress
    pylab.clf()

    from galyst.calculators import image as im

    im_g = im.sph_projection(halo_particles.g, width='60 kpc', units='Msol kpc^-2')

    @savefig halo_gas_surface_density.png width=8in
    im_g.show()

Gas Metallicity

.. ipython:: python

    @suppress
    pylab.clf()

    im_g_metals = im.sph_projection(halo_particles.g, quantity='metals', width='60 kpc')

    @savefig halo_gas_metallicity.png width=8in
    im_g_metals.show()

To plot the stellar luminosity image:

.. ipython:: python

    @suppress
    pylab.clf()

    im_s = im.star_luminosity_image(halo_particles, width='60 kpc')

    @savefig halo_star_luminosity.png width=8in
    im_s.show()

You can see a short bar in the center. Let's examine its kinematic features:

.. ipython:: python

    @suppress
    pylab.clf()

    im_s_m = im.sph_projection(halo_particles.s, smooth_floor=0.1, units='Msol kpc^-2', width='5 kpc')
    im_s_v = im.sph_projection(halo_particles.s, smooth_floor=0.1, quantity='vrxy', width='5 kpc')


    image = im_s_v.show()

    @savefig halo_star_velocity.png width=8in
    im_s_m.show_contour(image)
