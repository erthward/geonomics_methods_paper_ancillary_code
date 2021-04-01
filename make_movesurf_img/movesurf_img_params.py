# movesurf_img_params.py

# This is a parameters file generated by Geonomics
# (by the gnx.make_parameters_file() function).


                   ##  ::::::          :::    :: ::::::::::##
             ##:::::    ::::   :::      ::    :: :: ::::::::::: :##
          ##::::::::     ::            ::   ::::::::::::::::::::::::##
        ##:::::::::                      :::::::::: :::::: ::::::::  :##
      ## : ::::  ::                    ::::  : ::    :::::::: : ::  :   ##
     ##GGGGG  EEEEE OOOOO   NN   NN   OOOOO   MM   MM IIIIII  CCCCC SSSSS##
    ##GG     EE    OO   OO  NNN  NN  OO   OO  MM   MM   II   CC     SS    ##
    ##GG     EE   OO     OO NN N NN OO     OO MMM MMM   II   CC     SSSSSS##
    ##GG GGG EEEE OO     OO NN  NNN OO     OO MM M MM   II   CC         SS##
    ##GG   G EE    OO   OO  NN   NN  OO   OO  MM   MM   II   CC        SSS##
     ##GGGGG  EEEEE OOOOO   NN   NN   OOOOO   MM   MM IIIIII  CCCCC SSSSS##
      ##    :::::::::               :::::::::: ::              ::  :   :##
        ##:   :::::                    :::::: :::             ::::::: ##
          ##   :::                      :::::  ::              :::::##
             ## ::                      ::::                     ##
                   ##                                      ##
                      ## :: ::    :::            ##


params = {
#-----------------------------------------------------------------------------#

#-----------------#
#--- LANDSCAPE ---#
#-----------------#
    'landscape': {

    #------------#
    #--- main ---#
    #------------#
        'main': {
            #y,x (a.k.a. i,j) dimensions of the Landscape
            'dim':                      (8,8),
            #resolution of the Landscape
            'res':                      (1,1),
            #upper-left corner of the Landscape
            'ulc':                      (0,0),
            #projection of the Landscape
            'prj':                      None,
            }, # <END> 'main'

    #--------------#
    #--- layers ---#
    #--------------#
        'layers': {

            #layer name (LAYER NAMES MUST BE UNIQUE!)
            'lyr_0': {

        #-------------------------------------#
        #--- layer num. 0: init parameters ---#
        #-------------------------------------#

                #initiating parameters for this layer
                'init': {

                    #parameters for a 'file'-type Layer
                    'file': {
                        #</path/to/file>.<ext>
                        'filepath': ('/home/drew/Desktop/stuff/berk/research/'
                                     'projects/sim/methods_paper/make_movesurf_img/'
                                     'movesurf_lyr.txt'),
                        #minimum value to use to rescale the Layer to [0,1]
                        'scale_min_val':                None,
                        #maximum value to use to rescale the Layer to [0,1]
                        'scale_max_val':                None,
                        #decimal precision to use for coord-units (ulc & res)
                        'coord_prec':                   5,
                        #units of this file's variable
                        'units':                        None,

                        }, # <END> 'file'

                    }, # <END> 'init'

                }, # <END> layer num. 0



    #### NOTE: Individual Layers' sections can be copy-and-pasted (and
    #### assigned distinct keys and names), to create additional Layers.


            } # <END> 'layers'

        }, # <END> 'landscape'


#-----------------------------------------------------------------------------#

#-----------------#
#--- COMMUNITY ---#
#-----------------#
    'comm': {

        'species': {

            #species name (SPECIES NAMES MUST BE UNIQUE!)
            'spp_0': {

            #-----------------------------------#
            #--- spp num. 0: init parameters ---#
            #-----------------------------------#

                'init': {
                    #starting number of individs
                    'N':                250,
                    #carrying-capacity Layer name
                    'K_layer':          'lyr_0',
                    #multiplicative factor for carrying-capacity layer
                    'K_factor':         1,
                    }, # <END> 'init'

            #-------------------------------------#
            #--- spp num. 0: mating parameters ---#
            #-------------------------------------#

                'mating'    : {
                    #age(s) at sexual maturity (if tuple, female first)
                    'repro_age':                0,
                    #whether to assign sexes
                    'sex':                      False,
                    #ratio of males to females
                    'sex_ratio':                1/1,
                    #whether P(birth) should be weighted by parental dist
                    'dist_weighted_birth':       False,
                    #intrinsic growth rate
                    'R':                        0.5,
                    #intrinsic birth rate (MUST BE 0<=b<=1)
                    'b':                        0.2,
                    #expectation of distr of n offspring per mating pair
                    'n_births_distr_lambda':    1,
                    #whether n births should be fixed at n_births_dist_lambda
                    'n_births_fixed':           True,
                    #radius of mate-search area
                    'mating_radius':            10,
                    }, # <END> 'mating'

            #----------------------------------------#
            #--- spp num. 0: mortality parameters ---#
            #----------------------------------------#

                'mortality'     : {
                    #maximum age
                    'max_age':                      None,
                    #min P(death) (MUST BE 0<=d_min<=1)
                    'd_min':                        0,
                    #max P(death) (MUST BE 0<=d_max<=1)
                    'd_max':                        1,
                    #width of window used to estimate local pop density
                    'density_grid_window_width':    None,
                    }, # <END> 'mortality'

            #---------------------------------------#
            #--- spp num. 0: movement parameters ---#
            #---------------------------------------#

                'movement': {
                    #whether or not the species is mobile
                    'move':                     True,
                    #mode of distr of movement direction
                    'direction_distr_mu':       0,
                    #concentration of distr of movement direction
                    'direction_distr_kappa':    0,
                    #mean of distr of movement distance
                    'movement_distance_distr_param1':        0.25,
                    #variance of distr of movement distance
                    'movement_distance_distr_param2':     0.25,
                    'movement_distance_distr':     'wald',
                    #mean of distr of dispersal distance
                    'dispersal_distance_distr_param1':       0.25,
                    #variance of distr of dispersal distance
                    'dispersal_distance_distr_param2':    0.25,
                    'dispersal_distance_distr':   'wald',
                    'move_surf'     : {
                        #move-surf Layer name
                        'layer':                'lyr_0',
                        #whether to use mixture distrs
                        'mixture':              True,
                        #concentration of distrs
                        'vm_distr_kappa':       12,
                        #length of approximation vectors for distrs
                        'approx_len':           5000,
                        }, # <END> 'move_surf'

                    },    # <END> 'movement'



                }, # <END> spp num. 0



    #### NOTE: individual Species' sections can be copy-and-pasted (and
    #### assigned distinct keys and names), to create additional Species.


            }, # <END> 'species'

        }, # <END> 'comm'


#-----------------------------------------------------------------------------#

#-------------#
#--- MODEL ---#
#-------------#
    'model': {
        #total Model runtime (in timesteps)
        'T':            100,
        #min burn-in runtime (in timesteps)
        'burn_T':       30,
        #seed number
        'num':          None,
        'tskit_simp_interval':  100,

        #-----------------------------#
        #--- iterations parameters ---#
        #-----------------------------#
        'its': {
            #num iterations
            'n_its':            1,
            #whether to randomize Landscape each iteration
            'rand_landscape':   False,
            #whether to randomize Community each iteration
            'rand_comm':        False,
            #whether to burn in each iteration
            'repeat_burn':      False,
            }, # <END> 'iterations'



        } # <END> 'model'

    } # <END> params
