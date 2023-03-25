import pickle
import pandas as pd

""" 
Required package: 
    lightgbm, pickle, pandas

Input: 
    lateral_deviation (ft): standard deviation of lateral wondering
    speed (mile/hr): average speed
    spacing (ft): average spacing
    age (year) : pavement age
    initial_iri (m/km): initial iri of pavement

Output:
    iri (m/km)
"""

def iri_predict(lateral_deviation = 0.83, 
                speed = 50, 
                spacing = 60, 
                age = 4, 
                initial_iri = 0.77):
    
    data = pd.DataFrame.from_dict({'Gator': {0: 4.313781936531054},
                                    'Longitudinal_wp': {0: 4.992986393969996},
                                    'Longitudinal_nwp': {0: 5.29793462202595},
                                    'Patch_area': {0: 0.5},
                                    'Patch_number': {0: 0.0},
                                    'Wp_length': {0: 15.01648977795672},
                                    'Transverse_length_gt183': {0: 0.0},
                                    'Rutting': {0: 5.859497287122277},
                                    'Friction': {0: 33.35714285714279},
                                    'Initial_IRI': {0: 0.77},
                                    'Bc_asphalt_layer_modulus': {0: 52.34346841470218},
                                    'Bc_friction_layer_modulus': {0: 71.51665246581324},
                                    'Hydraulic_conductivity': {0: 9945.68555849306},
                                    'Mon_precip_avg': {0: 41.802987352812906},
                                    'Freeze_index_avg': {0: 17.799766429557273},
                                    'Kesal': {0: 547.4040706749079},
                                    'Kesal_exp_2': {0: 299651.21659145947},
                                    'Age': {0: 4},
                                    'Asphalt_specific_gravity': {0: 1.022550151975684},
                                    'Aggregate_comp_percent': {0: 100.0},
                                    'LATERAL_DEVIATION': {0: 0.83},
                                    'SPEED': {0: 50},
                                    'SPACING': {0: 60}})

    data.loc[0, 'LATERAL_DEVIATION'] = lateral_deviation
    data.loc[0, 'SPEED'] = speed
    data.loc[0, 'SPACING'] = spacing
    data.loc[0, 'Age'] = age
    data.loc[0, 'Initial_IRI'] = initial_iri


    model = pickle.load(open("model.dat", "rb"))
    y_pred = model.predict(data)
    return y_pred

if __name__ == "__main__":
    print('Predicted IRI: ' , iri_predict(), 'm/km')
