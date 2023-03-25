from iri_predict import iri_predict 


iri = iri_predict(lateral_deviation = 0.83, 
                speed = 50, 
                spacing = 60, 
                age = 4, 
                initial_iri = 0.77)
print('Predicted IRI: ' , iri, 'm/km')